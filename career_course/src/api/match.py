"""
CareerProphet - 匹配接口（多语言支持）
"""
from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Optional, Any
from src.engine.matcher import match_user
from src.api.suggestions import generate_suggestions

router = APIRouter()

class AnswerItem(BaseModel):
    question_id: int
    option_index: int

class MatchRequest(BaseModel):
    answers: List[AnswerItem]
    top_n: Optional[int] = 10
    language: Optional[str] = "zh"

@router.post("/match")
async def post_match(req: MatchRequest):
    """
    匹配接口（多语言支持）
    
    Args:
        req: 匹配请求
        language: 语言代码 (zh/en/es/ja/de/ru/fr)
    """
    answers = [{"question_id": a.question_id, "option_index": a.option_index} for a in req.answers]
    
    # 调用匹配引擎
    result = match_user(answers, top_n=req.top_n or 10)
    
    # 获取语言
    language = req.language or "zh"
    
    # 更新匹配结果中的多语言名称
    for match in result.get("matches", []):
        fig = match.get("suggestion", {})
        figure_name = fig.get("figure_name", "")
        
        # 获取多语言名字
        names = fig.get("names", {})
        multilingual_name = names.get(language, names.get("zh", figure_name))
        
        # 生成多语言建议
        gaps = fig.get("gaps", [])
        suggestion = generate_suggestions(gaps, fig.get("type", ""), language, multilingual_name)
        
        match["suggestion"]["figure_name"] = multilingual_name
        match["suggestion"]["suggestion"] = suggestion
        match["suggestion"]["name"] = multilingual_name
    
    return result
