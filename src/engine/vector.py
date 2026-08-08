"""向量计算模块：余弦相似度、欧氏距离、归一化"""

from __future__ import annotations

import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """计算两个向量的余弦相似度（范围 [-1, 1]，1 表示完全一致）"""
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(a, b) / (norm_a * norm_b))


def euclidean_distance(a: np.ndarray, b: np.ndarray) -> float:
    """计算两个向量的欧氏距离"""
    return float(np.linalg.norm(a - b))


def normalize(v: np.ndarray) -> np.ndarray:
    """将向量归一化为单位向量"""
    norm = np.linalg.norm(v)
    if norm == 0:
        return np.zeros_like(v, dtype=float)
    return v / norm
