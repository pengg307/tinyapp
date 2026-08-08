"""匹配引擎：用户向量 → 相似度排序 → TOP-5"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .vector import cosine_similarity


@dataclass
class MatchResult:
    """匹配结果"""
    name: str
    similarity: float
    score: float  # 保留原始分数用于排序


def match(
    user_vector: np.ndarray,
    character_vectors: dict[str, np.ndarray],
    top_k: int = 5,
) -> list[MatchResult]:
    """
    对用户向量与历史人物库进行相似度排序，返回 top_k 个匹配结果。

    Parameters
    ----------
    user_vector : np.ndarray
        用户特征向量
    character_vectors : dict[str, np.ndarray]
        历史人物向量字典，key 为人名
    top_k : int
        返回匹配数，默认 5

    Returns
    -------
    list[MatchResult]
        按余弦相似度降序排列的匹配结果
    """
    if top_k < 1:
        raise ValueError("top_k 必须 >= 1")

    results = []
    for name, char_vec in character_vectors.items():
        sim = cosine_similarity(user_vector, char_vec)
        results.append(MatchResult(name=name, similarity=sim, score=sim))

    results.sort(key=lambda x: x.similarity, reverse=True)
    return results[:top_k]
