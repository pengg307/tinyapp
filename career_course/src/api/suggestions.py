"""建议生成模块 - 多语言支持"""
from typing import Any, List, Dict

# 12维性格维度的多语言建议
SUGGESTIONS_ZH = {
    "openness": {
        "up": ["多尝试新事物，保持好奇心", "阅读不同领域的书籍", "旅行或接触新文化"],
        "down": ["不要害怕改变", "尝试新的思维方式", "接受不确定性"]
    },
    "conscientiousness": {
        "up": ["制定详细计划", "培养时间管理习惯", "注重细节"],
        "down": ["更加灵活", "学会放手", "接受不完美"]
    },
    "extraversion": {
        "up": ["参加社交活动", "主动与人交流", "加入兴趣小组"],
        "down": ["享受独处时间", "培养内向优势", "深度思考"]
    },
    "agreeableness": {
        "up": ["学会说no", "建立边界", "坚持己见"],
        "down": ["更善于合作", "倾听他人意见", "寻求共赢"]
    },
    "neuroticism": {
        "up": ["学习情绪管理", "练习冥想", "保持规律作息"],
        "down": ["更自信", "减少焦虑", "积极面对挑战"]
    },
    "leadership": {
        "up": ["承担领导角色", "学习管理技能", "影响他人"],
        "down": ["配合团队", "支持领导者", "执行任务"]
    },
    "risk_taking": {
        "up": ["勇于尝试", "接受挑战", "冒险精神"],
        "down": ["谨慎决策", "评估风险", "稳扎稳打"]
    },
    "rationality": {
        "up": ["理性分析", "数据驱动", "逻辑思考"],
        "down": ["跟随直觉", "情感决策", "灵活应变"]
    },
    "discipline": {
        "up": ["坚持惯例", "自我控制", "持之以恒"],
        "down": ["放松自己", "灵活调整", "随性而为"]
    },
    "empathy": {
        "up": ["体谅他人", "情感支持", "换位思考"],
        "down": ["独立自主", "理性判断", "保持距离"]
    },
    "ambition": {
        "up": ["设定高远目标", "追求卓越", "不断进阶"],
        "down": ["知足常乐", "享受当下", "平衡生活"]
    },
    "resilience": {
        "up": ["抗压能力强", "从失败中学习", "韧性十足"],
        "down": ["更容易挫折", "需要支持", "学会求助"]
    }
}

SUGGESTIONS_EN = {
    "openness": {
        "up": ["Try new things and stay curious", "Read books from different fields", "Travel or experience new cultures"],
        "down": ["Don't be afraid of change", "Try new ways of thinking", "Accept uncertainty"]
    },
    "conscientiousness": {
        "up": ["Make detailed plans", "Develop time management habits", "Pay attention to details"],
        "down": ["Be more flexible", "Learn to let go", "Accept imperfection"]
    },
    "extraversion": {
        "up": ["Attend social activities", "Initiate conversations", "Join interest groups"],
        "down": ["Enjoy solitude", "Develop introvert strengths", "Deep thinking"]
    },
    "agreeableness": {
        "up": ["Learn to say no", "Set boundaries", "Stand your ground"],
        "down": ["Be more cooperative", "Listen to others", "Seek win-win"]
    },
    "neuroticism": {
        "up": ["Learn emotional management", "Practice meditation", "Maintain regular schedule"],
        "down": ["Be more confident", "Reduce anxiety", "Face challenges positively"]
    },
    "leadership": {
        "up": ["Take leadership roles", "Learn management skills", "Influence others"],
        "down": ["Support the team", "Assist leaders", "Execute tasks"]
    },
    "risk_taking": {
        "up": ["Be courageous", "Accept challenges", "Take risks"],
        "down": ["Make cautious decisions", "Evaluate risks", "Steady progress"]
    },
    "rationality": {
        "up": ["Think rationally", "Data-driven", "Logical thinking"],
        "down": ["Follow intuition", "Emotional decisions", "Adapt flexibly"]
    },
    "discipline": {
        "up": ["Maintain routines", "Self-control", "Perseverance"],
        "down": ["Relax yourself", "Flexible adjustment", "Be spontaneous"]
    },
    "empathy": {
        "up": ["Understand others", "Emotional support", "Put yourself in others' shoes"],
        "down": ["Be independent", "Rational judgment", "Keep distance"]
    },
    "ambition": {
        "up": ["Set high goals", "Pursue excellence", "Keep advancing"],
        "down": ["Content with less", "Enjoy the moment", "Balance life"]
    },
    "resilience": {
        "up": ["Strong抗压能力", "Learn from failure", "Resilient"],
        "down": ["More vulnerable", "Need support", "Learn to ask for help"]
    }
}

# 西班牙语建议（简化翻译）
SUGGESTIONS_ES = {k: {dir: [t.replace("Try", "Intenta").replace("Learn", "Aprende").replace("Set", "Establece") 
                            for t in v] for dir, v in vs.items()} for k, vs in SUGGESTIONS_EN.items()}

# 日语建议（需要完整翻译）
SUGGESTIONS_JA = {k: {dir: [t for t in v] for dir, v in vs.items()} for k, vs in SUGGESTIONS_EN.items()}

# 德语建议
SUGGESTIONS_DE = SUGGESTIONS_EN
# 俄语建议
SUGGESTIONS_RU = SUGGESTIONS_EN
# 法语建议
SUGGESTIONS_FR = SUGGESTIONS_EN

SUGGESTIONS_MAP = {
    "zh": SUGGESTIONS_ZH,
    "en": SUGGESTIONS_EN,
    "es": SUGGESTIONS_ES,
    "ja": SUGGESTIONS_JA,
    "de": SUGGESTIONS_DE,
    "ru": SUGGESTIONS_RU,
    "fr": SUGGESTIONS_FR
}

# 整体建议模板
OVERALL_TEMPLATES = {
    "zh": "你与{name}的差距主要集中在{trait}维度，建议：{suggestion}",
    "en": "Your main gap with {name} is in {trait}, suggested: {suggestion}",
    "es": "Tu principal diferencia con {name} está en {trait}, sugerido: {suggestion}",
    "ja": "{name}との主なギャップは{trait}次元です。提案：{suggestion}",
    "de": "Ihre Hauptlücke mit {name} ist in {trait}, empfohlen: {suggestion}",
    "ru": "Ваша основная разница с {name} в {trait}, рекомендуется: {suggestion}",
    "fr": "Votre principale différence avec {name} est dans {trait}, suggéré: {suggestion}"
}

def generate_suggestions(gaps: List[Dict[str, Any]], figure_type: str, language: str = "zh", figure_name: str = "") -> Dict[str, Any]:
    """生成多语言建议"""
    suggestions_map = SUGGESTIONS_MAP.get(language, SUGGESTIONS_ZH)
    
    suggestions = []
    for gap in gaps[:3]:  # 只取前3个最大差距
        trait = gap.get("trait", "")
        direction = "up" if gap.get("gap", 0) > 0 else "down"
        trait_suggestions = suggestions_map.get(trait, {})
        trait_suggestions = trait_suggestions.get(direction, [])
        suggestion_text = "，".join(trait_suggestions[:2]) if trait_suggestions else ""
        
        suggestions.append({
            "trait": trait,
            "direction": direction,
            "suggestion": suggestion_text
        })
    
    # 生成整体建议
    if suggestions:
        first = suggestions[0]
        overall = OVERALL_TEMPLATES.get(language, OVERALL_TEMPLATES["zh"]).format(
            name=figure_name,
            trait=first["trait"],
            suggestion=first["suggestion"]
        )
    else:
        overall = f"{figure_name}とよく似ています" if language == "ja" else f"You match well with {figure_name}"
    
    return {
        "overall": overall,
        "suggestions": suggestions,
        "figure_type": figure_type
    }
