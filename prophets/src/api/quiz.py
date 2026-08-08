"""
测评题目接口
GET /api/quiz - 获取题目列表（支持语言选择）
"""

import json
from typing import Any
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from pathlib import Path

router = APIRouter()

# 支持的語言列表
SUPPORTED_LANGUAGES = ["zh", "en", "es", "ja", "de", "ru", "fr"]

# 缓存
_questions_data: list[dict[str, Any]] | None = None


def _load_questions() -> list[dict[str, Any]]:
    """加载题目数据"""
    global _questions_data
    if _questions_data is not None:
        return _questions_data

    # 使用正确的路径
    data_path = Path(__file__).parent.parent / "data" / "questions.json"

    if not data_path.exists():
        # 尝试备选路径
        data_path = Path(__file__).parent.parent.parent / "prophets" / "src" / "data" / "questions.json"

    if not data_path.exists():
        raise HTTPException(status_code=503, detail="题目数据文件不存在")

    try:
        with open(data_path, "r", encoding="utf-8") as f:
            _questions_data = json.load(f)
        return _questions_data
    except Exception as e:
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

    - language: 语言代码 (zh/en/es/ja/de/ru/fr)，默认中文
    - 返回指定语言的题目和选项
    """
    try:
        questions = _load_questions()

        sanitized_questions = []
        for q in questions:
            # 获取当前语言的文本和选项
            translations = q.get("translations", {})
            lang_options = translations.get(language, translations.get("zh", []))

            # 获取题目文本（使用第一个选项作为问题提示）
            question_text = q.get("text", "")

            sanitized_questions.append(QuizQuestion(
                id=q.get("id"),
                trait=q.get("trait", ""),
                text=question_text,
                options=lang_options[:4]  # 最多4个选项
            ))

        return QuizResponse(
            questions=sanitized_questions,
            total=len(sanitized_questions),
            language=language
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取题目失败: {e}")


@router.get("/quiz/{question_id}", summary="获取单道题目")
async def get_question(question_id: int, language: str = Query("zh", pattern="^(zh|en|es|ja|de|ru|fr)$")):
    """
    获取单道题目详情

    - question_id: 题目ID
    - language: 语言代码
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

        # 获取当前语言的选项
        translations = question.get("translations", {})
        lang_options = translations.get(language, translations.get("zh", []))

        sanitized = {
            "id": question.get("id"),
            "trait": question.get("trait", ""),
            "text": question.get("text", ""),
            "options": lang_options[:4]
        }

        return sanitized

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取题目失败: {e}")
