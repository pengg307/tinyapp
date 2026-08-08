# Prophets 匹配引擎

Prophets 项目的核心引擎模块，位于 `src/engine/`。

## 模块结构

```
src/engine/
├── __init__.py   # 统一导出
├── vector.py     # 向量计算：余弦相似度、欧氏距离、归一化
├── matcher.py    # 匹配引擎：用户向量 → 相似度排序 → TOP-K
└── analyzer.py   # 差距分析：逐维度对比、生成差距描述
```

## 公共 API

```python
from engine import cosine_similarity, euclidean_distance, normalize, match, analyze
```

### vector.py

| 函数 | 签名 | 说明 |
|------|------|------|
| `cosine_similarity` | `(a: np.ndarray, b: np.ndarray) -> float` | 范围 [-1, 1]，1 表示完全一致 |
| `euclidean_distance` | `(a: np.ndarray, b: np.ndarray) -> float` | 欧氏距离 |
| `normalize` | `(v: np.ndarray) -> np.ndarray` | L2 归一化，零向量返回零向量 |

### matcher.py

| 函数 | 签名 | 说明 |
|------|------|------|
| `match` | `(user_vector, character_vectors: dict[str, np.ndarray], top_k=5) -> list[MatchResult]` | 相似度排序，返回 TOP-K |

`MatchResult` 是 dataclass：`name: str`, `similarity: float`, `score: float`

### analyzer.py

| 函数 | 签名 | 说明 |
|------|------|------|
| `analyze` | `(user_vector, character_vector, dimension_names=None) -> dict` | 逐维度差距分析 |

返回结构：
```json
{
  "overall_similarity": 0.9894,
  "dimensions": [
    {"name": "开放性", "user_value": 0.7, "character_value": 0.8, "diff": -0.1, "gap": "略微低于"}
  ]
}
```

差距描述阈值：
- `|diff| < 0.2` → "基本相当"
- `0.2 ≤ |diff| ≤ 0.5` → "略微高/低于"
- `|diff| > 0.5` → "显著高/低于"

## 设计原则

1. **纯函数**：不内部加载数据文件，数据由调用方传入
2. **numpy 向量化**：所有计算使用 numpy，避免 Python 循环
3. **单职责**：每个函数只做一件事
4. **类型注解**：完整类型提示，便于 IDE 支持

## 验证

```bash
python -c "
import sys; sys.path.insert(0, 'src')
from engine import cosine_similarity, match, analyze
import numpy as np

# 向量测试
print(cosine_similarity(np.array([1,2,3]), np.array([2,3,4])))

# 匹配测试
chars = {'孔子': np.array([0.8, 0.7, 0.6]), '老子': np.array([0.9, 0.3, 0.7])}
print(match(np.array([0.8, 0.7, 0.6]), chars, top_k=2))

# 分析测试
print(analyze(np.array([0.8, 0.7, 0.6]), chars['孔子'], ['开放性', '尽责性', '外向性']))
"
```
