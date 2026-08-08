"""匹配接口：用户答案 → 匹配结果"""

from __future__ import annotations

import numpy as np
from fastapi import APIRouter, HTTPException
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


@router.post("/match", response_model=MatchResponse)
def match_user(
    request: MatchRequest,
) -> MatchResponse:
    """
    根据用户答案匹配最相似的历史人物
    
    Args:
        request: 用户答案列表
        
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
        suggestion = generate_suggestions(gaps, fig["type"])
        
        matches.append({
            "figure_id": r["figure_id"],
            "name": fig["name"],
            "name_en": fig.get("name_en", ""),
            "name_zh": fig.get("name_zh", fig["name"]),
            "similarity": r["similarity"],
            "gaps": gaps,
            "suggestion": suggestion
        })
    
    return MatchResponse(
        success=True,
        matches=matches,
        user_vector={k: float(v) for k, v in zip(
            ["openness", "conscientiousness", "extraversion", "agreeableness", 
             "neuroticism", "leadership", "risk_taking", "rationality", 
             "discipline", "empathy", "ambition", "resilience"],
            user_vector
        )}
    )


def calculate_user_vector(answers: list[AnswerItem], questions_data: list) -> np.ndarray:
    """根据用户答案计算用户性格向量"""
    # 初始化12维向量为0.5
    vector = np.ones(12) * 0.5
    
    # 遍历答案，累加维度得分
    dimension_scores = {i: [] for i in range(12)}
    trait_names = ["openness", "conscientiousness", "extraversion", "agreeableness", 
                   "neuroticism", "leadership", "risk_taking", "rationality", 
                   "discipline", "empathy", "ambition", "resilience"]
    
    for ans in answers:
        # 找到对应题目（questions_data是列表，用索引）
        if ans.question_id > len(questions_data):
            continue
        question = questions_data[ans.question_id - 1]
        
        # 找到对应选项
        if ans.option_index >= len(question["options"]):
            continue
        option = question["options"][ans.option_index]
        
        # 累加维度得分
        trait = question.get("trait", "")
        if trait in trait_names:
            dim_index = trait_names.index(trait)
            dimension_scores[dim_index].append(option["vector"].get(trait, 0.5))
    
    # 计算平均值
    for i in range(12):
        if dimension_scores[i]:
            vector[i] = np.mean(dimension_scores[i])
    
    return vector


def match_euclidean(
    user_vector: np.ndarray,
    figure_vectors: dict[int, np.ndarray],
    top_k: int = 5
) -> list[dict[str, Any]]:
    """
    使用欧氏距离进行匹配（距离越小越相似）
    
    Returns:
        按相似度降序排列的结果列表
    """
    results = []
    
    for fig_id, fig_vec in figure_vectors.items():
        # 计算欧氏距离
        dist = euclidean_distance(user_vector, fig_vec)
        
        # 转换为相似度分数（0-1之间，距离越小分数越高）
        # 使用指数衰减: sim = exp(-dist^2 / 2)
        similarity = np.exp(-(dist ** 2) / 2)
        
        results.append({
            "figure_id": fig_id,
            "distance": dist,
            "similarity": float(similarity)
        })
    
    # 按相似度降序排序
    results.sort(key=lambda x: x["similarity"], reverse=True)
    
    return results[:top_k]
