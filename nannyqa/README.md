# 家政面试题库系统 - v3.0

## 新功能：双角色流程 + 二维码分发

### 核心流程

```
雇主端                         应聘者端
─────────────────────────────────────────────
1. 打开APP
2. 输入姓名（可选）
3. 点击"生成二维码"
4. 系统创建Session（12小时有效）
5. 显示二维码和链接
6. 发送链接/二维码给应聘者
                              │
                              ▼
                              应聘者扫码/访问链接
                              进入答题页面
                              回答90道题目
                              点击提交
                              显示"感谢参与"
                              │
                              ▼
雇主再次打开APP
输入Session ID
查看评估报告
- 总分和星级
- 雷达图
- 维度分析
- 逐题详情（含反馈）
```

### API 端点

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/session` | POST | 创建测试会话，返回session_id和二维码数据 |
| `/api/session/{id}` | GET | 查询会话状态 |
| `/api/session/{id}/report` | GET | 获取评估报告（需完成） |
| `/api/session/{id}` | DELETE | 取消测试 |
| `/api/session/{id}/submit` | POST | 提交答案（应聘者） |
| `/test/{id}` | GET | 应聘者答题页面 |
| `/api/questions` | GET | 获取题目列表 |

### 技术实现

- **会话存储**: 内存字典（生产环境建议用Redis）
- **过期机制**: 12小时有效期，每分钟自动清理
- **二维码**: 使用qrcodejs库在前端生成
- **双角色分离**: 雇主端和应聘者端完全隔离

### 文件结构

```
E:/aiprojects/tinyapp/nannyqa/
├── src/
│   ├── main.py          # FastAPI后端（v3.0重写）
│   └── data/
│       └── questions.json  # 90道题目
├── static/
│   └── index.html       # 雇主端前端（含二维码）
└── scripts/
    ├── generate_questions.py
    ├── add_remaining_questions.py
    └── generate_qr.py    # 命令行生成二维码工具
```

### 使用示例

1. 雇主打开 http://localhost:8005
2. 输入姓名，点击"生成二维码"
3. 截图二维码或复制链接发给应聘者
4. 应聘者扫码答题（90题，约15-20分钟）
5. 雇主查询报告查看评估结果
