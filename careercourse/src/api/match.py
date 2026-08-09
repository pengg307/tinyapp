from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import json
from pathlib import Path

from src.engine.matcher import match_user, generate_suggestion

router = APIRouter()

class Answer(BaseModel):
    question_id: int
    option_index: int

class MatchRequest(BaseModel):
    answers: list[Answer]
    top_n: int = 10

@router.post("/match")
async def match(request: MatchRequest):
    answers = [a.dict() for a in request.answers]
    matches = match_user(answers, request.top_n)
    
    result = {
        "user_vector": matches[0]["user_vector"] if matches else {},
        "matches": []
    }
    
    for match in matches:
        suggestion = generate_suggestion(match)
        result["matches"].append({
            "figure": match["figure"],
            "similarity": match["similarity"],
            "suggestion": suggestion
        })
    
    return result
