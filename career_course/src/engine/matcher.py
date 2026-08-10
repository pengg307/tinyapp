import json
import math
from pathlib import Path

DIMENSIONS = [
    "openness","conscientiousness","extraversion","agreeableness","neuroticism",
    "leadership","risk_taking","rationality","discipline","empathy","ambition","resilience"
]

WEIGHTS = {
    "openness":1.0,"conscientiousness":1.2,"extraversion":0.9,"agreeableness":0.9,
    "neuroticism":0.8,"leadership":1.3,"risk_taking":0.9,"rationality":1.3,
    "discipline":1.2,"empathy":0.8,"ambition":1.1,"resilience":1.1
}

DATA_DIR = Path(__file__).parent.parent / "data"

# 维度名称多语言映射
DIM_NAMES = {
    "zh": {"openness": "开放性", "conscientiousness": "尽责性", "extraversion": "外向性", 
           "agreeableness": "宜人性", "neuroticism": "神经质", "leadership": "领导力",
           "risk_taking": "冒险性", "rationality": "理性", "discipline": "自律性",
           "empathy": "共情力", "ambition": "进取心", "resilience": "坚韧性"},
    "en": {"openness": "Openness", "conscientiousness": "Conscientiousness", "extraversion": "Extraversion",
           "agreeableness": "Agreeableness", "neuroticism": "Neuroticism", "leadership": "Leadership",
           "risk_taking": "Risk Taking", "rationality": "Rationality", "discipline": "Discipline",
           "empathy": "Empathy", "ambition": "Ambition", "resilience": "Resilience"},
    "es": {"openness": "Apertura", "conscientiousness": "Responsabilidad", "extraversion": "Extraversión",
           "agreeableness": "Amabilidad", "neuroticism": "Neuroticismo", "leadership": "Liderazgo",
           "risk_taking": "Toma de Riesgos", "rationality": "Racionalidad", "discipline": "Disciplina",
           "empathy": "Empatía", "ambition": "Ambición", "resilience": "Resiliencia"},
    "ja": {"openness": "開放性", "conscientiousness": "誠実性", "extraversion": "外向性",
           "agreeableness": "協調性", "neuroticism": "神経症性", "leadership": "リーダーシップ",
           "risk_taking": "リスクTaking", "rationality": "合理性", "discipline": "規律",
           "empathy": "共感", "ambition": "野心", "resilience": "回復力"},
}

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

def match_user(answers, top_n=10, language="zh"):
    user_vec = calculate_user_vector(answers)
    figures = load_figures()
    results = []
    
    for fig in figures:
        if not is_real_figure(fig):
            continue
        fig_vec = fig.get("vector", {})
        sim = similarity_score(user_vec, fig_vec, is_real=True)
        gaps = []
        for d in DIMENSIONS:
            user_val = user_vec.get(d, 0.5)
            fig_val = fig_vec.get(d, 0.5)
            gap = round(fig_val - user_val, 2)
            if abs(gap) > 0.15:
                gaps.append({"trait": d, "gap": gap, "direction": "up" if gap > 0 else "down"})
        gaps.sort(key=lambda x: abs(x["gap"]), reverse=True)
        
        # 多语言名字
        names = fig.get("names", {})
        figure_name = names.get(language, names.get("zh", fig.get("name_cn", "")))
        
        results.append({
            "figure": fig,
            "similarity": sim,
            "distance": round(weighted_distance(user_vec, fig_vec), 3),
            "suggestion": {
                "figure_name": figure_name,
                "names": names,
                "era": fig.get("era", ""),
                "type": fig.get("type", ""),
                "early_career": fig.get("early_career", ""),
                "early_actions": fig.get("early_actions", ""),
                "breakthrough": fig.get("breakthrough", ""),
                "key_lesson": fig.get("key_lesson", ""),
                "gaps": gaps,
                "overall": f"{figure_name}との類似度は{int(sim*100)}%です" if language == "ja" else 
                          f"您与{figure_name}的匹配度为 {int(sim*100)}%" if language == "zh" else
                          f"Your match with {figure_name} is {int(sim*100)}%",
                "radar": {
                    "user": [user_vec.get(d, 0) for d in DIMENSIONS],
                    "figure": [fig_vec.get(d, 0) for d in DIMENSIONS]
                }
            }
        })
    
    results.sort(key=lambda x: x["similarity"], reverse=True)
    return {"matches": results[:top_n], "total": len(results)}
