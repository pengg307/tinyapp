"""建议生成模块 - 根据维度差距生成改进建议（多语言支持）"""
from typing import Any

# 12维性格维度的多语言建议
SUGGESTIONS_ZH = {
    "openness": {
        "up": ["多尝试新事物，保持好奇心", "阅读不同领域的书籍", "旅行或接触新文化"],
        "down": ["不要害怕改变", "尝试每天做一件新的事", "参加新的社交活动"]
    },
    "conscientiousness": {
        "up": ["制定清晰的计划", "设置目标和截止日期", "保持良好的工作习惯"],
        "down": ["提高自律性", "使用时间管理工具", "制定每日待办清单"]
    },
    "extraversion": {
        "up": ["多参加社交活动", "主动与他人交流", "加入兴趣小组"],
        "down": ["练习在人群中表达自己", "从小型社交活动开始", "培养开放的心态"]
    },
    "agreeableness": {
        "up": ["学会倾听他人观点", "培养同理心", "在冲突中寻求共赢"],
        "down": ["学会说'不'", "设立个人边界", "在坚持自我与妥协间平衡"]
    },
    "neuroticism": {
        "up": ["学习情绪管理技巧", "练习冥想或正念", "培养稳定的情绪"],
        "down": ["减少焦虑和担忧", "寻找健康的压力释放方式", "保持积极乐观的心态"]
    },
    "leadership": {
        "up": ["承担更多领导责任", "学习团队管理技巧", "培养决策能力"],
        "down": ["从小事开始展现领导力", "主动承担责任", "学习有效沟通"]
    },
    "risk_taking": {
        "up": ["评估风险后勇敢尝试", "学习风险管理技巧", "在安全范围内冒险"],
        "down": ["不要因为恐惧而止步", "尝试新挑战", "计算风险后采取行动"]
    },
    "rationality": {
        "up": ["提高分析问题的能力", "学习批判性思维", "收集更多数据再决策"],
        "down": ["用数据支持决策", "避免情绪化判断", "学习逻辑推理"]
    },
    "discipline": {
        "up": ["培养良好的生活习惯", "设定每日规则", "坚持长期目标"],
        "down": ["增强自控能力", "建立日常惯例", "克服拖延习惯"]
    },
    "empathy": {
        "up": ["学习理解他人感受", "培养同理心", "关注他人需求"],
        "down": ["学会站在他人角度思考", "多倾听他人故事", "培养对他人的关怀"]
    },
    "ambition": {
        "up": ["设定更高远的目标", "保持进取心", "不断自我挑战"],
        "down": ["明确人生目标", "制定成长计划", "培养积极向上的态度"]
    },
    "resilience": {
        "up": ["从挫折中快速恢复", "培养心理韧性", "将失败视为学习机会"],
        "down": ["学会接受失败", "培养抗压能力", "保持乐观面对困难"]
    }
}

SUGGESTIONS_EN = {
    "openness": {
        "up": ["Try new things and stay curious", "Read books from different fields", "Travel or experience new cultures"],
        "down": ["Don't be afraid of change", "Try doing something new every day", "Join new social activities"]
    },
    "conscientiousness": {
        "up": ["Create clear plans", "Set goals and deadlines", "Maintain good work habits"],
        "down": ["Improve self-discipline", "Use time management tools", "Create daily to-do lists"]
    },
    "extraversion": {
        "up": ["Attend more social events", "Initiate conversations with others", "Join interest groups"],
        "down": ["Practice expressing yourself in groups", "Start with small social gatherings", "Cultivate an open mindset"]
    },
    "agreeableness": {
        "up": ["Learn to listen to others' perspectives", "Cultivate empathy", "Seek win-win in conflicts"],
        "down": ["Learn to say no", "Set personal boundaries", "Balance self-assertion with compromise"]
    },
    "neuroticism": {
        "up": ["Learn emotion management skills", "Practice meditation or mindfulness", "Cultivate emotional stability"],
        "down": ["Reduce anxiety and worry", "Find healthy ways to release stress", "Maintain a positive and optimistic mindset"]
    },
    "leadership": {
        "up": ["Take on more leadership responsibilities", "Learn team management skills", "Develop decision-making ability"],
        "down": ["Show leadership from small things", "Take initiative in responsibility", "Learn effective communication"]
    },
    "risk_taking": {
        "up": ["Take brave action after assessing risks", "Learn risk management skills", "Take risks within safe bounds"],
        "down": ["Don't stop because of fear", "Try new challenges", "Take action after calculating risks"]
    },
    "rationality": {
        "up": ["Improve analytical problem-solving skills", "Learn critical thinking", "Collect more data before deciding"],
        "down": ["Use data to support decisions", "Avoid emotional judgments", "Learn logical reasoning"]
    },
    "discipline": {
        "up": ["Cultivate good living habits", "Set daily rules", "Persist in long-term goals"],
        "down": ["Enhance self-control", "Establish daily routines", "Overcome procrastination"]
    },
    "empathy": {
        "up": ["Learn to understand others' feelings", "Cultivate empathy", "Pay attention to others' needs"],
        "down": ["Learn to think from others' perspectives", "Listen to others' stories more", "Cultivate care for others"]
    },
    "ambition": {
        "up": ["Set higher goals", "Maintain ambition", "Continuously challenge yourself"],
        "down": ["Clarify life goals", "Create growth plans", "Cultivate a positive attitude"]
    },
    "resilience": {
        "up": ["Recover quickly from setbacks", "Cultivate psychological resilience", "View failure as a learning opportunity"],
        "down": ["Learn to accept failure", "Develop stress resistance", "Maintain optimism when facing difficulties"]
    }
}

# 其他语言使用英语作为基础（实际项目中应添加完整翻译）
SUGGESTIONS_ES = {k: {dir: [t.replace("Try", "Intenta").replace("Learn", "Aprende").replace("Set", "Establece") for t in v] for dir, v in vs.items()} for k, vs in SUGGESTIONS_EN.items()}
SUGGESTIONS_JA = SUGGESTIONS_EN  # 日语需要完整翻译
SUGGESTIONS_DE = SUGGESTIONS_EN  # 德语需要完整翻译
SUGGESTIONS_RU = SUGGESTIONS_EN  # 俄语需要完整翻译
SUGGESTIONS_FR = SUGGESTIONS_EN  # 法语需要完整翻译

SUGGESTIONS_MAP = {
    "zh": SUGGESTIONS_ZH,
    "en": SUGGESTIONS_EN,
    "es": SUGGESTIONS_ES,
    "ja": SUGGESTIONS_JA,
    "de": SUGGESTIONS_DE,
    "ru": SUGGESTIONS_RU,
    "fr": SUGGESTIONS_FR
}

# 维度名称的多语言翻译
DIMENSION_NAMES = {
    "zh": {
        "openness": "开放性",
        "conscientiousness": "尽责性",
        "extraversion": "外向性",
        "agreeableness": "宜人性",
        "neuroticism": "情绪稳定性",
        "leadership": "领导力",
        "risk_taking": "风险偏好",
        "rationality": "理性度",
        "discipline": "自律性",
        "empathy": "共情力",
        "ambition": "野心",
        "resilience": "韧性"
    },
    "en": {
        "openness": "Openness",
        "conscientiousness": "Conscientiousness",
        "extraversion": "Extraversion",
        "agreeableness": "Agreeableness",
        "neuroticism": "Emotional Stability",
        "leadership": "Leadership",
        "risk_taking": "Risk Taking",
        "rationality": "Rationality",
        "discipline": "Discipline",
        "empathy": "Empathy",
        "ambition": "Ambition",
        "resilience": "Resilience"
    }
}

def generate_suggestions(gaps: list[dict[str, Any]], figure_type: str, language: str = "zh", figure_name: str = "") -> dict[str, Any]:
    """
    生成改进建议
    
    Args:
        gaps: 维度差距列表
        figure_type: 人物类型
        language: 语言代码 (zh/en/es/ja/de/ru/fr)
        figure_name: 人物名字
    
    Returns:
        建议对象
    """
    suggestions_map = SUGGESTIONS_MAP.get(language, SUGGESTIONS_ZH)
    dim_names = DIMENSION_NAMES.get(language, DIMENSION_NAMES["zh"])
    
    suggestions_list = []
    for gap in gaps[:3]:  # 只显示前3个最大差距
        trait = gap.get("trait", "")
        # gap > 0: 用户值低于人物值，需要"提升"
        # gap < 0: 用户值高于人物值，需要"调整"
        direction = "up" if gap.get("gap", 0) > 0 else "down"
        
        if trait in suggestions_map:
            tips = suggestions_map[trait].get(direction, [])
            suggestions_list.append({
                "trait": trait,
                "trait_cn": dim_names.get(trait, trait),
                "direction": direction,
                "tips": tips[:3],
                "gap_value": round(abs(gap.get("gap", 0)), 2)
            })
    
    # 构建总体评价
    if language == "zh":
        overall = f"你与{figure_name}的差距主要集中在{suggestions_list[0]['trait_cn'] if suggestions_list else '某些'}维度"
    else:
        overall = f"Your main gap with {figure_name} is in {suggestions_list[0]['trait_cn'] if suggestions_list else 'some'} dimension"
    
    return {
        "figure_name": figure_name,
        "overall": overall,
        "suggestions": suggestions_list
    }
