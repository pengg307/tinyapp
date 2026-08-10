"""Figures API endpoint."""
from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

DATA_DIR = Path(__file__).parent.parent.parent / "src" / "data"

@router.get("/figures")
async def get_figures():
    with open(DATA_DIR / "figures.json", "r", encoding="utf-8") as f:
        figures = json.load(f)
    return {"figures": figures, "total": len(figures)}
