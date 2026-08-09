# Prophets 项目 — 完整生成 Prompt

```markdown
你是一名全栈工程师。请从零开始构建一个名为 "Prophets（先知）" 的 Web 应用。

## 项目目标
- 用户完成60道情境选择题 → 系统计算12维性格向量 → 匹配最相似的历史人物
- 支持7种语言（中/英/西/日/德/俄/法）
- 付费解锁详细结果（¥9.90 或观看30秒广告）
- 部署在 Vercel

## 技术栈
- Backend: Python 3.11 + FastAPI + uvicorn
- Frontend: 单页 HTML + Vanilla JS + Chart.js（本地文件）
- 向量计算: numpy
- 部署: Vercel Serverless

## 目录结构
```
prophets/
├── src/
│   ├── __init__.py
│   ├── main.py                    # FastAPI 入口
│   ├── api/
│   │   ├── __init__.py
│   │   ├── quiz.py                # GET /api/quiz
│   │   ├── match.py               # POST /api/match
│   │   ├── payment.py             # 支付状态/创建/验证
│   │   ├── qr.py                  # 二维码生成
│   │   └── suggestions.py         # 建议生成
│   ├── data/
│   │   ├── __init__.py
│   │   ├── figures.py             # 人物数据加载
│   │   ├── questions.py           # 题目数据加载
│   │   ├── figures.json           # 96位历史人物
│   │   ├── questions.json         # 60道题目
│   │   └── traits.json            # 12维度定义
│   └── engine/
│       ├── __init__.py
│       ├── vector.py              # 向量计算
│       ├── matcher.py             # 匹配引擎
│       └── analyzer.py            # 差距分析
├── static/
│   ├── index.html                 # 单页应用
│   └── chart.min.js               # Chart.js 本地文件
├── requirements.txt
└── vercel.json
```

## 核心算法

### 1. 用户向量计算
- 60题对应12维度（每维度5题）
- 选项映射: 0→0.2, 1→0.5, 2→0.7, 3→1.0
- 每个维度计算所选答案的平均值
- 最终得到12维向量 [0,1]

### 2. 相似度计算
- 欧氏距离: dist = ||user_vector - figure_vector||
- 相似度: similarity = exp(-(dist²) / 2)
- 返回 TOP 10 匹配结果

### 3. 差距分析
- 计算每个维度的差距: gap = figure_value - user_value
- 按绝对值排序返回全部12个维度

## 数据结构

### figures.json — 96位历史人物
```json
{
  "id": 1,
  "name": "秦始皇",
  "era": "古代",
  "type": "帝王",
  "bio": "帝王，秦始皇的主要事迹与成就",
  "vector": {
    "openness": 0.22,
    "conscientiousness": 1.0,
    "extraversion": 0.91,
    "agreeableness": 0.17,
    "neuroticism": 0.25,
    "leadership": 0.96,
    "risk_taking": 0.86,
    "rationality": 0.79,
    "discipline": 0.96,
    "empathy": 0.08,
    "ambition": 0.94,
    "resilience": 0.98
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
**要求**: 96位人物，8类型×12人（帝王/军事家/政治家/思想家/科学家/艺术家/哲学家/宗教家），4时代×24人（古代/中世纪/近代/现代）。每人的names字段必须包含全部7语言。

### questions.json — 60道题目
```json
{
  "id": 1,
  "trait": "openness",
  "trait_cn": "开放性",
  "text": "面对全新的领域，你的态度是？",
  "options": ["充满好奇，积极尝试", "适度接受，但保持谨慎", "更倾向于熟悉的事物", "坚持传统，不喜变化"],
  "translations": {
    "zh": {"text": "...", "options": ["..."]},
    "en": {"text": "...", "options": ["..."]},
    "es": {"text": "...", "options": ["..."]},
    "ja": {"text": "...", "options": ["..."]},
    "de": {"text": "...", "options": ["..."]},
    "ru": {"text": "...", "options": ["..."]},
    "fr": {"text": "...", "options": ["..."]}
  }
}
```
**要求**: 60题，12维度×5题。每题必须有translations字段，包含全部7语言。

### traits.json — 12维度定义
```json
{
  "dimensions": [
    {"id": "openness", "name": "Openness", "name_cn": "开放性", "range_min": 0.0, "range_max": 1.0},
    // ... 12个维度
  ],
  "dimension_count": 12
}
```

## API 接口

### GET /api/health
返回: `{"status": "ok", "version": "0.1.0"}`

### GET /api/quiz?language=zh
返回60道题目（已处理语言翻译）:
```json
{
  "questions": [{"id": 1, "trait": "openness", "text": "...", "options": ["..."]}, ...],
  "total": 60,
  "language": "zh"
}
```

### POST /api/match
请求:
```json
{"answers": [{"question_id": 1, "option_index": 0}, ...], "language": "zh"}
```
返回:
```json
{
  "success": true,
  "matches": [
    {
      "figure_id": 1,
      "name": "秦始皇",
      "name_en": "Qin Shi Huang",
      "era": "古代",
      "type": "帝王",
      "similarity": 0.83,
      "gaps": [{"trait": "empathy", "user_value": 0.6, "figure_value": 0.08, "gap": -0.52}],
      "suggestion": {"figure_name": "秦始皇", "overall": "...", "suggestions": [...]}
    }
  ],
  "user_vector": {"openness": 0.65, ...},
  "summary": "您与秦始皇最为相似..."
}
```

### 支付API
- GET /api/payment/status/{user_id} — 查询支付状态
- POST /api/payment — 创建订单
- POST /api/payment/verify — 验证支付
- POST /api/payment/mock_pay — 模拟支付（测试用）
- GET /api/payment/qr/{order_id} — 生成二维码
- GET /api/payment/mock_qr/{user_id} — 测试用二维码

## 前端功能

### 页面流程
1. **首页** — 显示语言选择器、开始按钮
2. **答题页** — 60题逐题显示，进度条，自动保存答案
3. **支付页** — 未付费用户显示付费/广告选项
4. **结果页** — TOP 10匹配、雷达图、差距分析、改进建议

### 语言支持
- 7种语言切换：zh/en/es/ja/de/ru/fr
- 切换语言后重新加载题目（使用对应翻译）

### 支付流程
- 未付费：显示付费弹窗（¥9.90 或 30秒广告）
- 付费确认：输入 "qwe" 模拟支付
-  localStorage 记住支付状态（30天）

### 广告横幅
- 底部固定横幅
- localStorage 记住关闭状态

## Vercel 部署配置

### vercel.json
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
  "env": {"PYTHONPATH": "prophets"}
}
```

### requirements.txt
```
fastapi>=0.111.0
uvicorn>=0.30.0
numpy>=1.26.0
qrcode>=7.0.0
```

## 关键实现细节

### main.py 导入路径处理
```python
import sys
from pathlib import Path

_script = Path(__file__).resolve()
# Vercel部署: /var/task/prophets/src/main.py
# 需要添加 prophets/ 到 sys.path
if _script.parent.name == "src" and _script.parent.parent.name == "prophets":
    sys.path.insert(0, str(_script.parent.parent))
elif _script.parent.name == "src":
    sys.path.insert(0, str(_script.parent))

from src.api.quiz import router as quiz_router
# ... 其他导入
```

### 路由注册注意事项
- payment.py 和 qr.py 的路由定义**不能**有 `/api/` 前缀
- 因为 main.py 的 include_router 已加了 `prefix="/api"`
- 正确写法: `@router.get("/payment/status/{user_id}")`
- 错误写法: `@router.get("/api/payment/status/{user_id}")`

## 生成步骤

1. 创建目录结构
2. 生成 figures.json（96位历史人物 + 12维向量 + 7语言名字）
3. 生成 questions.json（60题 + 7语言翻译）
4. 生成 traits.json（12维度定义）
5. 实现 engine 模块（vector.py, matcher.py, analyzer.py）
6. 实现 API 模块（quiz.py, match.py, payment.py, qr.py, suggestions.py）
7. 实现 main.py（FastAPI 入口）
8. 实现 index.html（前端页面）
9. 创建 vercel.json 和 requirements.txt
10. 本地测试所有 API
11. 部署到 Vercel

## 数据生成提示

### 历史人物选择（96位）
**帝王(12)**: 秦始皇、汉武帝、唐太宗、宋太祖、成吉思汗、彼得大帝、凯撒、奥古斯都、图拉真、哈德良、拿破仑、路易十四

**军事家(12)**: 孙子、项羽、韩信、卫青、霍去病、亚历山大、汉尼拔、拿破仑、苏沃洛夫、顾城、粟裕、曼施坦因

**政治家(12)**: 孔子、管仲、商鞅、诸葛亮、张居正、林肯、丘吉尔、俾斯麦、梅特涅、华盛顿、杰斐逊、罗斯福

**思想家(12)**: 老子、孟子、荀子、朱熹、王阳明、苏格拉底、柏拉图、亚里士多德、康德、黑格尔、尼采、马克思

**科学家(12)**: 牛顿、爱因斯坦、达尔文、伽利略、居里夫人、法拉第、麦克斯韦、玻尔、海森堡、费曼、图灵、冯·诺依曼

**艺术家(12)**: 达芬奇、米开朗基罗、贝多芬、莫扎特、梵高、毕加索、莎士比亚、李白、杜甫、王羲之、齐白石、拉斐尔

**哲学家(12)**: 老子、孔子、庄子、孟子、柏拉图、亚里士多德、王阳明、笛卡尔、康德、黑格尔、尼采、萨特

**宗教家(12)**: 佛陀、耶稣、穆罕默德、老子、释迦牟尼、保罗、阿奎那、马丁·路德、王阳明、达摩、慧能、特蕾莎修女

### 向量赋值原则
- 帝王: 高leadership、高ambition、低empathy
- 科学家: 高openness、高rationality、高resilience
- 艺术家: 高openness、高empathy、低discipline
- 哲学/宗教家: 高idealism、高rationality

## 前端设计要点

### 设计风格
- 简洁现代，适合移动端
- 使用 CSS 变量定义主题色
- 主色调: 深蓝/灰色系，强调色: 橙棕色

### 关键组件
1. 语言选择器（顶部固定）
2. 进度条（答题时显示）
3. 题目卡片（逐题显示）
4. 雷达图（Chart.js）
5. 匹配结果列表（TOP 10）
6. 差距分析卡片
7. 改进建议列表

### JavaScript 核心函数
```javascript
let currentLang = 'zh';
let questions = [];
let answers = [];

async function loadQuiz() {
    const resp = await fetch(`/api/quiz?language=${currentLang}`);
    const data = await resp.json();
    questions = data.questions;
    renderQuestions();
}

async function submitQuiz() {
    const resp = await fetch('/api/match', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({answers, language: currentLang})
    });
    const data = await resp.json();
    renderResults(data);
}

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('language', lang);
    loadQuiz();
}
```

请开始生成完整代码。确保：
1. 所有文件都存在且格式正确
2. figures.json 有96条记录
3. questions.json 有60条记录
4. 所有翻译字段完整
5. API 测试通过
```
