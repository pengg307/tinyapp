# Prophets 历史人物性格匹配 Web App — 完整项目规范

## 1. 项目概述

**名称**: Prophets（先知）
**一句话描述**: 60道情境选择题 → 12维性格向量 → 匹配96位中外历史人物
**技术栈**: Python FastAPI + 单页HTML（Chart.js本地）
**部署**: Vercel（Python函数 + 静态文件）
**语言支持**: 中文/英文/西班牙文/日文/德文/俄文/法文（7语言）

---

## 2. 项目结构

```
prophets/
├── src/
│   ├── __init__.py                    # 空包
│   ├── main.py                        # FastAPI入口
│   ├── api/
│   │   ├── __init__.py                # 空包
│   │   ├── quiz.py                    # 题目API（GET /api/quiz）
│   │   ├── match.py                   # 匹配API（POST /api/match）
│   │   ├── payment.py                 # 支付API（支付状态/二维码）
│   │   ├── qr.py                      # 二维码生成API
│   │   └── suggestions.py             # 建议生成模块
│   ├── data/
│   │   ├── __init__.py                # 数据加载
│   │   ├── figures.py                 # 人物数据加载
│   │   ├── questions.py               # 题目数据加载
│   │   ├── figures.json               # 96位历史人物
│   │   ├── questions.json             # 60道题目
│   │   └── traits.json                # 12维度定义
│   └── engine/
│       ├── __init__.py                # 空包
│       ├── vector.py                  # 向量计算（余弦/欧氏）
│       ├── matcher.py                 # 匹配引擎
│       └── analyzer.py                # 差距分析
├── static/
│   ├── index.html                     # 单页应用（1786行）
│   └── chart.min.js                   # Chart.js本地文件
├── requirements.txt
└── vercel.json                        # Vercel部署配置
```

---

## 3. 数据模型

### 3.1 12维性格维度（traits.json）

```json
{
  "dimensions": [
    {
      "id": "openness",
      "name": "Openness",
      "name_cn": "开放性",
      "range_min": 0.0,
      "range_max": 1.0,
      "description": "...",
      "description_cn": "..."
    },
    // ... 共12个维度
  ],
  "dimension_count": 12
}
```

**12维度列表**（固定顺序，用于向量构建）：
1. `openness` — 开放性
2. `conscientiousness` — 尽责性
3. `extraversion` — 外向性
4. `agreeableness` — 宜人性
5. `neuroticism` — 情绪稳定性
6. `leadership` — 领导力
7. `risk_taking` — 风险偏好
8. `rationality` — 理性度
9. `discipline` — 自律性
10. `empathy` — 共情力
11. `ambition` — 野心
12. `resilience` — 韧性

### 3.2 历史人物（figures.json）— 96位

**数量**: 96位中外历史人物
**分类**:
- 按类型：帝王(12)、军事家(12)、政治家(12)、思想家(12)、科学家(12)、艺术家(12)、哲学家(12)、宗教家(12)
- 按时代：古代(24)、中世纪(24)、近代(24)、现代(24)

**数据结构**:
```json
{
  "id": 1,
  "name": "秦始皇",
  "era": "古代",
  "type": "帝王",
  "bio": "帝王，秦始皇的主要事迹与成就",
  "vector": {
    "openness": 0.219889628523367,
    "conscientiousness": 1.0,
    "extraversion": 0.9056785460347372,
    "agreeableness": 0.17367803620728878,
    "neuroticism": 0.24680559213273093,
    "leadership": 0.9555994520336203,
    "risk_taking": 0.8616167224336398,
    "rationality": 0.7878822749859844,
    "discipline": 0.9601115011743209,
    "empathy": 0.08329161244736728,
    "ambition": 0.9420584494295803,
    "resilience": 0.9751855763459191
  },
  "names": {
    "zh": "秦始皇",
    "en": "Qin Shi Huang",
    "es": "Qin Shi Huang",
    "ja": "秦始皇",
    "de": "Qin Shi Huang",
    "ru": "Цинь Шихуанди",
    "fr": "Qin Shi Huang"
  }
}
```

**注意**: 所有96位人物必须有完整的7语言名字（`names`字段），否则前端无法正确显示。

### 3.3 题目（questions.json）— 60道

**数量**: 60道情境选择题
**分布**: 12维度 × 5题 = 60题
**数据结构**:
```json
{
  "id": 1,
  "trait": "openness",
  "trait_cn": "开放性",
  "text": "面对全新的领域，你的态度是？",
  "options": ["充满好奇，积极尝试", "适度接受，但保持谨慎", "更倾向于熟悉的事物", "坚持传统，不喜变化"],
  "translations": {
    "zh": {
      "text": "面对全新的领域，你的态度是？",
      "options": ["充满好奇，积极尝试", "适度接受，但保持谨慎", "更倾向于熟悉的事物", "坚持传统，不喜变化"]
    },
    "en": { ... },
    "es": { ... },
    "ja": { ... },
    "de": { ... },
    "ru": { ... },
    "fr": { ... }
  }
}
```

**注意**: 所有60题必须有完整的7语言翻译（`translations`字段），否则切换语言后题目消失。

---

## 4. 算法核心

### 4.1 用户向量计算

**输入**: 用户答案（60题，每题1-4选项）
**选项映射**:
- option_index 0 → 0.2（低分）
- option_index 1 → 0.5（中低）
- option_index 2 → 0.7（中高）
- option_index 3 → 1.0（高分）

**计算过程**:
```python
# 按trait分组题目
trait_questions = {trait: [q1, q2, ...] for trait, q in questions}

# 计算每个维度的平均分
user_values = {}
for trait, questions in trait_questions.items():
    scores = [option_scores[ans.option_index] for ans in answers if ans.question_id == q.id]
    user_values[trait] = sum(scores) / len(scores)

# 构建12维向量（固定顺序）
vector = np.array([user_values[t] for t in trait_order])
```

### 4.2 匹配算法

**相似度公式**: `similarity = exp(-(distance²) / 2)`

其中 `distance` 是欧氏距离：
```python
distance = sqrt(sum((user[i] - figure[i])² for i in range(12)))
```

**返回TOP 10**匹配结果，按相似度降序排列。

### 4.3 差距分析（analyze_gaps）

```python
def analyze_gaps(user_vector, figure_vector):
    gaps = []
    for i, trait in enumerate(trait_names):
        gap = figure_vector[i] - user_vector[i]
        gaps.append({
            "trait": trait,
            "user_value": user_vector[i],
            "figure_value": figure_vector[i],
            "gap": gap
        })
    # 按差距绝对值排序
    gaps.sort(key=lambda x: abs(x["gap"]), reverse=True)
    return gaps
```

---

## 5. API 接口

### 5.1 GET /api/health
```json
{"status": "ok", "version": "0.1.0"}
```

### 5.2 GET /api/quiz?language=zh
```json
{
  "questions": [...],  // 60题，已处理翻译
  "total": 60,
  "language": "zh"
}
```
每个问题返回 `{id, trait, text, options}`，text/options 根据language参数返回对应翻译。

### 5.3 POST /api/match
**请求体**:
```json
{
  "answers": [
    {"question_id": 1, "option_index": 0},
    {"question_id": 2, "option_index": 1},
    ...
  ],
  "language": "zh"
}
```
**响应**:
```json
{
  "success": true,
  "matches": [
    {
      "figure_id": 1,
      "name": "秦始皇",
      "name_en": "Qin Shi Huang",
      "name_zh": "秦始皇",
      "name_ja": "秦始皇",
      "era": "古代",
      "type": "帝王",
      "similarity": 0.85,
      "gaps": [...],
      "suggestion": {...}
    }
  ],
  "user_vector": {
    "openness": 0.65,
    "conscientiousness": 0.8,
    ...
  },
  "summary": "您与秦始皇最为相似..."
}
```

### 5.4 支付相关API

**GET /api/payment/status/{user_id}**
```json
{"paid": false, "message": "未支付或已过期"}
// 或
{"paid": true, "order_id": "ORD...", "remaining_hours": 23.5}
```

**POST /api/payment**
```json
{"user_id": "anonymous"}
```
返回:
```json
{"success": true, "order_id": "ORD123", "amount": 9.9, "message": "...", "expire_at": "..."}
```

**POST /api/payment/verify**
```json
{"order_id": "ORD123", "user_id": "anonymous"}
```
返回:
```json
{"paid": true, "expire_at": "...", "remaining_hours": 23.5}
```

**POST /api/payment/mock_pay**
```json
{"user_id": "anonymous"}
```
模拟支付成功，将pending订单标记为paid。

**GET /api/payment/qr/{order_id}**
返回二维码图片base64数据。

**GET /api/payment/mock_qr/{user_id}**
创建订单并返回二维码（测试用）。

---

## 6. 前端功能

### 6.1 页面结构（5个区域）

1. **Header**: 语言选择器（7语言下拉）
2. **payment-section**: 付费/广告解锁入口
3. **quiz-section**: 60道题目（进度条+逐题显示）
4. **result-section**: TOP 10匹配结果（雷达图+列表）
5. **ad-banner**: 底部固定广告横幅（可关闭，localStorage记住）

### 6.2 核心JavaScript函数

```javascript
// 语言切换
async function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('language', lang);
    await loadQuiz();
}

// 加载题目
async function loadQuiz() {
    const resp = await fetch(`${API_BASE}/api/quiz?language=${currentLang}`);
    const data = await resp.json();
    questions = data.questions;
    renderQuestions();
}

// 提交答案
async function submitQuiz() {
    const answers = getUserAnswers(); // 收集60题答案
    const resp = await fetch(`${API_BASE}/api/match`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({answers, language: currentLang})
    });
    const data = await resp.json();
    renderResults(data);
}

// 检查支付状态
async function checkPayment() {
    const resp = await fetch(`${API_BASE}/api/payment/status/anonymous`);
    const data = await resp.json();
    if (data.paid) { showResult(); } else { showPaymentSection(); }
}
```

### 6.3 雷达图（Chart.js）

```javascript
new Chart(ctx, {
    type: 'radar',
    data: {
        labels: traitLabels,  // 12维度名称（根据语言）
        datasets: [
            {label: '您', data: userVector},
            {label: '匹配人物', data: figureVector}
        ]
    }
});
```

### 6.4 付费流程

1. 用户答题 → 显示付费弹窗
2. 双按钮：「付费 ¥9.90」或「观看30秒广告」
3. 付费：生成订单 → 显示二维码 → 输入"qwe"模拟支付确认 → 调用mock_pay API → 解锁结果
4. 广告：倒计时30秒 → 解锁结果

---

## 7. Vercel 部署配置

### 7.1 vercel.json

```json
{
  "version": 2,
  "builds": [
    {"src": "prophets/src/main.py", "use": "@vercel/python"},
    {"src": "prophets/static/**", "use": "@vercel/static"}
  ],
  "routes": [
    {"src": "/api/.*", "dest": "prophets/src/main.py"},
    {"src": "/chart.min.js", "dest": "prophets/static/chart.min.js"},
    {"src": "/(.*)", "dest": "prophets/static/$1"}
  ],
  "env": {
    "PYTHONPATH": "prophets"
  }
}
```

### 7.2 requirements.txt

```
fastapi>=0.111.0
uvicorn>=0.30.0
numpy>=1.26.0
qrcode>=7.0.0
```

### 7.3 main.py 关键路径处理

```python
import sys
from pathlib import Path

_script = Path(__file__).resolve()
# Vercel部署时：代码在 /var/task/prophets/src/main.py
# 需要添加 prophets 目录到sys.path，使 from src.api.* 能找到
if _script.parent.name == "src" and _script.parent.parent.name == "prophets":
    sys.path.insert(0, str(_script.parent.parent))  # 添加 prophets/
elif _script.parent.name == "src" and _script.parent.parent.name != "prophets":
    sys.path.insert(0, str(_script.parent))  # 添加 src/

from src.api.quiz import router as quiz_router
from src.api.match import router as match_router
from src.api.payment import router as payment_router
from src.api.qr import router as qr_router
```

---

## 8. 历史人物数据生成指南

### 8.1 人物选择标准

- 中外混合
- 必须是历史人物（去世/活跃≥60年前）
- 按8类平均分配（每类12人）：
  - 帝王、军事家、政治家、思想家
  - 科学家、艺术家、哲学家、宗教家
- 按4个时代平均分配（每个时代24人）：
  - 古代、中世纪、近代、现代

### 8.2 向量生成

为每位历史人物分配12维性格向量（0.0-1.0）：
- 参考人物生平事迹和历史评价
- 示例：秦始皇 — leadership=0.95, empathy=0.08, ambition=0.94
- 可使用LLM辅助生成初始值，再人工微调

### 8.3 名字翻译

为每位人物准备7语言名字：
- zh: 中文名
- en: 英文名（标准译名）
- es: 西班牙语名
- ja: 日文名（汉字或假名）
- de: 德语名
- ru: 俄语名（西里尔字母）
- fr: 法语名

---

## 9. 题目生成指南

### 9.1 题目设计原则

- 每维度5题（共60题）
- 情境选择题，4个选项
- 选项1 → 该维度最低分（0.2）
- 选项4 → 该维度最高分（1.0）
- 选项2/3 → 中间分（0.5/0.7）

### 9.2 题目示例（openness维度）

```json
{
  "id": 1,
  "trait": "openness",
  "text": "面对全新的领域，你的态度是？",
  "options": [
    "充满好奇，积极尝试",  // 0.2
    "适度接受，但保持谨慎",  // 0.5
    "更倾向于熟悉的事物",  // 0.7
    "坚持传统，不喜变化"   // 1.0
  ]
}
```

### 9.3 多语言翻译

- 先写中文题目
- 再翻译为en/es/ja/de/ru/fr
- 确保翻译准确、符合文化语境

---

## 10. 建议内容生成

### 10.1 suggestions.py 结构

```python
SUGGESTIONS_ZH = {
    "openness": {
        "up": ["多尝试新事物，保持好奇心", "阅读不同领域的书籍", ...],
        "down": ["不要害怕改变", "尝试每天做一件新的事", ...]
    },
    # ... 12个维度
}

SUGGESTIONS_EN = { ... }
# ... 其他5种语言
```

### 10.2 建议生成逻辑

```python
def generate_suggestions(gaps, figure_type, language, figure_name):
    # gaps: 按差距排序的列表
    # up: 用户值 < 人物值 → 建议"提升"
    # down: 用户值 > 人物值 → 建议"保持/适度"
    suggestions = []
    for gap in gaps[:3]:  # 取前3个差距最大的维度
        if gap["gap"] > 0:
            suggestions.extend(SUGGESTIONS[language][gap["trait"]]["up"])
        else:
            suggestions.extend(SUGGESTIONS[language][gap["trait"]]["down"])
    return {"figure_name": figure_name, "overall": f"您与{figure_name}的匹配度为...", "suggestions": suggestions}
```

---

## 11. 开发部署清单

### 11.1 必须文件

- [ ] `prophets/src/main.py` — FastAPI入口
- [ ] `prophets/src/api/quiz.py` — 题目API
- [ ] `prophets/src/api/match.py` — 匹配API
- [ ] `prophets/src/api/payment.py` — 支付API
- [ ] `prophets/src/api/qr.py` — 二维码API
- [ ] `prophets/src/api/suggestions.py` — 建议模块
- [ ] `prophets/src/data/figures.json` — 96位人物
- [ ] `prophets/src/data/questions.json` — 60题
- [ ] `prophets/src/data/traits.json` — 12维度定义
- [ ] `prophets/static/index.html` — 前端页面
- [ ] `prophets/static/chart.min.js` — Chart.js
- [ ] `prophets/requirements.txt`
- [ ] `vercel.json`

### 11.2 验证检查

```bash
# 本地测试
curl http://localhost:8000/api/health
curl http://localhost:8000/api/quiz?language=zh  # 返回60题
curl -X POST http://localhost:8000/api/match \
  -H "Content-Type: application/json" \
  -d '{"answers":[{"question_id":1,"option_index":0},...], "language":"zh"}'

# 检查数据完整性
python -c "
import json
q = json.load(open('prophets/src/data/questions.json'))
f = json.load(open('prophets/src/data/figures.json'))
print(f'Questions: {len(q)} (expected 60)')
print(f'Figures: {len(f)} (expected 96)')
print(f'Traits per question: {set(len(qs) for qs in [q for q in q if q[\"trait\"]])}')
# 检查翻译完整性
for item in q:
    assert set(item['translations'].keys()) == {'zh','en','es','ja','de','ru','fr'}
for item in f:
    assert set(item['names'].keys()) == {'zh','en','es','ja','de','ru','fr'}
"
```

---

## 12. 已知坑点

1. **路由重复前缀**: `payment.py`/`qr.py` 的路由定义**不能**有 `/api/` 前缀，因为 `main.py` 的 `include_router` 已加了 `prefix="/api"`。正确写法：`@router.get("/payment/status/{user_id}")` 而非 `@router.get("/api/payment/status/{user_id}")`

2. **Python导入路径**: Vercel部署时，`main.py` 需要动态调整 `sys.path`，否则 `from src.api.*` 会报 `ModuleNotFoundError`

3. **vercel.json路由**: 使用 `/api/.*` 而非 `/api/(.*)`，确保所有API路径都能匹配

4. **数据完整性**: questions.json必须60题、figures.json必须96位，且所有字段完整（特别是translations和names）

5. **Chart.js**: 必须本地下载，不能用CDN（避免CORS问题）
