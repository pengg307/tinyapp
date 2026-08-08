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
