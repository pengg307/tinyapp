"""
CareerProphet - 匹配接口（多语言支持）
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
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
    language = req.language or "zh"
    
    # 调用匹配引擎
    result = match_user(answers, top_n=req.top_n or 10, language=language)
    
    # 为每个匹配生成多语言建议
    for match in result.get("matches", []):
        fig = match.get("figure", {})
        suggestion_data = match.get("suggestion", {})
        gaps = suggestion_data.get("gaps", [])
        
        # 获取多语言名字
        names = fig.get("names", {})
        figure_name = names.get(language, names.get("zh", fig.get("name_cn", "")))
        
        # 生成多语言建议
        suggestions = generate_suggestions(gaps, fig.get("type", ""), language, figure_name)
        
        match["suggestion"]["figure_name"] = figure_name
        match["suggestion"]["overall"] = suggestions["overall"]
        match["suggestion"]["suggestions"] = suggestions["suggestions"]
    
    return result
