"""Generate 20 quiz questions for CareerCourse."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "src" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

QUESTIONS = [
    {
        "id": 1,
        "question": "面对一个全新且复杂的任务，你的第一反应是？",
        "dimension": "openness",
        "options": [
            {"text": "兴奋，渴望探索和学习", "values": {"openness": 0.9, "conscientiousness": 0.6, "risk_taking": 0.8}},
            {"text": "有些紧张，但愿意尝试", "values": {"openness": 0.6, "conscientiousness": 0.7, "risk_taking": 0.5}},
            {"text": "感到压力，希望有人指导", "values": {"openness": 0.4, "conscientiousness": 0.8, "risk_taking": 0.3}},
            {"text": "退缩，偏好熟悉的事情", "values": {"openness": 0.2, "conscientiousness": 0.9, "risk_taking": 0.2}},
            {"text": "感到焦虑，希望避免", "values": {"openness": 0.1, "conscientiousness": 0.7, "risk_taking": 0.1}}
        ]
    },
    {
        "id": 2,
        "question": "你的工作风格更接近？",
        "dimension": "conscientiousness",
        "options": [
            {"text": "制定详细计划，严格按计划执行", "values": {"conscientiousness": 0.95, "discipline": 0.95}},
            {"text": "有计划但灵活调整", "values": {"conscientiousness": 0.8, "discipline": 0.75}},
            {"text": "有大致方向，随机应变", "values": {"conscientiousness": 0.5, "discipline": 0.5}},
            {"text": "随性而为，不喜欢计划", "values": {"conscientiousness": 0.3, "discipline": 0.3}},
            {"text": "完全没有计划", "values": {"conscientiousness": 0.1, "discipline": 0.1}}
        ]
    },
    {
        "id": 3,
        "question": "在团队中，你更倾向于？",
        "dimension": "extraversion",
        "options": [
            {"text": "领导者，主动承担责任", "values": {"extraversion": 0.9, "leadership": 0.9}},
            {"text": "积极参与讨论和决策", "values": {"extraversion": 0.7, "leadership": 0.6}},
            {"text": "配合他人，完成分配任务", "values": {"extraversion": 0.5, "leadership": 0.4}},
            {"text": "默默工作，不引人注目", "values": {"extraversion": 0.3, "leadership": 0.2}},
            {"text": "避免社交，独自工作", "values": {"extraversion": 0.1, "leadership": 0.1}}
        ]
    },
    {
        "id": 4,
        "question": "面对同事的成功，你的感受是？",
        "dimension": "agreeableness",
        "options": [
            {"text": "真心为他高兴，并从中学习", "values": {"agreeableness": 0.9, "empathy": 0.85}},
            {"text": "高兴但也感到激励", "values": {"agreeableness": 0.7, "empathy": 0.6}},
            {"text": "中性，不太在意", "values": {"agreeableness": 0.5, "empathy": 0.5}},
            {"text": "有些嫉妒，但不承认", "values": {"agreeableness": 0.3, "ambition": 0.7, "neuroticism": 0.6}},
            {"text": "感到威胁，竞争意识强", "values": {"agreeableness": 0.1, "ambition": 0.9, "neuroticism": 0.8}}
        ]
    },
    {
        "id": 5,
        "question": "面对失败时，你通常会？",
        "dimension": "neuroticism",
        "options": [
            {"text": "快速调整，继续前进", "values": {"neuroticism": 0.1, "resilience": 0.95}},
            {"text": "短暂沮丧后恢复", "values": {"neuroticism": 0.3, "resilience": 0.8}},
            {"text": "需要一些时间消化", "values": {"neuroticism": 0.5, "resilience": 0.5}},
            {"text": "长时间受影响", "values": {"neuroticism": 0.7, "resilience": 0.3}},
            {"text": "陷入自责和焦虑", "values": {"neuroticism": 0.95, "resilience": 0.1}}
        ]
    },
    {
        "id": 6,
        "question": "你做决策时更依赖？",
        "dimension": "rationality",
        "options": [
            {"text": "数据和逻辑分析", "values": {"rationality": 0.95, "openness": 0.6}},
            {"text": "数据为主，兼顾直觉", "values": {"rationality": 0.8, "openness": 0.5}},
            {"text": "经验和直觉", "values": {"rationality": 0.5, "openness": 0.6}},
            {"text": "直觉和感受", "values": {"rationality": 0.3, "empathy": 0.7}},
            {"text": "完全凭直觉", "values": {"rationality": 0.1, "openness": 0.8}}
        ]
    },
    {
        "id": 7,
        "question": "你对目标的坚持程度？",
        "dimension": "resilience",
        "options": [
            {"text": "绝不放弃，百折不挠", "values": {"resilience": 0.95, "discipline": 0.9}},
            {"text": "遇到困难也不容易放弃", "values": {"resilience": 0.8, "discipline": 0.75}},
            {"text": "视情况而定", "values": {"resilience": 0.5, "discipline": 0.5}},
            {"text": "遇到困难可能考虑放弃", "values": {"resilience": 0.3, "discipline": 0.3}},
            {"text": "容易妥协", "values": {"resilience": 0.1, "discipline": 0.1}}
        ]
    },
    {
        "id": 8,
        "question": "在职业规划中，你最看重？",
        "dimension": "ambition",
        "options": [
            {"text": "成为领域顶尖，追求成就", "values": {"ambition": 0.95, "leadership": 0.8}},
            {"text": "做出有意义的工作", "values": {"ambition": 0.7, "empathy": 0.8}},
            {"text": "工作与生活平衡", "values": {"ambition": 0.4, "conscientiousness": 0.6}},
            {"text": "稳定安定的生活", "values": {"ambition": 0.2, "conscientiousness": 0.8, "neuroticism": 0.3}},
            {"text": "没有特别追求", "values": {"ambition": 0.1, "conscientiousness": 0.5}}
        ]
    },
    {
        "id": 9,
        "question": "处理冲突时，你的风格是？",
        "dimension": "leadership",
        "options": [
            {"text": "直接面对，积极解决", "values": {"leadership": 0.9, "extraversion": 0.8}},
            {"text": "尝试调和双方意见", "values": {"leadership": 0.6, "agreeableness": 0.7, "empathy": 0.7}},
            {"text": "中立，不站队", "values": {"leadership": 0.4, "agreeableness": 0.5}},
            {"text": "回避冲突", "values": {"leadership": 0.2, "neuroticism": 0.6, "agreeableness": 0.4}},
            {"text": "逃避，不愿面对", "values": {"leadership": 0.1, "neuroticism": 0.8}}
        ]
    },
    {
        "id": 10,
        "question": "面对风险决策，你倾向于？",
        "dimension": "risk_taking",
        "options": [
            {"text": "高风险高回报，敢于冒险", "values": {"risk_taking": 0.95, "ambition": 0.9}},
            {"text": "评估后适度冒险", "values": {"risk_taking": 0.7, "rationality": 0.8}},
            {"text": "保守，偏好稳定", "values": {"risk_taking": 0.4, "conscientiousness": 0.7, "neuroticism": 0.5}},
            {"text": "尽量避免风险", "values": {"risk_taking": 0.2, "conscientiousness": 0.8, "neuroticism": 0.7}},
            {"text": "完全规避风险", "values": {"risk_taking": 0.1, "neuroticism": 0.9}}
        ]
    },
    {
        "id": 11,
        "question": "你如何学习新技能？",
        "dimension": "discipline",
        "options": [
            {"text": "系统学习，制定计划严格执行", "values": {"discipline": 0.95, "conscientiousness": 0.9}},
            {"text": "有计划但可调整", "values": {"discipline": 0.75, "conscientiousness": 0.7}},
            {"text": "根据兴趣灵活学习", "values": {"discipline": 0.5, "openness": 0.7}},
            {"text": "想到什么学什么", "values": {"discipline": 0.3, "openness": 0.8}},
            {"text": "很少主动学习", "values": {"discipline": 0.1, "conscientiousness": 0.3}}
        ]
    },
    {
        "id": 12,
        "question": "你的工作动机主要来自？",
        "dimension": "empathy",
        "options": [
            {"text": "帮助他人，创造社会价值", "values": {"empathy": 0.95, "agreeableness": 0.9}},
            {"text": "实现个人成长和贡献", "values": {"empathy": 0.7, "ambition": 0.7}},
            {"text": "获得认可和成就感", "values": {"empathy": 0.5, "ambition": 0.6}},
            {"text": "经济收入和安全感", "values": {"empathy": 0.3, "conscientiousness": 0.7, "neuroticism": 0.5}},
            {"text": "没有特别动机", "values": {"empathy": 0.1, "ambition": 0.2}}
        ]
    },
    {
        "id": 13,
        "question": "面对批评时，你的反应是？",
        "dimension": "neuroticism",
        "options": [
            {"text": "视为成长机会，虚心接受", "values": {"neuroticism": 0.1, "openness": 0.9, "resilience": 0.9}},
            {"text": "考虑是否有道理", "values": {"neuroticism": 0.3, "rationality": 0.8}},
            {"text": "有些在意，但不想太多", "values": {"neuroticism": 0.5, "agreeableness": 0.5}},
            {"text": "感到受伤，但会消化", "values": {"neuroticism": 0.7, "resilience": 0.4}},
            {"text": "非常生气或沮丧", "values": {"neuroticism": 0.9, "resilience": 0.2, "agreeableness": 0.3}}
        ]
    },
    {
        "id": 14,
        "question": "你的理想工作环境是？",
        "dimension": "extraversion",
        "options": [
            {"text": "充满挑战和变化", "values": {"openness": 0.9, "risk_taking": 0.8, "extraversion": 0.7}},
            {"text": "有明确目标和方向", "values": {"conscientiousness": 0.8, "rationality": 0.7}},
            {"text": "和谐稳定的团队", "values": {"agreeableness": 0.9, "empathy": 0.8}},
            {"text": "安静独立的空间", "values": {"extraversion": 0.2, "conscientiousness": 0.6}},
            {"text": "完全没有压力", "values": {"extraversion": 0.1, "neuroticism": 0.7}}
        ]
    },
    {
        "id": 15,
        "question": "对于未来，你更倾向于？",
        "dimension": "ambition",
        "options": [
            {"text": "积极规划，雄心勃勃", "values": {"ambition": 0.95, "resilience": 0.8, "discipline": 0.85}},
            {"text": "有计划但会调整", "values": {"ambition": 0.7, "discipline": 0.7}},
            {"text": "走一步看一步", "values": {"ambition": 0.4, "openness": 0.6}},
            {"text": "不太关注未来", "values": {"ambition": 0.2, "neuroticism": 0.5}},
            {"text": "担心未来太多", "values": {"ambition": 0.1, "neuroticism": 0.9}}
        ]
    },
    {
        "id": 16,
        "question": "你更擅长？",
        "dimension": "rationality",
        "options": [
            {"text": "逻辑分析和解决问题", "values": {"rationality": 0.95, "conscientiousness": 0.8}},
            {"text": "技术性和系统性工作", "values": {"rationality": 0.8, "discipline": 0.7}},
            {"text": "创意和发散思维", "values": {"rationality": 0.5, "openness": 0.9}},
            {"text": "人际沟通和协调", "values": {"rationality": 0.4, "empathy": 0.85, "extraversion": 0.7}},
            {"text": "直觉和艺术感受", "values": {"rationality": 0.2, "openness": 0.9, "empathy": 0.7}}
        ]
    },
    {
        "id": 17,
        "question": "在团队中，你的角色偏好？",
        "dimension": "leadership",
        "options": [
            {"text": "领导者，统筹全局", "values": {"leadership": 0.95, "extraversion": 0.8, "ambition": 0.8}},
            {"text": "协调者，推动执行", "values": {"leadership": 0.7, "conscientiousness": 0.8}},
            {"text": "执行者，完成任务", "values": {"leadership": 0.4, "conscientiousness": 0.7, "discipline": 0.7}},
            {"text": "支持者，提供帮助", "values": {"leadership": 0.2, "empathy": 0.85, "agreeableness": 0.8}},
            {"text": "观察者，默默工作", "values": {"leadership": 0.1, "extraversion": 0.2, "conscientiousness": 0.6}}
        ]
    },
    {
        "id": 18,
        "question": "面对困难，你更倾向于？",
        "dimension": "resilience",
        "options": [
            {"text": "迎难而上，坚持到底", "values": {"resilience": 0.95, "ambition": 0.85, "discipline": 0.8}},
            {"text": "寻找替代方案", "values": {"resilience": 0.7, "openness": 0.7, "rationality": 0.7}},
            {"text": "寻求帮助和支持", "values": {"resilience": 0.5, "empathy": 0.7, "agreeableness": 0.6}},
            {"text": "暂时放下，稍后再处理", "values": {"resilience": 0.3, "neuroticism": 0.6}},
            {"text": "放弃或逃避", "values": {"resilience": 0.1, "neuroticism": 0.9, "ambition": 0.2}}
        ]
    },
    {
        "id": 19,
        "question": "你的决策风格更接近？",
        "dimension": "rationality",
        "options": [
            {"text": "完全理性分析", "values": {"rationality": 0.95, "conscientiousness": 0.85}},
            {"text": "数据分析为主", "values": {"rationality": 0.8, "conscientiousness": 0.7}},
            {"text": "综合判断", "values": {"rationality": 0.6, "openness": 0.5, "empathy": 0.5}},
            {"text": "依靠经验和直觉", "values": {"rationality": 0.3, "openness": 0.7, "empathy": 0.6}},
            {"text": "凭感觉行动", "values": {"rationality": 0.1, "openness": 0.9, "risk_taking": 0.8}}
        ]
    },
    {
        "id": 20,
        "question": "你对成功的定义是？",
        "dimension": "ambition",
        "options": [
            {"text": "成就卓越，影响他人", "values": {"ambition": 0.95, "leadership": 0.9, "resilience": 0.85}},
            {"text": "实现个人价值", "values": {"ambition": 0.75, "openness": 0.8}},
            {"text": "获得认可和尊重", "values": {"ambition": 0.55, "extraversion": 0.6}},
            {"text": "生活幸福满足", "values": {"ambition": 0.3, "empathy": 0.7, "agreeableness": 0.7}},
            {"text": "没有特别追求", "values": {"ambition": 0.1, "neuroticism": 0.6}}
        ]
    }
]

with open(DATA_DIR / "questions.json", "w", encoding="utf-8") as f:
    json.dump({"questions": QUESTIONS, "total": len(QUESTIONS)}, f, ensure_ascii=False, indent=2)

print(f"Generated {len(QUESTIONS)} questions")
