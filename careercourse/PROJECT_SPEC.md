# CareerCourse - 历史人物职业指导系统
## 完整项目规格说明书（供LLM重建项目使用）

---

## 1. 项目概述

### 1.1 产品定位
CareerCourse是一个职业性格测试网站，用户通过回答20道职业性格问题，与100位历史人物进行匹配，展示相似历史人物在相同职业阶段的经历和建议。

### 1.2 核心功能
1. **职业性格测试**：20道选择题，自动跳转，测量12维人格特质
2. **历史人物匹配**：基于向量相似度匹配最相似的历史人物
3. **详细展示**：显示匹配人物的早期经历、关键行动、核心成就、人生教训
4. **成长建议**：指出用户与匹配人物之间的特质差距

### 1.3 目标用户
- 处于职业迷茫期的年轻人
- 希望从历史人物经验中寻找灵感的人
- 对职业规划和性格分析感兴趣的用户

---

## 2. 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| 后端框架 | FastAPI | Python异步Web框架 |
| 运行服务器 | Uvicorn | ASGI服务器 |
| 前端 | 原生HTML/CSS/JavaScript | 单页面应用，无框架依赖 |
| 数据格式 | JSON | 人物和题目数据 |
| 匹配算法 | 欧几里得距离 | 12维向量空间 |

---

## 3. 项目结构

```
careercourse/
├── src/
│   ├── __init__.py
│   ├── main.py                    # FastAPI应用入口
│   ├── api/
│   │   ├── __init__.py
│   │   ├── quiz.py                # 题目API
│   │   ├── match.py               # 匹配API
│   │   └── figures.py             # 人物API
│   ├── engine/
│   │   ├── __init__.py
│   │   └── matcher.py             # 匹配引擎核心逻辑
│   └── data/
│       ├── figures.json           # 100位历史人物数据
│       └── questions.json         # 20道题目数据
├── static/
│   └── index.html                 # 前端页面
├── scripts/
│   ├── generate_data.py           # 人物数据生成脚本
│   └── generate_questions.py      # 题目数据生成脚本
├── pyproject.toml                 # 项目配置
└── README.md                      # 项目文档
```

---

## 4. 数据模型

### 4.1 历史人物数据 (figures.json)

每个历史人物包含以下字段：

```json
{
  "id": "newton",                    // 唯一标识符
  "name": "Isaac Newton",            // 英文名
  "name_cn": "牛顿",                  // 中文名
  "era": "1643-1727",                // 年代
  "period": "17世纪",                  // 时期
  "type": "科学家",                    // 类型
  "vector": {
    "openness": 0.6,                 // 开放性
    "conscientiousness": 0.9,        // 尽责性
    "extraversion": 0.2,             // 外向性
    "agreeableness": 0.2,            // 宜人性
    "neuroticism": 0.4,              // 情绪稳定性
    "leadership": 0.5,               // 领导力
    "risk_taking": 0.4,              // 风险承担
    "rationality": 0.95,             // 理性
    "discipline": 0.9,               // 自律
    "empathy": 0.2,                  // 共情
    "ambition": 0.7,                 // 野心
    "resilience": 0.8                // 韧性
  },
  "early_career": "剑桥大学三一学院学生...",  // 早期职业经历
  "early_actions": "在隔离期间发展出...",     // 关键行动
  "breakthrough": "发表《自然哲学的数学原理》...", // 核心成就
  "key_lesson": "Standing on the shoulders..." // 人生教训
}
```

### 4.2 题目数据 (questions.json)

```json
{
  "id": 1,
  "question": "面对一个全新且复杂的任务，你的第一反应是？",
  "dimension": "openness",
  "options": [
    {
      "text": "兴奋，渴望探索和学习",
      "values": {"openness": 0.9, "conscientiousness": 0.6, "risk_taking": 0.8}
    },
    // ... 更多选项
  ]
}
```

### 4.3 12维人格特质

| 维度 | 英文名称 | 含义 |
|------|----------|------|
| openness | Openness | 开放性，对新事物的接受度 |
| conscientiousness | Conscientiousness | 尽责性，计划性和条理性 |
| extraversion | Extraversion | 外向性，社交倾向 |
| agreeableness | Agreeableness | 宜人性，合作倾向 |
| neuroticism | Neuroticism | 情绪稳定性（低值=稳定） |
| leadership | Leadership | 领导力，决策能力 |
| risk_taking | Risk Taking | 风险承担意愿 |
| rationality | Rationality | 理性思维程度 |
| discipline | Discipline | 自律程度 |
| empathy | Empathy | 共情能力 |
| ambition | Ambition | 野心/成就动机 |
| resilience | Resilience | 韧性/抗压能力 |

---

## 5. API 接口规格

### 5.1 GET /api/figures
获取所有历史人物列表。

**响应格式：**
```json
{
  "figures": [...],
  "total": 100
}
```

### 5.2 GET /api/questions
获取所有测试题目。

**响应格式：**
```json
{
  "questions": [
    {
      "id": 1,
      "question": "...",
      "dimension": "...",
      "options": [...]
    }
  ],
  "total": 20
}
```

### 5.3 POST /api/match
提交答案，获取匹配结果。

**请求体：**
```json
{
  "answers": [
    {"question_id": 1, "option_index": 0},
    {"question_id": 2, "option_index": 2},
    // ... 20个答案
  ],
  "top_n": 10
}
```

**响应格式：**
```json
{
  "user_vector": {...},
  "matches": [
    {
      "figure": {...},
      "similarity": 0.85,
      "suggestion": {
        "figure_name": "牛顿",
        "figure_name_en": "Isaac Newton",
        "era": "1643-1727",
        "type": "科学家",
        "early_career": "...",
        "early_actions": "...",
        "breakthrough": "...",
        "key_lesson": "...",
        "gaps": [
          {"dimension": "resilience", "user_value": 0.5, "figure_value": 0.8, "difference": 0.3, "direction": "develop"}
        ],
        "overall": "Your career profile is most similar to 牛顿 (1643-1727)."
      }
    }
  ]
}
```

---

## 6. 匹配算法

### 6.1 用户向量计算
1. 收集用户所有答案
2. 对每道题，根据选项的values累加对应维度分数
3. 计算各维度平均值，得到12维用户向量

### 6.2 相似度计算
```
欧几里得距离 = sqrt(Σ(user_vec[i] - figure_vec[i])²)
相似度 = 1 - min(距离 / sqrt(维度数), 1.0)
```

### 6.3 真实人物优先
- 真实历史人物（20位）获得 +0.20 相似度加分
- 确保匹配结果中真实人物排在前面

### 6.4 边界处理
- option_index 超出选项范围时，自动钳制到有效范围
- 未回答的题目不参与计算

---

## 7. 前端规格

### 7.1 页面流程
1. **开始页面**：展示标题、简介、"开始测试"按钮
2. **答题页面**：显示当前题目、进度条、选项按钮
3. **加载页面**：显示"正在分析你的职业性格..."
4. **结果页面**：展示10个匹配人物卡片

### 7.2 交互逻辑
- 点击选项后，0.3秒后自动跳转到下一题
- 最后一题提交后显示加载动画
- 匹配结果按相似度降序排列
- 点击结果卡片可展开/收起详细信息
- 提供"重新测试"按钮

### 7.3 UI设计规范
- 深色主题背景渐变 (#1a1a2e → #16213e → #0f3460)
- 主色调：红色渐变 (#e94560 → #ff6b6b)
- 字体：Microsoft YaHei（中文）/ Segoe UI（英文）
- 卡片毛玻璃效果 (backdrop-filter: blur)
- 进度条红色渐变填充
- 结果卡片悬停效果：向右平移

### 7.4 容错处理
- API调用失败时返回开始页面
- 匹配结果为空时返回开始页面
- 添加调试日志便于排查问题

---

## 8. 数据生成

### 8.1 历史人物数据
- **真实人物**：20位著名历史人物，包含详细生平
- **泛化人物**：80位根据随机向量生成的"历史人物N"
- 生成脚本：`scripts/generate_data.py`

### 8.2 题目数据
- 20道职业性格测试题
- 每道题测量1-3个维度
- 每道题4-5个选项
- 生成脚本：`scripts/generate_questions.py`

---

## 9. 部署说明

### 9.1 环境要求
- Python 3.11+
- pip 或 uv

### 9.2 依赖安装
```bash
pip install fastapi uvicorn pydantic
```

### 9.3 启动命令
```bash
python -m uvicorn src.main:app --host 0.0.0.0 --port 8005
```

### 9.4 访问地址
```
http://localhost:8005
```

---

## 10. 核心代码实现

### 10.1 FastAPI应用 (main.py)
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pathlib import Path

STATIC_DIR = Path("static")

app = FastAPI(title="CareerCourse")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

from src.api import quiz, match, figures
app.include_router(quiz.router, prefix="/api")
app.include_router(match.router, prefix="/api")
app.include_router(figures.router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def root():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        with open(index_file, "r", encoding="utf-8") as f:
            return f.read()
    return HTMLResponse("<h1>Error: index.html not found</h1>")

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

### 10.2 匹配引擎 (matcher.py)
关键函数：
- `load_figures()`: 加载人物数据
- `load_questions()`: 加载题目数据
- `calculate_user_vector(answers)`: 计算用户向量
- `euclidean_distance(v1, v2)`: 计算欧几里得距离
- `is_real_figure(fig)`: 判断是否为真实人物
- `match_user(answers, top_n)`: 执行匹配
- `generate_suggestion(match_result)`: 生成建议

---

## 11. 20位真实历史人物

| ID | 英文名 | 中文名 | 类型 | 年代 |
|----|--------|--------|------|------|
| newton | Isaac Newton | 牛顿 | 科学家 | 1643-1727 |
| einstein | Albert Einstein | 爱因斯坦 | 科学家 | 1879-1955 |
| tesla | Nikola Tesla | 特斯拉 | 发明家 | 1856-1943 |
| galileo | Galileo Galilei | 伽利略 | 科学家 | 1564-1642 |
| mozart | Wolfgang Mozart | 莫扎特 | 艺术家 | 1756-1791 |
| shakespeare | William Shakespeare | 莎士比亚 | 作家 | 1564-1616 |
| curie | Marie Curie | 居里夫人 | 科学家 | 1867-1934 |
| lincoln | Abraham Lincoln | 林肯 | 政治家 | 1809-1865 |
| steve_jobs | Steve Jobs | 乔布斯 | 企业家 | 1955-2011 |
| elon_musk | Elon Musk | 马斯克 | 企业家 | 1971-至今 |
| mark_zuckerberg | Mark Zuckerberg | 扎克伯格 | 企业家 | 1984-至今 |
| bill_gates | Bill Gates | 比尔·盖茨 | 企业家 | 1955-至今 |
| warren_buffett | Warren Buffett | 沃伦·巴菲特 | 投资者 | 1930-至今 |
| edison | Thomas Edison | 爱迪生 | 发明家 | 1847-1931 |
| freud | Sigmund Freud | 弗洛伊德 | 心理学家 | 1856-1939 |
| darwin | Charles Darwin | 达尔文 | 科学家 | 1809-1882 |
| pasteur | Louis Pasteur | 巴斯德 | 科学家 | 1822-1895 |
| ada_lovelace | Ada Lovelace | 阿达·洛芙莱斯 | 科学家 | 1815-1852 |
| florence_nightingale | Florence Nightingale | 南丁格尔 | 护士 | 1820-1910 |
| helen_keller | Helen Keller | 海伦·凯勒 | 作家 | 1880-1968 |

---

## 12. 项目约束

1. **数据持久化**：使用JSON文件存储，无需数据库
2. **无状态设计**：每次请求独立计算，不存储用户状态
3. **前端无框架**：纯原生HTML/CSS/JavaScript
4. **CORS全开**：允许任何来源访问API
5. **中文界面**：所有用户可见文本使用中文
6. **响应式设计**：支持桌面和移动设备

---

## 13. 常见问题排查

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| 422 Unprocessable Entity | CORS配置缺失 | 添加CORS中间件 |
| 返回JSON而非HTML | 路由配置错误 | 使用HTMLResponse |
| 缓存导致界面不更新 | 浏览器缓存 | 添加no-cache meta标签 |
| 匹配结果为空 | 数据文件缺失 | 运行generate_data.py |
| 服务器启动失败 | 端口冲突 | 更换端口或杀掉占用进程 |

---

## 14. 开发工作流

1. 生成数据：`python scripts/generate_data.py && python scripts/generate_questions.py`
2. 启动服务器：`python -m uvicorn src.main:app --host 0.0.0.0 --port 8005`
3. 访问应用：浏览器打开 `http://localhost:8005`
4. 验证API：`curl http://localhost:8005/api/figures`

---

**文档版本**: 1.0  
**最后更新**: 2026-08-09  
**项目路径**: `E:/aiprojects/tinyapp/careercourse/`
