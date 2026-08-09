"""
Prophets - 历史人物性格匹配引擎
FastAPI 应用入口
"""
import logging
import sys
from pathlib import Path

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 动态调整 Python 路径以支持多种部署方式：
# 1. Vercel Root Directory = prophets → PYTHONPATH=. → src 在当前目录
# 2. Vercel Root Directory = 空 → PYTHONPATH=prophets → src 在父目录
_script = Path(__file__).resolve()
# 如果 prophets/src/main.py，添加 prophets/src 到路径
if _script.parent.name == "src" and _script.parent.parent.name == "prophets":
    sys.path.insert(0, str(_script.parent))
# 如果 src/main.py，添加当前目录到路径
elif _script.parent.name == "src" and _script.parent.parent.name != "prophets":
    sys.path.insert(0, str(_script.parent.parent))

# 导入路由
from src.api.quiz import router as quiz_router
from src.api.match import router as match_router
from src.api.payment import router as payment_router
from src.api.qr import router as qr_router
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response

# 创建 FastAPI 应用
app = FastAPI(
    title="Prophets API",
    description="历史人物性格匹配引擎",
    version="0.1.0",
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件路径
static_path = Path(__file__).parent.parent / "static"


@app.get("/api/health")
async def health_check():
    """健康检查端点"""
    logger.info("Health check called")
    return {"status": "ok"}


@app.get("/")
async def root():
    """返回前端页面"""
    html_path = static_path / "index.html"
    if not html_path.exists():
        logger.error(f"HTML file not found: {html_path}")
        raise HTTPException(status_code=404, detail="Frontend not found")
    
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()


@app.get("/chart.min.js")
async def chart_js():
    """提供 Chart.js 文件"""
    chart_path = static_path / "chart.min.js"
    if chart_path.exists():
        return FileResponse(chart_path, media_type="application/javascript")
    return HTTPException(status_code=404, detail="Chart.js not found")


@app.get("/favicon.ico")
async def favicon():
    """返回空的 favicon"""
    return Response(content="", media_type="image/x-icon")


# 注册路由
app.include_router(quiz_router, prefix="/api")
app.include_router(match_router, prefix="/api")
app.include_router(payment_router, prefix="/api")
app.include_router(qr_router, prefix="/api")
