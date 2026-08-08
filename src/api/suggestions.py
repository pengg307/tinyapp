"""建议生成模块：基于维度差距生成改进建议"""

from __future__ import annotations
from typing import Any

# 每个维度的改进建议模板
SUGGESTION_TEMPLATES = {
    "openness": {
        "low_to_high": [
            "尝试每周接触一种新事物：新的音乐类型、新菜肴、新爱好",
            "阅读不同领域的书籍，拓宽知识面",
            "练习创造性思维：每天写500字随笔或绘画",
            "旅行到陌生地方，体验不同文化",
            "参加创意工作坊或艺术课程"
        ],
        "high_to_low": [
            "学习聚焦与执行：设定明确的短期目标",
            "培养坚持完成一件事的习惯",
            "在实践中验证想法，避免空想",
            "学习时间管理和任务优先级排序"
        ]
    },
    "conscientiousness": {
        "low_to_high": [
            "制定每日计划，使用待办清单工具",
            "设定 SMART 目标（具体、可衡量、可达成、相关、有时限）",
            "培养整理习惯：每天整理 workspace 10分钟",
            "使用日历提醒重要事项",
            "分解大任务为小步骤，逐步完成"
        ],
        "high_to_low": [
            "学会灵活变通，接受不完美",
            "给生活留白，不要过度规划",
            "尝试即兴活动：没有计划的周末",
            "学会说'差不多就行了'"
        ]
    },
    "extraversion": {
        "low_to_high": [
            "每周参加一次社交活动：聚会、沙龙、兴趣小组",
            "主动与同事/同学打招呼、聊天",
            "练习公开表达：参加读书会分享",
            "从一对一深聊开始，逐步扩展社交圈",
            "志愿服务：在帮助他人中建立连接"
        ],
        "high_to_low": [
            "培养独处能力：享受安静时光",
            "练习深度倾听而非急于表达",
            "减少社交媒体的碎片化互动",
            "每天留出30分钟独立思考时间"
        ]
    },
    "agreeableness": {
        "low_to_high": [
            "练习换位思考：每天理解一个不同立场的人",
            "学会说'我理解你的感受'",
            "参与团队协作项目，培养合作精神",
            "减少批评，增加建设性反馈",
            "练习感恩：每天记录3件感激的事"
        ],
        "high_to_low": [
            "学会设立边界：勇敢说'不'",
            "在重要事务上坚持自己的观点",
            "竞争也是成长的动力，适度参与",
            "不必过度考虑他人意见而委屈自己"
        ]
    },
    "emotional_stability": {
        "low_to_high": [
            "练习正念冥想：每天10分钟呼吸冥想",
            "建立情绪日记：记录触发情绪的事件",
            "学习认知重构：质疑消极想法",
            "保证充足睡眠，规律运动",
            "找到情绪出口：运动、写作、音乐"
        ],
        "high_to_low": [
            "不要压抑情绪，允许自己感受",
            "与信任的人分享内心感受",
            "学习表达脆弱，这也是力量",
            "偶尔'失控'也能释放压力"
        ]
    },
    "leadership": {
        "low_to_high": [
            "主动承担项目负责人的角色",
            "练习决策：在小事务上快速做决定",
            "学习领导力课程：如《高效能人士的七个习惯》",
            "在团队中提出想法并推动执行",
            "寻找导师，学习领导艺术"
        ],
        "high_to_low": [
            "学会授权：信任他人完成任务",
            "培养协作型领导风格",
            "倾听团队成员的意见",
            "领导不一定要强势"
        ]
    },
    "risk_taking": {
        "low_to_high": [
            "从小风险开始：尝试新的工作方式",
            "设定'风险预算'：每月做一件超出舒适区的事",
            "学习风险管理而非逃避风险",
            "投资学习：接触金融、创业等高风险高回报领域",
            "问自己：最坏的情况是什么？能接受吗？"
        ],
        "high_to_low": [
            "学会评估风险：计算概率与收益",
            "在重要决策前咨询他人意见",
            "设置止损点：知道何时该放弃",
            "长期主义：考虑10年后的结果"
        ]
    },
    "rationality": {
        "low_to_high": [
            "学习批判性思维：区分事实与观点",
            "做决策前列出利弊清单",
            "阅读逻辑学入门：如《思考，快与慢》",
            "练习数据驱动决策",
            "遇到问题先问'为什么'5次"
        ],
        "high_to_low": [
            "信任直觉：有时数据无法告诉你一切",
            "学会感受而非分析",
            "艺术表达：绘画、音乐、写作",
            "与感性的人交流，学习情感语言"
        ]
    },
    "discipline": {
        "low_to_high": [
            "建立晨间例行：固定时间起床、运动、学习",
            "使用番茄工作法：25分钟专注+5分钟休息",
            "删除干扰源：手机静音、清理桌面",
            "设定'不可商量'的时间块",
            "追踪习惯：连续打卡30天"
        ],
        "high_to_low": [
            "偶尔打破规律，体验 spontaneity",
            "不要过度自律导致 burnout",
            "学会享受当下，而非总是追求目标",
            "给'浪费'时间一点空间"
        ]
    },
    "empathy": {
        "low_to_high": [
            "练习积极倾听：不打断、不评判",
            "阅读文学作品：体验不同人物内心",
            "志愿服务：接触不同背景的人",
            "问他人：'你当时是什么感受？'",
            "观察非语言信号：表情、肢体、语调"
        ],
        "high_to_low": [
            "学会情绪隔离：不要过度承担他人情绪",
            "保持理性判断，不被情绪左右",
            "设立情感边界：理解不等于认同",
            "保护自己的能量"
        ]
    },
    "ambition": {
        "low_to_high": [
            "设定3年人生愿景：你想成为什么样的人",
            "寻找榜样：研究成功人士的成长路径",
            "建立目标体系：年度→季度→月度→周度",
            "投资自己：学习高价值技能",
            "主动争取机会：不要等待被看见"
        ],
        "high_to_low": [
            "学会知足：欣赏已有的一切",
            "定义自己的成功，而非社会标准",
            "享受过程而非只关注结果",
            "偶尔'躺平'也是智慧"
        ]
    },
    "resilience": {
        "low_to_high": [
            "回顾过去：列出你克服的5个困难",
            "建立支持系统：亲友、导师、社群",
            "练习成长型思维：失败是学习机会",
            "每日小挑战：逐步提升抗压能力",
            "学习逆境故事：阅读人物传记"
        ],
        "high_to_low": [
            "承认脆弱：不需要总是坚强",
            "学会求助：这不是软弱",
            "给自己休息的时间",
            "韧性不等于永远正能量"
        ]
    },
    "independence": {
        "low_to_high": [
            "独自在外旅行：没有计划地探索",
            "独立做决策：减少征求他人意见",
            "培养独处的能力：享受一个人做事",
            "建立个人原则：知道什么不可妥协",
            "尝试自由职业或创业"
        ],
        "high_to_low": [
            "学会合作：团队力量大于个人",
            "听取他人建议：他人视角有价值",
            "建立深度关系：依赖也是连接",
            "不要孤立自己"
        ]
    }
}

# 维度中文名映射
TRAIT_CN_MAP = {
    "openness": "开放性",
    "conscientiousness": "尽责性",
    "extraversion": "外向性",
    "agreeableness": "宜人性",
    "emotional_stability": "情绪稳定性",
    "leadership": "领导力",
    "risk_taking": "风险偏好",
    "idealism": "理想主义",
    "rationality": "理性度",
    "discipline": "自律性",
    "empathy": "共情力",
    "ambition": "野心",
    "resilience": "韧性",
    "independence": "独立性"
}


def generate_suggestions(
    gaps: list[dict[str, Any]],
    figure_name: str,
    figure_bio: str = "",
) -> dict[str, Any]:
    """
    根据维度差距生成改进建议。

    Parameters
    ----------
    gaps : list[dict]
        维度差距列表，每项包含 trait, user, figure, diff
    figure_name : str
        历史人物名称
    figure_bio : str
        历史人物简介

    Returns
    -------
    dict
        包含建议标题、总体评价、各维度建议
    """
    # 总体评价
    positive_gaps = [g for g in gaps if g["gap"] > 0]
    negative_gaps = [g for g in gaps if g["gap"] < 0]
    
    # 主要差距维度（按差距绝对值排序，取前3）
    top_gaps = sorted(gaps, key=lambda x: abs(x["gap"]), reverse=True)[:3]
    
    # 生成建议
    suggestions = []
    for gap in top_gaps:
        trait = gap["trait"]
        direction = gap["gap"]
        
        if trait in SUGGESTION_TEMPLATES:
            templates = SUGGESTION_TEMPLATES[trait]
            # diff > 0: 用户高于人物，建议向人物学习（降低该维度）
            # diff < 0: 用户低于人物，建议提升该维度
            if direction > 0:
                # 用户更高，建议适当降低
                tips = templates.get("high_to_low", [])
            else:
                # 用户更低，建议提升
                tips = templates.get("low_to_high", [])
            
            if tips:
                suggestions.append({
                    "trait": trait,
                    "trait_cn": TRAIT_CN_MAP.get(trait, trait),
                    "direction": "提升" if direction < 0 else "调整",
                    "tips": tips[:3],  # 取前3条建议
                    "gap_value": round(abs(direction), 2)
                })
    
    # 总体评价
    overall = _generate_overall_evaluation(figure_name, positive_gaps, negative_gaps)
    
    # 摘要
    summary = _generate_summary(figure_name, top_gaps)
    
    return {
        "figure_name": figure_name,
        "figure_bio": figure_bio,
        "overall": overall,
        "suggestions": suggestions,
        "summary": summary
    }


def _generate_overall_evaluation(
    figure_name: str,
    positive_gaps: list,
    negative_gaps: list,
) -> str:
    """生成总体评价"""
    if len(positive_gaps) > len(negative_gaps):
        direction = "整体高于"
        advice = f"你在这些维度上已经很强，可以学习{figure_name}的其他特质"
    elif len(negative_gaps) > len(positive_gaps):
        direction = "整体低于"
        advice = f"你需要在这些方面向{figure_name}学习"
    else:
        direction = "相当均衡"
        advice = f"你与{figure_name}在某些方面相似，某些方面不同"
    
    return f"你与{figure_name}相比{direction}，{advice}。"


def _generate_summary(figure_name: str, top_gaps: list) -> str:
    """生成简洁摘要"""
    if not top_gaps:
        return f"你与{figure_name}非常相似！"
    
    main_gap = top_gaps[0]
    trait_cn = TRAIT_CN_MAP.get(main_gap["trait"], main_gap["trait"])
    
    if main_gap["gap"] > 0:
        return f"你比{figure_name}更{trait_cn}，可以多学习其其他特质"
    else:
        return f"你比{figure_name}少{trait_cn}，建议向{figure_name}学习"
