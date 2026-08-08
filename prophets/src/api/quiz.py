"""
测评题目接口
GET /api/quiz - 获取题目列表（不含选项向量）
"""

from typing import Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# 路由定义
router = APIRouter()

# 数据加载缓存
_questions_data: list[dict[str, Any]] | None = None


def _load_questions() -> list[dict[str, Any]]:
    """加载题目数据"""
    global _questions_data
    if _questions_data is not None:
        return _questions_data
    
    import json
    from pathlib import Path
    
    data_path = Path(__file__).parent.parent.parent / "src" / "data" / "questions.json"
    
    if not data_path.exists():
        raise HTTPException(status_code=503, detail="题目数据文件不存在")
    
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            _questions_data = json.load(f)
        return _questions_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"加载题目数据失败: {e}")


class QuizResponse(BaseModel):
    """题目响应模型"""
    questions: list[dict[str, Any]]
    total: int


@router.get("/quiz", response_model=QuizResponse, summary="获取测评题目")
async def get_quiz():
    """
    获取测评题目列表
    
    - 返回所有题目基本信息（ID、题干）
    - 不含选项向量数据（避免泄露匹配逻辑）
    - 选项文本保留，供用户选择
    """
    try:
        questions = _load_questions()
        
        # 清理敏感数据：移除选项向量
        sanitized_questions = []
        for q in questions:
            q_clean = {
                "id": q.get("id"),
                "text": q.get("text"),
                "options": []
            }
            
            # 保留选项文本，移除向量
            for opt in q.get("options", []):
                q_clean["options"].append({
                    "text": opt.get("text"),
                    "index": opt.get("index", 0)
                })
            
            sanitized_questions.append(q_clean)
        
        return QuizResponse(
            questions=sanitized_questions,
            total=len(sanitized_questions)
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取题目失败: {e}")


@router.get("/quiz/{question_id}", summary="获取单道题目")
async def get_question(question_id: int):
    """
    获取单道题目详情
    
    - 返回题目和所有选项
    - 不含选项向量
    """
    try:
        questions = _load_questions()
        
        # 查找题目
        question = None
        for q in questions:
            if q.get("id") == question_id:
                question = q
                break
        
        if question is None:
            raise HTTPException(status_code=404, detail=f"题目 {question_id} 不存在")
        
        # 清理数据
        sanitized = {
            "id": question.get("id"),
            "text": question.get("text"),
            "options": [
                {
                    "text": opt.get("text"),
                    "index": opt.get("index", 0)
                }
                for opt in question.get("options", [])
            ]
        }
        
        return sanitized
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取题目失败: {e}")
