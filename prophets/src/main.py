"""Prophets - 历史人物性格匹配引擎"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from src.api.quiz import router as quiz_router
from src.api.match import router as match_router
from src.api.payment import router as payment_router
from src.api.qr import router as qr_router

app = FastAPI(
    title="Prophets API",
    description="历史人物性格匹配引擎",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件服务
static_path = Path(__file__).parent.parent / "static"

# 路由挂载
app.include_router(quiz_router, prefix="/api", tags=["quiz"])
app.include_router(match_router, prefix="/api", tags=["match"])
app.include_router(payment_router, tags=["payment"])
app.include_router(qr_router, tags=["qr"])

@app.get("/api/health")
async def health_check():
    """健康检查"""
    logger.info("Health check requested")
    return {"status": "ok", "version": "0.1.0"}

@app.get("/")
async def root():
    """根路径返回HTML前端"""
    logger.info("Serving index.html")
    from fastapi.responses import HTMLResponse
    html_path = static_path / "index.html"
    if not html_path.exists():
        logger.error(f"HTML file not found: {html_path}")
        raise HTTPException(status_code=404, detail="前端文件不存在")
    return HTMLResponse(content=open(html_path, encoding="utf-8").read())

@app.get("/chart.min.js")
async def serve_chart_js():
    """提供本地Chart.js文件"""
    from fastapi.responses import FileResponse
    chart_path = static_path / "chart.min.js"
    if chart_path.exists():
        return FileResponse(chart_path, media_type="application/javascript")
    return {"error": "Chart.js file not found"}

@app.get("/favicon.ico")
async def favicon():
    """返回空的 favicon 避免 404 错误"""
    from fastapi.responses import Response
    return Response(content="", media_type="image/x-icon")
