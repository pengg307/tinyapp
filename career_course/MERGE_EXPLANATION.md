# CareerProphet 合并方案

## 一、问题分析：4个项目的关系

### 项目对比表

| 项目 | 数据 | 功能 | 特点 | 状态 |
|------|------|------|------|------|
| **prophets/** | 20个真实人物 | 测试 + 支付 + 多语言 | 最完整，有payment/qr模块 | 保留代码 |
| **genprophets/** | 100个生成人物 | 简化版测试 | 与career_course几乎相同 | 废弃 |
| **careercourse/** | 早期版本 | 原型 | 已被替换 | 废弃 |
| **career_course/** | 100个真实人物 | 最新版 | 当前工作路径 | **主服务** |

### 核心发现

```
career_course/ = genprophets/ （几乎相同）
careercourse/ = 早期genprophets（可废弃）
prophets/ = 有支付功能的专业版
```

**实际只有3个独立项目：**
1. `prophets/` - 有支付系统、多语言、建议生成
2. `career_course/` - 有100位真实人物、雷达图、60题
3. `genprophets/` - 已合并到career_course

---

## 二、合并策略

### 方案：以career_course为基础，融合prophets的增强功能

```
最终结构：career_course/ (作为 CareerProphet 统一服务)
```

### 合并内容

| 来源 | 合并内容 | 目的 |
|------|----------|------|
| **career_course/** | 100位真实历史人物 | 完整数据 |
| **career_course/** | 60题 + 12维度 | 完整测试 |
| **career_course/** | Canvas雷达图 | 可视化 |
| **career_course/** | 加权欧氏+高斯衰减算法 | 精确匹配 |
| **prophets/** | payment.py（支付） | 商业化 |
| **prophets/** | qr.py（二维码） | 支付接口 |
| **prophets/** | suggestions.py（建议） | 详细报告 |
| **prophets/** | 多语言支持 | 国际化 |

---

## 三、实施步骤

### Step 1: 数据修复（已完成）

**问题：** career_course的向量格式错误
- figures.json中的vector是list：`[0.8, 0.9, ...]`
- matcher.py期望dict：`{"openness": 0.8, "conscientiousness": 0.9, ...}`

**修复：**
```python
# 脚本：scripts/fix_vectors.py
# 将80个历史人物的vector从list转换为dict
for fig in figures:
    vec = fig.get("vector")
    if isinstance(vec, list):
        fig["vector"] = {DIMENSIONS[i]: val for i, val in enumerate(vec)}
```

**结果：** ✓ 所有100个vector都是dict格式

### Step 2: 统一入口（已完成）

**文件：** `src/main.py`

```python
# 之前的career_course/main.py（简单版本）
app = FastAPI(title="CareerCourse")

# 现在的统一入口
app = FastAPI(title="CareerProphet")
```

**关键改动：**
```python
# 1. 更新服务名称
app = FastAPI(title="CareerProphet", description="职业性格测试与历史人物匹配平台")

# 2. 保留原有路由
app.include_router(quiz.router, prefix="/api")
app.include_router(match.router, prefix="/api")
app.include_router(figures.router, prefix="/api")

# 3. 预留支付路由（从prophets迁移）
# from src.api import payment, qr
# app.include_router(payment.router, prefix="/api")
# app.include_router(qr.router, prefix="/api")

# 4. 添加健康检查
@app.get("/health")
async def health():
    return {"status": "healthy", "service": "CareerProphet"}

# 5. 添加子页面路由
@app.get("/prophets")
async def prophets_page():
    # 未来可添加详细历史人物页面
    pass
```

### Step 3: 验证测试（已完成）

**测试脚本：** `scripts/verify_matcher.py`

```python
# 1. 检查数据完整性
figs = json.load(open("src/data/figures.json"))
questions = json.load(open("src/data/questions.json"))
assert len(figs["figures"]) == 100
assert len(questions["questions"]) == 60

# 2. 检查向量格式
for fig in figs["figures"]:
    assert isinstance(fig["vector"], dict), f"{fig['name']} has list vector"

# 3. 测试匹配引擎
from src.engine.matcher import match_user
answers = [{"question_id": i+1, "option_index": i%4} for i in range(60)]
result = match_user(answers, top_n=3)
assert len(result["matches"]) == 3
assert "radar" in result["matches"][0]["suggestion"]

# 4. 测试API服务
import subprocess, urllib.request
proc = subprocess.Popen([sys.executable, "-m", "uvicorn", "src.main:app", "--port", "8040"])
r = urllib.request.urlopen("http://localhost:8040/health")
assert json.loads(r.read())["status"] == "healthy"
```

---

## 四、技术架构

### 统一服务架构

```
CareerProphet/
│
├── src/
│   ├── main.py              # 统一入口（已合并）
│   ├── api/
│   │   ├── quiz.py          # 题目接口（来自career_course）
│   │   ├── match.py         # 匹配接口（来自career_course）
│   │   ├── figures.py       # 人物接口（来自career_course）
│   │   ├── payment.py       # 支付接口（预留，来自prophets）
│   │   ├── qr.py            # 二维码（预留，来自prophets）
│   │   └── suggestions.py   # 建议生成（预留，来自prophets）
│   ├── engine/
│   │   ├── matcher.py       # 匹配引擎（加权欧氏+高斯衰减）
│   │   ├── vector.py        # 向量计算
│   │   └── analyzer.py      # 差距分析
│   └── data/
│       ├── figures.json     # 100位真实历史人物
│       └── questions.json   # 60题
│
├── static/
│   ├── index.html           # 主页面（测试流程）
│   └── prophets/            # 子页面（预留）
│
├── scripts/
│   ├── fix_vectors.py       # 向量格式修复
│   ├── replace_names.py     # 替换占位符名称
│   └── verify_matcher.py    # 验证脚本
│
└── README.md                # 项目说明
```

### API端点

| 端点 | 方法 | 功能 | 来源 |
|------|------|------|------|
| `/health` | GET | 健康检查 | 统一入口 |
| `/api/questions` | GET | 获取60道题 | career_course |
| `/api/match` | POST | 匹配历史人物 | career_course |
| `/api/figures` | GET | 获取人物列表 | career_course |
| `/api/payment` | POST | 支付接口 | prophets（预留） |
| `/api/qr` | GET | 二维码 | prophets（预留） |

---

## 五、用户预期

### 用户体验流程

```
1. 用户访问 http://localhost:8006
   ↓
2. 看到"职业性格测试"页面
   ↓
3. 回答60道题目（约5分钟）
   ↓
4. 查看匹配的10位历史人物
   ↓
5. 雷达图对比（蓝色=用户，红色=历史人物）
   ↓
6. 点击查看详细建议（早期经历、关键行动、核心成就）
   ↓
7. （可选）付费获取完整报告
```

### 核心价值

1. **自我认知** - 通过60题了解12维职业性格
2. **历史对标** - 匹配100位真实历史人物
3. **可视化** - 雷达图直观展示差异
4. **可执行建议** - 早期经历、关键行动、人生教训

---

## 六、未合并部分（可选）

以下功能来自prophets，暂未合并但可集成：

1. **支付系统** - payment.py, qr.py
   - 需要微信支付API密钥
   - 可选：免费测试 + 付费详细报告

2. **多语言支持**
   - prophets有zh/en/es/ja/de/ru/fr
   - career_course仅中文（已够用）

3. **详细建议生成**
   - prophets的suggestions.py更复杂
   - career_course有简单文本建议

**决策：** 先保持简洁，用户反馈后再添加付费功能。

---

## 七、Git提交历史

```
9940316 feat: merge all projects into CareerProphet unified service
7ac4ebb fix: convert list vectors to dictionaries in figures.json
5ab1d54 fix: replace final 3 placeholder names (Euler, Gauss, Riemann)
258d54f fix: replace remaining 3 placeholder names
8cdf8da fix: replace all placeholder names with real historical figures
```

---

## 八、运行方式

```bash
# 进入项目目录
cd E:/aiprojects/tinyapp/career_course

# 启动服务
python -m uvicorn src.main:app --port 8006

# 访问
http://localhost:8006
```

**验证：**
```bash
curl http://localhost:8006/health
# {"status": "healthy", "service": "CareerProphet"}

curl http://localhost:8006/api/questions
# {"questions": [...], "total": 60}

curl -X POST http://localhost:8006/api/match -H "Content-Type: application/json" \
  -d '{"answers": [...], "top_n": 3}'
# {"matches": [{"suggestion": {"figure_name": "牛顿", ...}}, ...]}
```
