"""
Quiz API - 测评题目接口
"""
import json
import logging
from typing import Any
from pathlib import Path
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

logger = logging.getLogger(__name__)
router = APIRouter()

# 数据缓存
_questions_data: list[dict[str, Any]] | None = None


def _get_data_path() -> Path:
    """获取 questions.json 路径"""
    current = Path(__file__).resolve()
    
    # 尝试多个可能的路径
    paths = [
        current.parent.parent / "data" / "questions.json",
        current.parent.parent.parent / "prophets" / "src" / "data" / "questions.json",
        Path("prophets/src/data/questions.json"),
    ]
    
    for p in paths:
        resolved = p.resolve()
        if resolved.exists():
            logger.info(f"Found data at: {resolved}")
            return resolved
    
    raise HTTPException(status_code=503, detail="Questions data not found")


def _load_questions() -> list[dict[str, Any]]:
    """加载题目数据"""
    global _questions_data
    if _questions_data is not None:
        return _questions_data
    
    try:
        data_path = _get_data_path()
        with open(data_path, "r", encoding="utf-8") as f:
            _questions_data = json.load(f)
        logger.info(f"Loaded {len(_questions_data)} questions")
        return _questions_data
    except Exception as e:
        logger.error(f"Error loading questions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


class QuizQuestion(BaseModel):
    id: int
    trait: str
    text: str
    options: list[str]


@router.get("/quiz")
async def get_quiz(language: str = Query(default="zh")):
    """获取测评题目"""
    try:
        questions = _load_questions()
        
        result = []
        for q in questions:
            translations = q.get("translations", {})
            lang_data = translations.get(language, translations.get("zh", {}))
            
            result.append(QuizQuestion(
                id=q["id"],
                trait=q.get("trait", ""),
                text=lang_data.get("text", q.get("text", "")),
                options=lang_data.get("options", [])
            ))
        
        return {"questions": result, "total": len(result), "language": language}
    except Exception as e:
        logger.error(f"Error in get_quiz: {e}")
        raise HTTPException(status_code=500, detail=str(e))
