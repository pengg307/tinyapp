"""
CareerProphet - 题目接口（多语言支持）
"""
from fastapi import APIRouter
from src.engine.matcher import load_questions

router = APIRouter()

@router.get("/questions")
async def get_questions(language: str = "zh"):
    """
    获取题目列表，根据语言参数返回对应翻译
    language: zh (中文), en (英文), es (西班牙文), ja (日文)
    """
    qs = load_questions()
    
    # 根据语言选择题目文本
    lang_key = f"question_{language}"
    text_key = f"text_{language}"
    
    for q in qs:
        # 替换题目文本
        if lang_key in q and q[lang_key]:
            q["question"] = q[lang_key]
        # 替换选项文本
        for opt in q.get("options", []):
            if text_key in opt and opt[text_key]:
                opt["text"] = opt[text_key]
    
    return {"questions": qs, "total": len(qs)}
