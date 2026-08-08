# Prophets - 历史人物性格匹配引擎

> 你的性格像哪位历史人物？

## 项目概述

Prophets 是一个 Web 应用，通过 20 道基于历史事件决策情境的选择题，量化用户性格特征，并与 100 位中外历史人物进行多维度相似度匹配。

### 核心功能

1. **人物库**：100 位历史人物，每人 12 维性格向量
2. **性格测评**：20 道情境选择题，映射到 12 维性格空间
3. **相似度匹配**：余弦相似度计算，返回 TOP-5 最相似人物
4. **差距分析**：逐维度对比用户与每位相似人物的差异
5. **可视化**：雷达图展示性格分布

## 技术栈

| 层级 | 技术 | 说明 |
|------|------|------|
| 后端 | Python 3.11 + FastAPI | REST API |
| 数据 | JSON + NumPy | 人物数据 + 向量计算 |
| 前端 | 单页 HTML/CSS/JS | 无框架 |
| 可视化 | Chart.js | 雷达图 |

## 项目结构

```
E:/aiprojects/tinyapp/prophets/
├── README.md                 # 本文件
├── pyproject.toml            # 项目配置
├── run.py                    # 启动脚本
├── src/
│   ├── main.py               # FastAPI 入口
│   ├── data/
│   │   ├── figures.json      # 100 位历史人物数据
│   │   ├── traits.json       # 12 维性格维度定义
│   │   └── questions.json    # 20 道测评题目
│   ├── engine/
│   │   ├── vector.py         # 向量计算（余弦相似度）
│   │   ├── matcher.py        # 匹配引擎
│   │   └── analyzer.py       # 差距分析
│   └── api/
│       ├── quiz.py           # 测评相关接口
│       └── match.py          # 匹配结果接口
└── static/
    └── index.html            # 前端单页应用
```

## 数据模型

### 人物向量（12 维）

| 维度 | 范围 | 说明 |
|------|------|------|
| openness | 0-1 | 开放性：创新 vs 传统 |
| conscientiousness | 0-1 | 尽责性：计划 vs 随性 |
| extraversion | 0-1 | 外向性：社交 vs 独处 |
| agreeableness | 0-1 | 宜人性：合作 vs 竞争 |
| neuroticism | 0-1 | 情绪稳定性：稳定 vs 波动 |
| leadership | 0-1 | 领导力：主导 vs 跟随 |
| risk_taking | 0-1 | 冒险性：冒险 vs 保守 |
| rationality | 0-1 | 理性：逻辑 vs 情感 |
| discipline | 0-1 | 自律性：克制 vs 放纵 |
| empathy | 0-1 | 共情力：感知 vs 理性 |
| ambition | 0-1 | 野心：成就 vs 淡泊 |
| resilience | 0-1 | 韧性：抗压 vs 脆弱 |

## API 设计

### GET /api/quiz
获取测评题目列表

### POST /api/match
提交用户答案，获取匹配结果

**请求体**：
```json
{
  "answers": [{"question_id": 1, "option_index": 0}, ...]
}
```

**响应**：
```json
{
  "user_vector": {"openness": 0.65, ...},
  "matches": [
    {
      "figure_id": "sunzhongshan",
      "name": "孙中山",
      "similarity": 0.9924,
      "gaps": [{"trait": "openness", "user": 0.6, "figure": 0.8, "diff": -0.2}, ...]
    }
  ],
  "summary": "你与孙中山（99%相似）最像"
}
```

## 运行方式

```bash
cd E:/aiprojects/tinyapp/prophets
uvicorn src.main:app --reload --port 8000
```

访问: http://localhost:8000

## 验证状态

- ✅ 100 位历史人物数据
- ✅ 20 道测评题目
- ✅ 12 维性格模型
- ✅ 向量计算引擎
- ✅ 匹配算法
- ✅ API 接口
- ✅ 前端页面
