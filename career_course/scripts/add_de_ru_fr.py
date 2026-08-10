"""Add German, Russian, French translations to all questions"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
questions_file = BASE / "src/data/questions.json"

with open(questions_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Add de/ru/fr translations for each pattern
PATTERNS = [
    {
        "de": ["Flexibel anpassen und schnell handeln", "Tief analysieren und vorsichtig entscheiden", "Begeistert erforschen und Unsicherheit akzeptieren", "Der Tradition folgen und stetig vorankommen"],
        "ru": ["Гибко адаптироваться и быстро действовать", "Глубоко анализировать и осторожно принимать решения", "Энтузиастично исследовать и принимать неопределенность", "Следовать традициям и steadily прогрессировать"],
        "fr": ["S'adapter flexiblement et agir rapidement", "Analyser profondément et décider prudemment", "Explorer enthousiaste et accepter l'incertitude", "Suivre la tradition et progresser steadily"],
    },
    {
        "de": ["Proaktiv kommunizieren und Konsens suchen", "Konflikte vermeiden und Harmonie wahren", "An Prinzipien festhalten und leidenschaftlich argumentieren", "Flexibel sein und Harmonie priorisieren"],
        "ru": ["Проактивно коммуницировать и искать консенсус", "Избегать конфликтов и сохранять гармонию", "Придерживаться принципов и твердо аргументировать", "Быть гибким и приоритизировать гармонию"],
        "fr": ["Communiquer proactivement et chercher le consensus", "Éviter les conflits et maintenir l'harmonie", "S'en tenir aux principes et argumenter fermement", "Être flexible et privilégier l'harmonie"],
    },
    {
        "de": ["Detaillierte Pläne erstellen und strikt ausführen", "Allgemeinen Rahmen erstellen und flexibel anpassen", "Während desmachens anpassen und auf Veränderungen reagieren", "Der Intuition folgen und die Natur entwickeln lassen"],
        "ru": ["Создавать детальные планы и строго выполнять", "Создать общий框架 и гибко адаптировать", "Адаптировать во время выполнения и реагировать на изменения", "Следовать интуиции и позволить природе развиваться"],
        "fr": ["Créer des plans détaillés et exécuter strictement", "Créer un cadre général et ajuster flexiblement", "Ajuster pendant l'exécution et réagir aux changements", "Suivre l'intuition et laisser la nature se développer"],
    },
    {
        "de": ["Führer, das Team voranbringen", "Ausführer, Aufgaben effizient abschließen", "Koordinator, Teamharmonie fördern", "Unterstützer, mit Teamarbeit kooperieren"],
        "ru": ["Лидер, продвигать команду вперед", "Исполнитель, эффективно завершать задачи", "Координатор, способствовать командной гармонии", "Помощник, сотрудничать с командной работой"],
        "fr": ["Leader, pousser l'équipe vers l'avant", "Exécutant, compléter les tâches efficacement", "Coordinateur, promouvoir l'harmonie d'équipe", "Soutien, coopérer avec le travail d'équipe"],
    },
]

for i, q in enumerate(data["questions"]):
    pattern_idx = i % len(PATTERNS)
    pattern = PATTERNS[pattern_idx]
    
    for j, opt in enumerate(q.get("options", [])):
        if j < 4:
            opt["text_de"] = pattern["de"][j]
            opt["text_ru"] = pattern["ru"][j]
            opt["text_fr"] = pattern["fr"][j]

with open(questions_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Added de/ru/fr to {len(data['questions'])} questions")

# Verify
for lang in ["de", "ru", "fr"]:
    q = data["questions"][0]
    opts = [opt[f"text_{lang}"] for opt in q["options"]]
    print(f"{lang.upper()}: {opts[0][:20]}...")
