"""FastAPI application for CareerCourse."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

# Use the correct path based on project location
STATIC_DIR = Path(r"E:\aiprojects\tinyapp\careercourse\static")

app = FastAPI(title="CareerCourse")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

# Include routers
from src.api import quiz, match
app.include_router(quiz.router, prefix="/api")
app.include_router(match.router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main HTML page."""
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        with open(index_file, "r", encoding="utf-8") as f:
            return f.read()
    return HTMLResponse("<h1>Error: index.html not found</h1>")

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy"}
