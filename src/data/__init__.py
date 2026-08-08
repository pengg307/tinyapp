"""数据加载模块"""
import json
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent


def load_figures() -> list[dict[str, Any]]:
    """加载历史人物数据"""
    with open(DATA_DIR / "figures.json", encoding="utf-8") as f:
        return json.load(f)


def load_questions() -> dict[str, Any]:
    """加载题目数据"""
    with open(DATA_DIR / "questions.json", encoding="utf-8") as f:
        return json.load(f)


def load_traits() -> dict[str, Any]:
    """加载维度定义"""
    with open(DATA_DIR / "traits.json", encoding="utf-8") as f:
        return json.load(f)
