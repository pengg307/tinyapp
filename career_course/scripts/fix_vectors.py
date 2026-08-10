"""Fix list vectors to dict format in career_course"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
DIMENSIONS = [
    "openness","conscientiousness","extraversion","agreeableness","neuroticism",
    "leadership","risk_taking","rationality","discipline","empathy","ambition","resilience"
]

figs_file = BASE / "src/data/figures.json"
with open(figs_file, encoding="utf-8") as f:
    data = json.load(f)

converted = 0
for fig in data["figures"]:
    vec = fig.get("vector")
    if isinstance(vec, list):
        fig["vector"] = {DIMENSIONS[i]: val for i, val in enumerate(vec)}
        converted += 1

print(f"Converted {converted} figures")

with open(figs_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Saved to {figs_file}")