"""CareerCourse matching engine - prioritizes real historical figures."""
import json
import math
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).parent.parent.parent / "src" / "data"

def load_figures() -> list[dict]:
    with open(DATA_DIR / "figures.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return data.get("figures", [])

def load_questions() -> list[dict]:
    with open(DATA_DIR / "questions.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return data.get("questions", [])

DIMENSIONS = ["openness", "conscientiousness", "extraversion", "agreeableness",
              "neuroticism", "leadership", "risk_taking", "rationality",
              "discipline", "empathy", "ambition", "resilience"]

def calculate_user_vector(answers: list[dict]) -> dict:
    questions = load_questions()
    q_map = {q['id']: q for q in questions}

    vector = {dim: 0.0 for dim in DIMENSIONS}
    count = 0

    for ans in answers:
        q = q_map.get(ans['question_id'])
        if not q:
            continue

        opt_index = max(0, min(ans['option_index'], len(q['options']) - 1))
        opt = q['options'][opt_index]

        for dim in DIMENSIONS:
            if dim in opt:
                vector[dim] += opt[dim]
        count += 1

    if count > 0:
        for dim in DIMENSIONS:
            vector[dim] /= count

    return vector

def euclidean_distance(v1: dict, v2: dict) -> float:
    return math.sqrt(sum((v1.get(d, 0) - v2.get(d, 0)) ** 2 for d in DIMENSIONS))

def is_real_figure(fig: dict) -> bool:
    """Check if figure is a real historical figure (not generated generic)."""
    real_ids = {"newton", "einstein", "tesla", "galileo", "mozart", "shakespeare",
                "curie", "lincoln", "steve_jobs", "elon_musk", "mark_zuckerberg",
                "bill_gates", "warren_buffett", "edison", "freud", "darwin",
                "pasteur", "ada_lovelace", "florence_nightingale", "helen_keller"}
    return fig.get('id', '') in real_ids

def match_user(answers: list[dict], top_n: int = 10) -> list[dict]:
    figures = load_figures()
    user_vector = calculate_user_vector(answers)

    matches = []
    for fig in figures:
        fig_vector = fig.get('vector', {})
        dist = euclidean_distance(user_vector, fig_vector)
        similarity = 1 - min(dist / math.sqrt(len(DIMENSIONS)), 1.0)

        # Bonus for real historical figures
        if is_real_figure(fig):
            similarity += 0.20

        matches.append({
            'figure': fig,
            'similarity': similarity,
            'user_vector': user_vector
        })

    matches.sort(key=lambda x: x['similarity'], reverse=True)
    return matches[:top_n]

def generate_suggestion(match_result: dict) -> dict:
    fig = match_result['figure']
    user_vec = match_result['user_vector']
    fig_vec = fig['vector']

    gaps = []
    for dim in DIMENSIONS:
        user_val = user_vec.get(dim, 0)
        fig_val = fig_vec.get(dim, 0)
        diff = fig_val - user_val
        if diff > 0.1:
            gaps.append({
                'dimension': dim,
                'user_value': round(user_val, 3),
                'figure_value': round(fig_val, 3),
                'difference': round(diff, 3),
                'direction': 'develop'
            })

    gaps.sort(key=lambda x: x['difference'], reverse=True)

    return {
        'figure_name': fig['name_cn'],
        'figure_name_en': fig['name'],
        'era': fig['era'],
        'type': fig['type'],
        'early_career': fig.get('early_career', ''),
        'early_actions': fig.get('early_actions', ''),
        'breakthrough': fig.get('breakthrough', ''),
        'key_lesson': fig.get('key_lesson', ''),
        'gaps': gaps[:5],
        'overall': f"Your career profile is most similar to {fig['name_cn']} ({fig['era']})."
    }
