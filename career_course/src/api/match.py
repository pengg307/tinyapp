"""
CareerProphet - 匹配接口
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from src.engine.matcher import match_user

router = APIRouter()

class AnswerItem(BaseModel):
    question_id: int
    option_index: int

class MatchRequest(BaseModel):
    answers: List[AnswerItem]
    top_n: Optional[int] = 10

@router.post("/match")
async def post_match(req: MatchRequest):
    answers = [{"question_id": a.question_id, "option_index": a.option_index} for a in req.answers]
    result = match_user(answers, top_n=req.top_n or 10)
    return result
