"""Fix remaining 3 placeholders"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
figs_file = BASE / "src/data/figures.json"

with open(figs_file, encoding="utf-8") as f:
    data = json.load(f)

figures = data["figures"]

# Fix remaining placeholders
EXTRA_FIGURES = [
    {"name": "Einstein", "name_cn": "爱因斯坦", "era": "现代", "type": "科学家",
     "vector": [0.95, 0.7, 0.5, 0.6, 0.4, 0.6, 0.9, 0.95, 0.6, 0.7, 0.8, 0.7],
     "early_career": "专利局职员期间发表奇迹年论文",
     "early_actions": "提出相对论，解释光电效应",
     "breakthrough": "E=mc²改变人类对宇宙的认知",
     "key_lesson": "想象力比知识更重要"},
    {"name": "Curie", "name_cn": "居里夫人", "era": "现代", "type": "科学家",
     "vector": [0.85, 0.95, 0.4, 0.7, 0.3, 0.5, 0.8, 0.9, 0.95, 0.6, 0.9, 0.9],
     "early_career": "巴黎理化学校研究放射性物质",
     "early_actions": "发现钋和镭，开创放射性理论",
     "breakthrough": "两获诺贝尔奖，唯一跨物理学和化学",
     "key_lesson": "坚韧不拔是科学的基石"},
    {"name": "Darwin", "name_cn": "达尔文", "era": "维多利亚", "type": "科学家",
     "vector": [0.85, 0.8, 0.4, 0.65, 0.3, 0.5, 0.75, 0.9, 0.75, 0.6, 0.7, 0.8],
     "early_career": "小猎犬号环球航行考察",
     "early_actions": "研究物种变异，提出自然选择",
     "breakthrough": "《物种起源》改变人类自我认知",
     "key_lesson": "适应者生存，而非最强者"},
]

# Find and fix
for i, fig in enumerate(figures):
    if "历史人物" in fig.get("name_cn", ""):
        if i < len(EXTRA_FIGURES):
            extra = EXTRA_FIGURES[i]
            fig["name"] = extra["name"]
            fig["name_cn"] = extra["name_cn"]
            fig["era"] = extra["era"]
            fig["type"] = extra["type"]
            fig["vector"] = extra["vector"]
            fig["early_career"] = extra["early_career"]
            fig["early_actions"] = extra["early_actions"]
            fig["breakthrough"] = extra["breakthrough"]
            fig["key_lesson"] = extra["key_lesson"]
            print(f"Fixed index {i}: {extra['name_cn']} ({extra['name']})")

# Save
data["figures"] = figures
with open(figs_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✓ Fixed {len(EXTRA_FIGURES)} remaining placeholders")
