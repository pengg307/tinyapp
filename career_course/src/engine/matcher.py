import json
import math
from pathlib import Path

DIMENSIONS = [
    "openness","conscientiousness","extraversion","agreeableness","neuroticism",
    "leadership","risk_taking","rationality","discipline","empathy","ambition","resilience"
]

# 维度权重：核心职业能力维度更高权重
WEIGHTS = {
    "openness":1.0,"conscientiousness":1.2,"extraversion":0.9,"agreeableness":0.9,
    "neuroticism":0.8,"leadership":1.3,"risk_taking":0.9,"rationality":1.3,
    "discipline":1.2,"empathy":0.8,"ambition":1.1,"resilience":1.1
}

DATA_DIR = Path(__file__).parent.parent / "data"

def load_figures():
    with open(DATA_DIR / "figures.json", "r", encoding="utf-8") as f:
        return json.load(f)["figures"]

def load_questions():
    with open(DATA_DIR / "questions.json", "r", encoding="utf-8") as f:
        return json.load(f)["questions"]

def calculate_user_vector(answers):
    dims = {d: 0.0 for d in DIMENSIONS}
    counts = {d: 0 for d in DIMENSIONS}
    q_map = {q["id"]: q for q in load_questions()}
    for ans in answers:
        qid = ans.get("question_id")
        q = q_map.get(qid, {})
        opts = q.get("options", [])
        if not opts:
            continue
        idx = max(0, min(len(opts) - 1, ans.get("option_index", 0)))
        opt = opts[idx]
        for d, val in opt.get("values", {}).items():
            if d in dims:
                dims[d] += val
                counts[d] += 1
    for d in dims:
        dims[d] = dims[d] / max(counts[d], 1)
    for d in dims:
        dims[d] = max(0.05, min(0.95, dims[d]))
    return dims

def is_real_figure(fig):
    real_ids = {
        "newton", "einstein", "tesla", "galileo", "mozart", "shakespeare",
        "curie", "lincoln", "steve_jobs", "elon_musk", "mark_zuckerberg",
        "bill_gates", "warren_buffett", "edison", "freud", "darwin",
        "pasteur", "ada_lovelace", "florence_nightingale", "helen_keller"
    }
    return fig.get("id") in real_ids

def weighted_distance(v1, v2):
    s = 0.0
    for d in DIMENSIONS:
        diff = (v1.get(d, 0) - v2.get(d, 0)) ** 2
        s += WEIGHTS[d] * diff
    return math.sqrt(s)

def similarity_score(user_vec, fig_vec, is_real=False):
    dist = weighted_distance(user_vec, fig_vec)
    norm_dist = dist / 2.0
    base_sim = math.exp(-norm_dist)
    if is_real:
        bonus = 0.08 + 0.04 * max(0, 1 - dist / 1.5)
        base_sim = min(0.98, base_sim + bonus)
    big_gap = sum(1 for d in DIMENSIONS if abs(user_vec.get(d, 0) - fig_vec.get(d, 0)) > 0.6)
    if big_gap >= 3:
        base_sim *= 0.92
    return round(base_sim, 3)

def match_user(answers, top_n=10):
    user_vec = calculate_user_vector(answers)
    figures = load_figures()
    results = []
    for fig in figures:
        sim = similarity_score(user_vec, fig["vector"], is_real=is_real_figure(fig))
        results.append({
            "figure": fig,
            "similarity": sim,
            "distance": round(weighted_distance(user_vec, fig["vector"]), 3),
            "radar": {
                "dimensions": DIMENSIONS,
                "user": [round(user_vec[d], 2) for d in DIMENSIONS],
                "figure": [round(fig["vector"].get(d, 0), 2) for d in DIMENSIONS]
            }
        })
    results.sort(key=lambda x: -x["similarity"])
    top = results[:top_n]
    for r in top:
        r["suggestion"] = generate_suggestion(r, user_vec)
    return {"user_vector": user_vec, "matches": top}

def generate_suggestion(match_result, user_vec):
    fig = match_result["figure"]
    gaps = []
    for d in DIMENSIONS:
        u = user_vec.get(d, 0)
        f = fig["vector"].get(d, 0)
        diff = round(abs(u - f), 2)
        if diff > 0.15:
            direction = "develop" if f > u else "leverage"
            gaps.append({
                "dimension": d,
                "user_value": round(u, 2),
                "figure_value": round(f, 2),
                "difference": diff,
                "direction": direction
            })
    gaps.sort(key=lambda x: -x["difference"])
    overall = f"Your career profile is most similar to {fig['name_cn']} ({fig['name']}, {fig['era']})."
    return {
        "figure_name": fig["name_cn"],
        "figure_name_en": fig["name"],
        "era": fig["era"],
        "type": fig["type"],
        "early_career": fig.get("early_career", ""),
        "early_actions": fig.get("early_actions", ""),
        "breakthrough": fig.get("breakthrough", ""),
        "key_lesson": fig.get("key_lesson", ""),
        "gaps": gaps[:6],
        "overall": overall,
        "radar": match_result.get("radar")
    }
