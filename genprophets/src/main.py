"""
GenProphets - 职业性格测试与历史人物匹配
FastAPI 应用入口
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path

STATIC_DIR = Path(__file__).parent.parent / "static"

app = FastAPI(title="GenProphets")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

from src.api import quiz, match, figures
app.include_router(quiz.router, prefix="/api")
app.include_router(match.router, prefix="/api")
app.include_router(figures.router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/", response_class=HTMLResponse)
async def root():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return index_file.read_text(encoding="utf-8")
    return HTMLResponse("<h1>Error: index.html not found</h1>")
