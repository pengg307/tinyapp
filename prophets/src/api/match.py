"""匹配接口：用户答案 → 匹配结果"""

from __future__ import annotations

import numpy as np
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import Any

from src.data.figures import load_figures
from src.data.questions import load_questions
from src.engine.vector import euclidean_distance
from src.engine.matcher import match
from src.engine.analyzer import analyze_gaps
from src.api.suggestions import generate_suggestions

router = APIRouter()


class AnswerItem(BaseModel):
    """用户答案"""
    question_id: int
    option_index: int


class MatchRequest(BaseModel):
    """匹配请求"""
    answers: list[AnswerItem]


class MatchResponse(BaseModel):
    """匹配响应"""
    success: bool
    matches: list[dict[str, Any]]
    user_vector: dict[str, float]
    summary: str = ""


def calculate_user_vector(answers: list[dict], questions_data: list[dict]) -> np.ndarray:
    """根据答案计算用户向量"""
    # 选项映射到维度分数
    option_scores = {
        0: 0.2,  # 低分选项
        1: 0.5,  # 中等偏低
        2: 0.7,  # 中等偏高
        3: 1.0   # 高分选项
    }
    
    # 按trait分组题目
    trait_questions = {}
    for q in questions_data:
        trait = q.get("trait", "")
        if trait not in trait_questions:
            trait_questions[trait] = []
        trait_questions[trait].append(q)
    
    # 计算每个维度的平均分数
    user_values = {}
    for trait, questions in trait_questions.items():
        scores = []
        for q in questions:
            qid = q.get("id")
            for ans in answers:
                if ans.question_id == qid:
                    opt_idx = ans.option_index
                    scores.append(option_scores.get(opt_idx, 0.5))
                    break
        if scores:
            user_values[trait] = sum(scores) / len(scores)
        else:
            user_values[trait] = 0.5
    
    # 确保所有12个维度都有值
    trait_order = ["openness", "conscientiousness", "extraversion", "agreeableness", 
                   "neuroticism", "leadership", "risk_taking", "rationality", 
                   "discipline", "empathy", "ambition", "resilience"]
    
    vector = np.array([user_values.get(t, 0.5) for t in trait_order])
    return vector


def match_euclidean(user_vector: np.ndarray, figure_vectors: dict, top_k: int = 10) -> list[dict]:
    """使用欧氏距离进行匹配"""
    results = []
    for fig_id, fig_vec in figure_vectors.items():
        dist = euclidean_distance(user_vector, fig_vec)
        # 转换为相似度 (0-1, 1表示完全匹配)
        similarity = np.exp(-(dist ** 2) / 2)
        results.append({
            "figure_id": fig_id,
            "distance": dist,
            "similarity": float(similarity)
        })
    
    # 按相似度降序排序
    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:top_k]


def generate_summary(user_vector: np.ndarray, top_match: dict, language: str = "zh") -> str:
    """生成匹配总结"""
    if not top_match:
        return ""
    
    name = top_match.get("name", "历史人物")
    
    # 找出用户最高和最低的维度
    trait_names = {
        "zh": ["开放性", "尽责性", "外向性", "宜人性", "情绪稳定性", 
               "领导力", "风险偏好", "理性度", "自律性", "共情力", "野心", "韧性"],
        "en": ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", 
               "Emotional Stability", "Leadership", "Risk Taking", "Rationality", 
               "Discipline", "Empathy", "Ambition", "Resilience"],
    }
    
    traits_zh = trait_names.get(language, trait_names["zh"])
    max_idx = np.argmax(user_vector)
    min_idx = np.argmin(user_vector)
    
    return f"您与{name}最为相似，在{traits_zh[max_idx]}方面表现突出，在{traits_zh[min_idx]}方面有待提升。"


@router.post("/match", response_model=MatchResponse)
def match_user(
    request: MatchRequest,
    language: str = Query("zh", pattern="^(zh|en|es|ja|de|ru|fr)$")
) -> MatchResponse:
    """
    根据用户答案匹配最相似的历史人物
    
    Args:
        request: 用户答案列表
        language: 语言代码 (zh/en/es/ja/de/ru/fr)，默认中文
    
    Returns:
        匹配结果
    """
    # 加载题目和人物
    questions_data = load_questions()
    figures_data = load_figures()
    
    # 计算用户向量（根据答案计算）
    user_vector = calculate_user_vector(request.answers, questions_data)
    
    # 构建人物向量字典
    figure_vectors = {}
    for fig in figures_data:
        figure_vectors[fig["id"]] = np.array(list(fig["vector"].values()))
    
    # 使用欧氏距离匹配
    results = match_euclidean(user_vector, figure_vectors, top_k=10)
    
    # 构建响应
    matches = []
    for r in results:
        fig = next(f for f in figures_data if f["id"] == r["figure_id"])
        gaps = analyze_gaps(user_vector, figure_vectors[r["figure_id"]])
        suggestion = generate_suggestions(gaps, fig["type"], language)
        
        # 获取多语言名字
        names = fig.get("names", {})
        
        matches.append({
            "figure_id": r["figure_id"],
            "name": names.get(language, names.get("zh", fig["name"])),
            "name_en": names.get("en", ""),
            "name_zh": names.get("zh", fig["name"]),
            "name_ja": names.get("ja", ""),
            "era": fig.get("era", ""),
            "type": fig.get("type", ""),
            "similarity": r["similarity"],
            "gaps": gaps,
            "suggestion": suggestion
        })
    
    # 生成总结
    top_match = matches[0] if matches else None
    summary = generate_summary(user_vector, top_match, language) if top_match else ""
    
    return MatchResponse(
        success=True,
        matches=matches,
        user_vector={k: float(v) for k, v in zip(
            ["openness", "conscientiousness", "extraversion", "agreeableness", 
             "neuroticism", "leadership", "risk_taking", "rationality", 
             "discipline", "empathy", "ambition", "resilience"],
            user_vector
        )},
        summary=summary
    )
