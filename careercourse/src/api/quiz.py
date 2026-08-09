from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
import json
from pathlib import Path

router = APIRouter()

# Use the correct path
DATA_DIR = Path(r"E:\aiprojects\tinyapp\careercourse\src\data")

@router.get("/questions")
async def get_questions():
    with open(DATA_DIR / "questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    return {"questions": questions, "total": len(questions)}

@router.get("/figures")
async def get_figures():
    with open(DATA_DIR / "figures.json", "r", encoding="utf-8") as f:
        figures = json.load(f)
    return {"figures": figures, "total": len(figures)}

@router.post("/start")
async def start_quiz():
    return {"status": "started", "message": "Begin the career assessment"}
