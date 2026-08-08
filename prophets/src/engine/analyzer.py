"""差距分析模块：逐维度对比、生成差距描述"""

from __future__ import annotations

import numpy as np
from typing import Any


def analyze_gaps(user_vector: np.ndarray, figure_vector: np.ndarray) -> list[dict[str, Any]]:
    """分析用户与人物之间的维度差距
    
    Returns:
        按差距绝对值排序的差距列表，每个元素包含：
        - trait: 维度名称
        - user_value: 用户值
        - figure_value: 人物值
        - gap: 差距值（人物值 - 用户值）
    """
    trait_names = ["openness", "conscientiousness", "extraversion", "agreeableness",
                   "neuroticism", "leadership", "risk_taking", "rationality",
                   "discipline", "empathy", "ambition", "resilience"]
    
    if len(user_vector) != len(trait_names):
        raise ValueError(f"用户向量维度不匹配: 期望{len(trait_names)}, 实际{len(user_vector)}")
    if len(figure_vector) != len(trait_names):
        raise ValueError(f"人物向量维度不匹配: 期望{len(trait_names)}, 实际{len(figure_vector)}")
    
    gaps = []
    for i, dim in enumerate(trait_names):
        diff = float(figure_vector[i] - user_vector[i])
        gaps.append({
            "trait": dim,
            "user_value": float(user_vector[i]),
            "figure_value": float(figure_vector[i]),
            "gap": diff
        })
    
    # 按差距绝对值排序
    gaps.sort(key=lambda x: abs(x["gap"]), reverse=True)
    
    return gaps[:5]  # 返回差距最大的5个维度
