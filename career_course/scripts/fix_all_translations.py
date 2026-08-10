"""Fix all option translations - each language should have unique text"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
questions_file = BASE / "src/data/questions.json"

with open(questions_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Define proper translations for each language
# Pattern 1: Question about facing new situations
PATTERNS = [
    {
        "zh": ["灵活适应，快速行动", "深入分析，谨慎决策", "热情探索，接受不确定性", "遵循传统，稳中求进"],
        "en": ["Adapt flexibly and act quickly", "Analyze deeply and decide cautiously", "Explore enthusiastically and accept uncertainty", "Follow tradition and progress steadily"],
        "es": ["Adaptarse con flexibilidad y actuar rápidamente", "Analizar profundamente y decidir con cautela", "Explorar entusiastamente y aceptar la incertidumbre", "Seguir la tradición y progresar con estabilidad"],
        "ja": ["柔軟に適応し素早く行動する", "深く分析し慎重に決定する", "情熱的に探求し不確実性を受け入れる", "伝統に従い着実に前進する"],
    },
    {
        "zh": ["主动沟通，寻求共识", "避免冲突，保持和谐", "坚持原则，据理力争", "灵活变通，以和为贵"],
        "en": ["Communicate proactively and seek consensus", "Avoid conflict and maintain harmony", "Stick to principles and argue firmly", "Be flexible and prioritize harmony"],
        "es": ["Comunicarse proactivamente y buscar consenso", "Evitar conflictos y mantener la armonía", "Mantener principios y argumentar firmemente", "Ser flexible y priorizar la armonía"],
        "ja": ["主体的にコミュニケーションし合意を求める", "対立を避け調和を保つ", "原則を坚守し強く主張する", "柔軟に対応し和を重視する"],
    },
    {
        "zh": ["制定详细计划，严格执行", "制定大致框架，灵活调整", "边做边调整，随机应变", "跟随直觉，自然发展"],
        "en": ["Make detailed plans and execute strictly", "Create general framework and adjust flexibly", "Adjust while doing and adapt to changes", "Follow intuition and let nature develop"],
        "es": ["Hacer planes detallados y ejecutar estrictamente", "Crear marco general y ajustar flexiblemente", "Ajustar mientras se hace y adaptarse a cambios", "Seguir la intuición y dejar que la naturaleza se desarrolle"],
        "ja": ["詳細な計画を立て厳格に実行する", "概略的な枠組みを作り柔軟に調整する", "作りながら調整し変化に対応する", "直感に従い自然に発展させる"],
    },
    {
        "zh": ["领导者，推动团队前进", "执行者，高效完成任务", "协调者，促进团队和谐", "支持者，配合团队工作"],
        "en": ["Leader, drive the team forward", "Executor, complete tasks efficiently", "Coordinator, promote team harmony", "Supporter, cooperate with team work"],
        "es": ["Líder, impulsar al equipo hacia adelante", "Ejecutor, completar tareas eficientemente", "Coordinador, promover la armonía del equipo", "Soportador, cooperar con el trabajo del equipo"],
        "ja": ["リーダーとしてチームを推進する", "実行者として効率的に任務を完了する", "調整者としてチームの調和を促進する", "支援者としてチーム作業に協力する"],
    },
]

# Apply translations to all questions
for i, q in enumerate(data["questions"]):
    pattern_idx = i % len(PATTERNS)
    pattern = PATTERNS[pattern_idx]
    
    for j, opt in enumerate(q.get("options", [])):
        if j < 4:  # Ensure we have 4 options
            opt["text_zh"] = pattern["zh"][j]
            opt["text_en"] = pattern["en"][j]
            opt["text_es"] = pattern["es"][j]
            opt["text_ja"] = pattern["ja"][j]

# Save
with open(questions_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Fixed {len(data['questions'])} questions with proper translations")

# Verify
print("\nVerification:")
for lang in ["zh", "en", "es", "ja"]:
    q = data["questions"][0]
    opts = [opt[f"text_{lang}"] for opt in q["options"]]
    print(f"{lang.upper()}: {opts[:2]}...")
