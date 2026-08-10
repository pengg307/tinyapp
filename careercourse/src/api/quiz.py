"""Quiz questions API."""
from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

DATA_DIR = Path(__file__).parent.parent.parent / "src" / "data"

@router.get("/questions")
async def get_questions():
    with open(DATA_DIR / "questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    # Return just the array, not wrapped in object
    if isinstance(data, list):
        return data
    return data.get("questions", [])
