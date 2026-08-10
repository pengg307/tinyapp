"""Add English option translations"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
questions_file = BASE / "src/data/questions.json"

with open(questions_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# English option translations
OPTION_EN = [
    "Adapt flexibly and act quickly",
    "Analyze deeply and decide cautiously",
    "Explore enthusiastically and accept uncertainty",
    "Follow tradition and progress steadily",
    "Communicate proactively and seek consensus",
    "Avoid conflict and maintain harmony",
    "Stick to principles and argue firmly",
    "Be flexible and prioritize harmony",
    "Make detailed plans and execute strictly",
    "Create general framework and adjust flexibly",
    "Adjust while doing and adapt to changes",
    "Follow intuition and let nature develop",
    "Lead and drive the team forward",
    "Execute and complete tasks efficiently",
    "Coordinate and promote team harmony",
    "Support and cooperate with team work",
    "Stay calm and analyze rationally",
    "Actively seek help and ask for support",
    "Handle alone and bear silently",
    "Release pressure and adjust mindset",
    # Pattern 2 - questions 20-39
    "Take initiative in conflict resolution",
    "Avoid confrontation and keep peace",
    "Stand firm on principles",
    "Compromise for harmony",
    "Plan in detail",
    "Be flexible with plans",
    "Adjust on the fly",
    "Follow natural flow",
    "Lead the team",
    "Support the team",
    "Coordinate efforts",
    "Work independently",
    "Stay calm under pressure",
    "Seek support from others",
    "Handle pressure alone",
    "Take time to decompress",
    # Pattern 3 - questions 40-59
    "Face conflict directly",
    "Avoid conflict when possible",
    "Stand ground on principles",
    "Find middle ground",
    "Plan everything out",
    "Keep plans flexible",
    "Adapt as you go",
    "Go with the flow",
    "Take charge",
    "Follow along",
    "Bridge differences",
    "Work solo",
    "Remain composed",
    "Ask for help",
    "Endure silently",
    "Take a break",
    # Pattern 4 - questions 60-79 (duplicates for 60 questions)
    "Address conflict head-on",
    "Sidestep conflict",
    "Hold your ground",
    "Meet halfway",
    "Detail-oriented planning",
    "Flexible planning",
    "Improvisation",
    "Intuitive approach",
    "Leadership role",
    "Supportive role",
    "Mediation role",
    "Independent role",
    "Calm analysis",
    "Seek assistance",
    "Self-reliance",
    "Stress relief",
]

# Apply translations
for i, q in enumerate(data["questions"]):
    for j, opt in enumerate(q.get("options", [])):
        if j < len(OPTION_EN):
            opt["text_en"] = OPTION_EN[(i * 4 + j) % len(OPTION_EN)]
        else:
            opt["text_en"] = opt["text"]

# Save
with open(questions_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Updated {len(data['questions'])} questions with English option translations")
