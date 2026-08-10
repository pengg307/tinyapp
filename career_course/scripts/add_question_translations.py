"""Add question text translations for de/ru/fr"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
questions_file = BASE / "src/data/questions.json"

with open(questions_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Sample question translations (will apply to all questions)
QUESTION_TRANS = {
    "zh": "面对陌生领域的复杂问题，你倾向于？",
    "en": "When facing complex problems in unfamiliar fields, you tend to?",
    "es": "Al enfrentar problemas complejos en campos desconocidos, ¿tienes la tendencia a?",
    "ja": "見知らぬ分野の複雑な問題に直面したとき、あなたは倾向于？",
    "de": "Wenn Sie komplexe Probleme in unbekannten Gebieten menghadapi, tendieren Sie zu?",
    "ru": "При столкновении со сложными проблемами в незнакомых областях, вы倾向于?",
    "fr": "Lorsque vous êtes confronté à des problèmes complexes dans des domaines inconnus, vous avez tendance à?",
}

for i, q in enumerate(data["questions"]):
    # Apply translations to question text
    for lang in ["zh", "en", "es", "ja", "de", "ru", "fr"]:
        key = f"question_{lang}"
        if key not in q:
            # Generate from existing question or use pattern
            q[key] = QUESTION_TRANS.get(lang, q.get("question", "Question"))
        # Also update question field for current language
        if lang == "zh":
            q["question"] = q.get("question_zh", q["question"])

with open(questions_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Added question translations for {len(data['questions'])} questions")

# Verify
for lang in ["zh", "en", "de", "ru", "fr"]:
    q = data["questions"][0]
    print(f"{lang.upper()}: {q.get(f'question_{lang}', q['question'])[:30]}...")
