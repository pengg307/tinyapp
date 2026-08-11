"""CareerProphet - Matcher Engine with full multilingual support"""
import json
import math
from pathlib import Path

DIMENSIONS = [
    "openness","conscientiousness","extraversion","agreeableness","neuroticism",
    "leadership","risk_taking","rationality","discipline","empathy","ambition","resilience"
]

# Dimension name translations for all 8 languages
DIM_NAMES = {
    "zh": {"openness": "开放性", "conscientiousness": "尽责性", "extraversion": "外向性",
           "agreeableness": "宜人性", "neuroticism": "情绪稳定性", "leadership": "领导力",
           "risk_taking": "冒险精神", "rationality": "理性", "discipline": "自律性",
           "empathy": "同理心", "ambition": "雄心", "resilience": "韧性"},
    "en": {"openness": "Openness", "conscientiousness": "Conscientiousness", "extraversion": "Extraversion",
           "agreeableness": "Agreeableness", "neuroticism": "Emotional Stability", "leadership": "Leadership",
           "risk_taking": "Risk Taking", "rationality": "Rationality", "discipline": "Discipline",
           "empathy": "Empathy", "ambition": "Ambition", "resilience": "Resilience"},
    "es": {"openness": "Apertura", "conscientiousness": "Responsabilidad", "extraversion": "Extraversión",
           "agreeableness": "Amabilidad", "neuroticism": "Estabilidad Emocional", "leadership": "Liderazgo",
           "risk_taking": "Toma de Riesgos", "rationality": "Racionalidad", "discipline": "Disciplina",
           "empathy": "Empatía", "ambition": "Ambición", "resilience": "Resiliencia"},
    "ja": {"openness": "開放性", "conscientiousness": "誠実性", "extraversion": "外向性",
           "agreeableness": "協調性", "neuroticism": "感情の安定", "leadership": "リーダーシップ",
           "risk_taking": "リスクテイク", "rationality": "合理性", "discipline": "自制心",
           "empathy": "共感力", "ambition": "野心", "resilience": "回復力"},
    "de": {"openness": "Offenheit", "conscientiousness": "Gewissenhaftigkeit", "extraversion": "Extravertiertheit",
           "agreeableness": "Verträglichkeit", "neuroticism": "Emotionale Stabilität", "leadership": "Führung",
           "risk_taking": "Risikobereitschaft", "rationality": "Rationalität", "discipline": "Disziplin",
           "empathy": "Empathie", "ambition": "Ambition", "resilience": "Widerstandsfähigkeit"},
    "ru": {"openness": "Открытость", "conscientiousness": "Добросовестность", "extraversion": "Экстраверсия",
           "agreeableness": "Доброжелательность", "neuroticism": "Эмоциональная стабильность", "leadership": "Лидерство",
           "risk_taking": "Склонность к риску", "rationality": "Рациональность", "discipline": "Дисциплина",
           "empathy": "Эмпатия", "ambition": "Амбициозность", "resilience": "Стрессоустойчивость"},
    "fr": {"openness": "Ouverture", "conscientiousness": "Conscience", "extraversion": "Extraversion",
           "agreeableness": "Agrément", "neuroticism": "Stabilité émotionnelle", "leadership": "Leadership",
           "risk_taking": "Prise de risque", "rationality": "Rationalité", "discipline": "Discipline",
           "empathy": "Empathie", "ambition": "Ambition", "resilience": "Résilience"},
    "ko": {"openness": "개방성", "conscientiousness": "성실성", "extraversion": "외향성",
           "agreeableness": "친화성", "neuroticism": "정서적 안정", "leadership": "리더십",
           "risk_taking": "위험 감수", "rationality": "합리성", "discipline": "자율성",
           "empathy": "공감력", "ambition": "야망", "resilience": "회복력"}
}

# FIXED: Map each of 60 questions to one of 12 dimensions (5 questions per dimension)
# Order: openness, conscientiousness, extraversion, agreeableness, neuroticism,
#        leadership, risk_taking, rationality, discipline, empathy, ambition, resilience
ANSWER_DIM_MAP = [
    0, 1, 2, 3, 4,  # Q1-5: First 5 dimensions
    5, 6, 7, 8, 9,  # Q6-10: Next 5 dimensions
    10, 11, 0, 1, 2,  # Q11-15: Wrap around
    3, 4, 5, 6, 7,  # Q16-20
    8, 9, 10, 11, 0,  # Q21-25
    1, 2, 3, 4, 5,  # Q26-30
    6, 7, 8, 9, 10,  # Q31-35
    11, 0, 1, 2, 3,  # Q36-40
    4, 5, 6, 7, 8,  # Q41-45
    9, 10, 11, 0, 1,  # Q46-50
    2, 3, 4, 5, 6,  # Q51-55
    7, 8, 9, 10, 11  # Q56-60
]

# Option values: 0=very low, 1=low, 2=high, 3=very high
OPTION_VALUES = [0.2, 0.4, 0.7, 0.9]

DATA_DIR = Path(__file__).parent.parent / "data"
FIGURES_FILE = DATA_DIR / "figures.json"
QUESTIONS_FILE = DATA_DIR / "questions.json"

def load_figures():
    with open(FIGURES_FILE, "r", encoding="utf-8") as f:
        return json.load(f).get("figures", [])

def load_questions():
    with open(QUESTIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f).get("questions", [])

def is_real_figure(fig):
    return fig.get("id", "").startswith(("isaac_", "albert_", "marie_", "leonardo_", "nikola_",
                                          "william_", "shakespeare_", "abraham_", "mahatma_",
                                          "napoleon_", "winston_", "ada_", "florence_", "charles_",
                                          "galileo_", "mendel_", "darwin_", "pascal_", "newton_"))

def calculate_user_vector(answers):
    """Calculate user vector from answers using proper normalization."""
    # Initialize dimension accumulators
    dim_sums = {d: 0.0 for d in DIMENSIONS}
    dim_counts = {d: 0 for d in DIMENSIONS}

    # Collect scores for each dimension
    for ans in answers:
        q_idx = ans.get("question_id", 0) - 1
        opt_idx = ans.get("option_index", 0)

        if 0 <= q_idx < len(ANSWER_DIM_MAP) and 0 <= opt_idx < 4:
            dim_idx = ANSWER_DIM_MAP[q_idx]
            dim = DIMENSIONS[dim_idx]
            dim_sums[dim] += OPTION_VALUES[opt_idx]
            dim_counts[dim] += 1

    # Calculate mean for each dimension
    user_vec = {}
    for dim in DIMENSIONS:
        if dim_counts[dim] > 0:
            user_vec[dim] = dim_sums[dim] / dim_counts[dim]
        else:
            user_vec[dim] = 0.5  # Default if no questions for this dimension

    return user_vec

def weighted_distance(v1, v2):
    """Calculate weighted Euclidean distance between two vectors."""
    total = 0
    for dim in DIMENSIONS:
        diff = v1.get(dim, 0.5) - v2.get(dim, 0.5)
        total += diff ** 2
    return math.sqrt(total)

def similarity_score(user_vec, fig_vec, is_real=False):
    """Calculate similarity score using Gaussian decay with proper spread."""
    dist = weighted_distance(user_vec, fig_vec)

    # Use sigma=0.8 for better discrimination while maintaining reasonable scores
    # This gives good spread: close matches ~0.9, distant ~0.3
    sim = math.exp(-(dist ** 2) / (2 * 0.8 ** 2))

    # Add bonus for real historical figures (small bonus to not dominate)
    if is_real:
        bonus = 0.05 * max(0, 1 - dist / 1.2)
        sim = min(0.99, sim + bonus)

    # Penalize large gaps more aggressively
    big_gaps = sum(1 for d in DIMENSIONS if abs(user_vec.get(d, 0.5) - fig_vec.get(d, 0.5)) > 0.4)
    if big_gaps >= 6:
        sim *= 0.6
    elif big_gaps >= 5:
        sim *= 0.7
    elif big_gaps >= 4:
        sim *= 0.85
    elif big_gaps >= 3:
        sim *= 0.95

    return round(sim, 3)

def match_user(answers, top_n=10, language="zh"):
    """Match user answers against historical figures."""
    user_vec = calculate_user_vector(answers)
    figures = load_figures()
    results = []

    for fig in figures:
        if not is_real_figure(fig):
            continue

        fig_vec = fig.get("vector", {})
        sim = similarity_score(user_vec, fig_vec, is_real=True)

        # Calculate gaps with translated dimension names
        gaps = []
        for d in DIMENSIONS:
            user_val = user_vec.get(d, 0.5)
            fig_val = fig_vec.get(d, 0.5)
            gap = round(fig_val - user_val, 2)
            if abs(gap) > 0.15:
                gaps.append({
                    "trait": d,
                    "dimension": DIM_NAMES.get(language, DIM_NAMES["zh"]).get(d, d),
                    "gap": gap,
                    "direction": "up" if gap > 0 else "down",
                    "user_value": round(user_val, 2),
                    "figure_value": round(fig_val, 2)
                })
        gaps.sort(key=lambda x: abs(x["gap"]), reverse=True)

        # Get translated figure name
        names = fig.get("names", {})
        figure_name = names.get(language, names.get("zh", fig.get("name_cn", "")))

        # Get translated figure bio fields
        def get_field(field):
            key = f"{field}_{language}"
            return fig.get(key) or fig.get(field, "")

        # Generate overall suggestion
        from src.api.suggestions import SUGGESTIONS_MAP
        suggestions_map = SUGGESTIONS_MAP.get(language, SUGGESTIONS_MAP["en"])

        overall = generate_overall(figure_name, gaps, language, suggestions_map)

        results.append({
            "figure": fig,
            "similarity": sim,
            "distance": round(weighted_distance(user_vec, fig_vec), 3),
            "suggestion": {
                "figure_name": figure_name,
                "names": names,
                "era": fig.get("era", ""),
                "type": fig.get("type", ""),
                "early_career": get_field("early_career"),
                "early_actions": get_field("early_actions"),
                "breakthrough": get_field("breakthrough"),
                "key_lesson": get_field("key_lesson"),
                "gaps": gaps,
                "overall": overall,
                "radar": {
                    "user": [user_vec.get(d, 0) for d in DIMENSIONS],
                    "figure": [fig_vec.get(d, 0) for d in DIMENSIONS]
                }
            }
        })

    results.sort(key=lambda x: x["similarity"], reverse=True)
    return {"matches": results[:top_n], "total": len(results)}

def generate_overall(figure_name, gaps, language, suggestions_map):
    """Generate overall suggestion text in the specified language."""
    if not gaps:
        templates = {
            "zh": f"你与{figure_name}高度匹配！",
            "en": f"You match well with {figure_name}!",
            "ja": f"{figure_name}とよく似ています！",
            "es": f"¡Coincides mucho con {figure_name}!",
            "de": f"Sie ähneln stark {figure_name}!",
            "ru": f"Вы очень похожи на {figure_name}!",
            "fr": f"Vous correspondez bien à {figure_name}!",
            "ko": f"{figure_name}과 많이 유사합니다!"
        }
        return templates.get(language, templates["en"])

    first = gaps[0]
    trait = first["trait"]
    direction = first["direction"]
    dim_name = first["dimension"]

    trait_suggestions = suggestions_map.get(trait, {}).get(direction, [])
    suggestion_text = "，".join(trait_suggestions[:2]) if trait_suggestions else ""

    templates = {
        "zh": f"你与{figure_name}的差距主要集中在{dim_name}维度，建议：{suggestion_text}",
        "en": f"Your main gap with {figure_name} is in {dim_name}, suggested: {suggestion_text}",
        "es": f"Tu principal diferencia con {figure_name} está en {dim_name}, sugerido: {suggestion_text}",
        "ja": f"{figure_name}との主なギャップは{dim_name}です。提案：{suggestion_text}",
        "de": f"Ihre Hauptlücke mit {figure_name} ist in {dim_name}, empfohlen: {suggestion_text}",
        "ru": f"Ваша основная разница с {figure_name} в {dim_name}, рекомендуется: {suggestion_text}",
        "fr": f"Votre principale différence avec {figure_name} est dans {dim_name}, suggéré: {suggestion_text}",
        "ko": f"{figure_name}와의 주요 차이는 {dim_name}입니다. 권장사항: {suggestion_text}"
    }

    return templates.get(language, templates["en"])
