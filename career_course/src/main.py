"""
统一入口：CareerProphet - 职业性格测试与历史人物匹配平台
融合 prophets 的支付系统和 career_course 的完整数据
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pathlib import Path

STATIC_DIR = Path(__file__).parent.parent / "static"

app = FastAPI(title="CareerProphet", description="职业性格测试与历史人物匹配平台")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# API 路由
from src.api import quiz, match, figures
app.include_router(quiz.router, prefix="/api")
app.include_router(match.router, prefix="/api")
app.include_router(figures.router, prefix="/api")

# 可选：支付路由（从 prophets 迁移）
# from src.api import payment, qr
# app.include_router(payment.router, prefix="/api")
# app.include_router(qr.router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "CareerProphet"}

@app.get("/", response_class=HTMLResponse)
async def root():
    """主入口：职业性格测试"""
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return HTMLResponse("<h1>CareerProphet</h1><p>职业性格测试与历史人物匹配平台</p>")

@app.get("/prophets", response_class=HTMLResponse)
async def prophets_page():
    """历史人物匹配详情页面（可选）"""
    prophets_file = STATIC_DIR / "prophets" / "index.html"
    if prophets_file.exists():
        return FileResponse(prophets_file)
    return HTMLResponse("<h1>Prophets</h1><p>与历史人物相遇</p>")
