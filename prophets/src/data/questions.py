"""题目数据加载"""
import json
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent


def load_questions() -> list[dict[str, Any]]:
    """加载题目数据（返回列表）"""
    with open(DATA_DIR / "questions.json", encoding="utf-8") as f:
        return json.load(f)


def load_traits() -> dict[str, Any]:
    """加载维度定义"""
    with open(DATA_DIR / "traits.json", encoding="utf-8") as f:
        return json.load(f)
