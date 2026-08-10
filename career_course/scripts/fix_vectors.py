"""Fix vectors to be dictionaries instead of lists"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
figs_file = BASE / "src/data/figures.json"

with open(figs_file, encoding="utf-8") as f:
    data = json.load(f)

figures = data["figures"]
DIMENSIONS = [
    "openness","conscientiousness","extraversion","agreeableness","neuroticism",
    "leadership","risk_taking","rationality","discipline","empathy","ambition","resilience"
]

# Convert list vectors to dictionaries
converted = 0
for fig in figures:
    vec = fig.get("vector")
    if isinstance(vec, list):
        fig["vector"] = {DIMENSIONS[i]: val for i, val in enumerate(vec)}
        converted += 1
    elif not isinstance(vec, dict):
        print(f"Warning: {fig.get('name')} has invalid vector type: {type(vec)}")

print(f"Converted {converted} figures from list to dict vectors")

# Save
data["figures"] = figures
with open(figs_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Saved to {figs_file}")
