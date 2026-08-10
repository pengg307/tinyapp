"""
GenProphets - 题目接口
"""
from fastapi import APIRouter
from src.engine.matcher import load_questions

router = APIRouter()

@router.get("/questions")
async def get_questions():
    qs = load_questions()
    return {"questions": qs, "total": len(qs)}
