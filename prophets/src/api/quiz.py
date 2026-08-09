"""
测评题目接口
GET /api/quiz - 获取题目列表（支持语言选择）
"""

import json
import os
from typing import Any
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from pathlib import Path

router = APIRouter()

# 支持的语言列表
SUPPORTED_LANGUAGES = ["zh", "en", "es", "ja", "de", "ru", "fr"]

# 缓存
_questions_data: list[dict[str, Any]] | None = None


def _find_data_file() -> Path:
    """Find the questions.json file with multiple fallback paths"""
    # Try different possible locations
    possible_paths = [
        # Current working directory based
        Path("src/data/questions.json"),
        Path("prophets/src/data/questions.json"),
        Path("data/questions.json"),
        # Based on __file__
        Path(__file__).parent.parent / "data" / "questions.json",
        Path(__file__).parent.parent.parent / "prophets" / "src" / "data" / "questions.json",
        Path(__file__).parent / "data" / "questions.json",
        # Absolute paths for debugging
        Path("/home/vercel/project/src/data/questions.json"),
        Path("/var/task/src/data/questions.json"),
    ]
    
    for path in possible_paths:
        resolved = path.resolve()
        if resolved.exists():
            print(f"DEBUG: Found questions.json at {resolved}")
            return resolved
    
    # Last resort: search from project root
    project_root = Path(__file__).resolve().parent.parent.parent.parent
    fallback = project_root / "prophets" / "src" / "data" / "questions.json"
    if fallback.exists():
        print(f"DEBUG: Found questions.json at fallback path {fallback}")
        return fallback
    
    raise HTTPException(status_code=503, detail="题目数据文件不存在")


def _load_questions() -> list[dict[str, Any]]:
    """加载题目数据"""
    global _questions_data
    if _questions_data is not None:
        return _questions_data

    try:
        data_path = _find_data_file()
        print(f"DEBUG: Loading questions from {data_path}")
        
        with open(data_path, "r", encoding="utf-8") as f:
            _questions_data = json.load(f)
        
        print(f"DEBUG: Loaded {len(_questions_data)} questions")
        return _questions_data
    except Exception as e:
        print(f"DEBUG: Error loading questions: {e}")
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

        return QuizResponse(
            questions=sanitized_questions,
            total=len(sanitized_questions),
            language=language
        )

    except HTTPException:
        raise
    except Exception as e:
        print(f"DEBUG: Error in get_quiz: {e}")
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
        print(f"DEBUG: Error in get_question: {e}")
        raise HTTPException(status_code=500, detail=f"获取题目失败: {e}")
