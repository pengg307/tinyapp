"""
CareerProphet - 历史人物接口
"""
from fastapi import APIRouter
from src.engine.matcher import load_figures

router = APIRouter()

@router.get("/figures")
async def get_figures():
    figs = load_figures()
    return {"figures": figs, "total": len(figs)}
