"""
测评题目接口
GET /api/quiz - 获取题目列表（支持语言选择）
"""

import json
import os
import logging
from typing import Any
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from pathlib import Path

logger = logging.getLogger(__name__)
router = APIRouter()

# 支持的语言列表
SUPPORTED_LANGUAGES = ["zh", "en", "es", "ja", "de", "ru", "fr"]

# 缓存
_questions_data: list[dict[str, Any]] | None = None


def _find_data_file() -> Path:
    """Find the questions.json file with multiple fallback paths"""
    current_file = Path(__file__).resolve()
    
    # Possible locations based on where the file might be in different environments
    possible_paths = [
        # Direct relative paths
        Path("prophets/src/data/questions.json"),
        Path("src/data/questions.json"),
        Path("data/questions.json"),
        # Based on __file__ location
        current_file.parent.parent / "data" / "questions.json",
        current_file.parent.parent.parent / "prophets" / "src" / "data" / "questions.json",
        current_file.parent / "data" / "questions.json",
        # Search up multiple levels
        current_file.parent.parent.parent.parent / "prophets" / "src" / "data" / "questions.json",
        current_file.parent.parent.parent.parent / "src" / "data" / "questions.json",
    ]
    
    for path in possible_paths:
        resolved = path.resolve()
        if resolved.exists():
            logger.info(f"Found questions.json at {resolved}")
            return resolved
    
    # Last resort: try to find it in common Vercel locations
    vercel_paths = [
        Path("/var/task/prophets/src/data/questions.json"),
        Path("/home/vercel/project/prophets/src/data/questions.json"),
        Path("/opt/prophets/src/data/questions.json"),
    ]
    
    for path in vercel_paths:
        if path.exists():
            logger.info(f"Found questions.json at Vercel path {path}")
            return path
    
    logger.error("questions.json not found in any expected location")
    raise HTTPException(status_code=503, detail="题目数据文件不存在")


def _load_questions() -> list[dict[str, Any]]:
    """加载题目数据"""
    global _questions_data
    if _questions_data is not None:
        return _questions_data

    try:
        data_path = _find_data_file()
        logger.info(f"Loading questions from {data_path}")
        
        with open(data_path, "r", encoding="utf-8") as f:
            _questions_data = json.load(f)
        
        logger.info(f"Loaded {len(_questions_data)} questions")
        return _questions_data
    except Exception as e:
        logger.error(f"Error loading questions: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"加载题目数据失败: {e}")


class QuizQuestion(BaseModel):
    id: int
    trait: str
    text: str
    options: list[str]


class QuizResponse(BaseModel):
    questions: list[QuizQuestion]
    total: int
    language: str


@router.get("/quiz", response_model=QuizResponse, summary="获取测评题目")
async def get_quiz(language: str = Query("zh", pattern="^(zh|en|es|ja|de|ru|fr)$")):
    """
    获取测评题目列表
    """
    try:
        logger.info(f"Getting quiz questions, language={language}")
        questions = _load_questions()

        sanitized_questions = []
        for q in questions:
            translations = q.get("translations", {})
            lang_data = translations.get(language, translations.get("zh", {}))
            
            question_text = lang_data.get("text", q.get("text", ""))
            lang_options = lang_data.get("options", [])

            sanitized_questions.append(QuizQuestion(
                id=q.get("id"),
                trait=q.get("trait", ""),
                text=question_text,
                options=lang_options[:4]
            ))

        logger.info(f"Returning {len(sanitized_questions)} questions")
        return QuizResponse(
            questions=sanitized_questions,
            total=len(sanitized_questions),
            language=language
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in get_quiz: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"获取题目失败: {e}")


@router.get("/quiz/{question_id}", summary="获取单道题目")
async def get_question(question_id: int, language: str = Query("zh", pattern="^(zh|en|es|ja|de|ru|fr)$")):
    """
    获取单道题目详情
    """
    try:
        questions = _load_questions()

        question = None
        for q in questions:
            if q.get("id") == question_id:
                question = q
                break

        if question is None:
            raise HTTPException(status_code=404, detail=f"题目 {question_id} 不存在")

        translations = question.get("translations", {})
        lang_data = translations.get(language, translations.get("zh", {}))
        question_text = lang_data.get("text", question.get("text", ""))
        lang_options = lang_data.get("options", [])

        sanitized = {
            "id": question.get("id"),
            "trait": question.get("trait", ""),
            "text": question_text,
            "options": lang_options[:4]
        }

        return sanitized

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in get_question: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"获取题目失败: {e}")
