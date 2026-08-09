"""CareerCourse matching engine - prioritizes real historical figures."""
import json
import math
from pathlib import Path
from typing import Any

# Use the correct path based on project location
DATA_DIR = Path(r"E:\aiprojects\tinyapp\careercourse\src\data")

def load_figures() -> list[dict]:
    with open(DATA_DIR / "figures.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_questions() -> list[dict]:
    with open(DATA_DIR / "questions.json", "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_user_vector(answers: list[dict]) -> dict[str, float]:
    """Calculate user vector from quiz answers."""
    dimensions = ["openness", "conscientiousness", "extraversion", "agreeableness",
                  "neuroticism", "leadership", "risk_taking", "rationality",
                  "discipline", "empathy", "ambition", "resilience"]
    
    user_vector = {dim: 0.0 for dim in dimensions}
    total_weight = 0
    
    questions = load_questions()
    for answer in answers:
        question = next((q for q in questions if q["id"] == answer["question_id"]), None)
        if not question:
            continue
        
        # Add boundary check - clamp to valid range for this question
        max_index = len(question["options"]) - 1
        option_index = max(0, min(answer["option_index"], max_index))
        option = question["options"][option_index]
        opt_vector = option.get("vector", {})
        
        for dim in dimensions:
            if dim in opt_vector:
                user_vector[dim] += opt_vector[dim]
                total_weight += 1
    
    if total_weight > 0:
        for dim in dimensions:
            user_vector[dim] = round(user_vector[dim] / total_weight, 4)
    
    return user_vector

def euclidean_distance(v1: dict, v2: dict) -> float:
    """Calculate Euclidean distance between two vectors."""
    dimensions = ["openness", "conscientiousness", "extraversion", "agreeableness",
                  "neuroticism", "leadership", "risk_taking", "rationality",
                  "discipline", "empathy", "ambition", "resilience"]
    
    distance = 0.0
    for dim in dimensions:
        diff = v1.get(dim, 0) - v2.get(dim, 0)
        distance += diff * diff
    
    return math.sqrt(distance)

def match_user(answers: list[dict], top_n: int = 10) -> list[dict]:
    """Match user answers to historical figures."""
    user_vector = calculate_user_vector(answers)
    figures = load_figures()
    
    # Separate real and generic figures
    real_figures = [f for f in figures if not f.get("name", "").startswith("History Figure")]
    generic_figures = [f for f in figures if f.get("name", "").startswith("History Figure")]
    
    # Calculate similarity for each figure
    matches = []
    
    # Score real figures with HIGHER weight
    for fig in real_figures:
        fig_vector = fig.get("vector", {})
        distance = euclidean_distance(user_vector, fig_vector)
        similarity = 1 - (distance / math.sqrt(len(user_vector)))
        similarity = max(0, min(1, similarity))
        # Boost real figures by 30% to ensure they show up
        similarity = min(1.0, similarity * 1.3)
        
        matches.append({
            "figure": fig,
            "similarity": similarity,
            "user_vector": user_vector,
            "is_real": True
        })
    
    # Score generic figures
    for fig in generic_figures:
        fig_vector = fig.get("vector", {})
        distance = euclidean_distance(user_vector, fig_vector)
        similarity = 1 - (distance / math.sqrt(len(user_vector)))
        similarity = max(0, min(1, similarity))
        
        matches.append({
            "figure": fig,
            "similarity": similarity,
            "user_vector": user_vector,
            "is_real": False
        })
    
    # Sort by similarity (descending)
    matches.sort(key=lambda x: x["similarity"], reverse=True)
    
    # Get top N
    result = matches[:top_n]
    
    # Ensure at least 70% real figures in result
    real_count = sum(1 for m in result if m.get("is_real", False))
    min_real = max(7, top_n * 7 // 10)  # At least 7 real figures
    
    if real_count < min_real:
        # Replace generic figures with real ones from remaining matches
        real_remaining = [m for m in matches[top_n:] if m.get("is_real", False)]
        generic_in_result = [m for m in result if not m.get("is_real", False)]
        
        needed = min(len(generic_in_result), min_real - real_count)
        for i in range(needed):
            if real_remaining and generic_in_result:
                old_idx = result.index(generic_in_result[i])
                result[old_idx] = real_remaining.pop(0)
    
    return result

def generate_suggestion(match: dict) -> dict:
    """Generate career suggestion based on match."""
    figure = match["figure"]
    user_vector = match["user_vector"]
    fig_vector = figure.get("vector", {})
    
    dimensions = ["openness", "conscientiousness", "extraversion", "agreeableness",
                  "neuroticism", "leadership", "risk_taking", "rationality",
                  "discipline", "empathy", "ambition", "resilience"]
    
    gaps = []
    for dim in dimensions:
        user_val = user_vector.get(dim, 0)
        fig_val = fig_vector.get(dim, 0)
        diff = round(fig_val - user_val, 2)
        
        if abs(diff) > 0.1:
            gaps.append({
                "dimension": dim,
                "user_value": round(user_val, 2),
                "figure_value": round(fig_val, 2),
                "difference": diff,
                "direction": "develop" if diff > 0 else "maintain"
            })
    
    gaps.sort(key=lambda x: abs(x["difference"]), reverse=True)
    
    suggestion = {
        "figure_name": figure["name_cn"],
        "figure_name_en": figure["name"],
        "era": figure["era"],
        "type": figure["type"],
        "early_career": figure.get("early_career", ""),
        "early_actions": figure.get("early_actions", ""),
        "breakthrough": figure.get("breakthrough", ""),
        "key_lesson": figure.get("key_lesson", ""),
        "gaps": gaps,
        "overall": f"Your career profile is most similar to {figure['name_cn']} ({figure['era']}). "
                   f"At a similar stage, {figure['name_cn']} {'did: ' + figure.get('early_actions', '')}"
    }
    
    return suggestion
