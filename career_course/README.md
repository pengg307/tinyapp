"""
CareerProphet - 职业性格测试与历史人物匹配平台

统一服务，融合以下项目：
- prophets: 支付系统、多语言支持
- career_course: 100位真实历史人物、60题、雷达图
- genprophets: Canvas雷达图实现

功能：
1. 职业性格测试（60题，12维度）
2. 历史人物匹配（100位真实人物）
3. 雷达图可视化
4. 差距分析和建议
5. 支付系统（可选）
6. 多语言支持（zh/en/es/ja/de/ru/fr）

技术栈：
- FastAPI + Uvicorn
- Canvas雷达图
- 加权欧氏距离 + 高斯衰减匹配算法
"""

# 主入口在 src/main.py
# 运行方式：python -m uvicorn src.main:app --port 8006
