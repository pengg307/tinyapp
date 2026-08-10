import json
import random
from pathlib import Path

DIMENSIONS = [
    "openness","conscientiousness","extraversion","agreeableness","neuroticism",
    "leadership","risk_taking","rationality","discipline","empathy","ambition","resilience"
]

# 每维度5题，共60题；每题主维度固定，附带1-2个关联维度
TEMPLATES = [
    {"q":"面对陌生领域的复杂问题，你倾向于？","main":"openness","sec":["conscientiousness","risk_taking"]},
    {"q":"执行长期计划时，你更看重？","main":"conscientiousness","sec":["discipline","rationality"]},
    {"q":"在团队中，你通常的角色是？","main":"extraversion","sec":["leadership","agreeableness"]},
    {"q":"与他人意见冲突时，你会？","main":"agreeableness","sec":["empathy","neuroticism"]},
    {"q":"面对压力和挫败时，你的情绪反应？","main":"neuroticism","sec":["resilience","discipline"]},
    {"q":"需要做出重大决策时，你依赖？","main":"leadership","sec":["rationality","ambition"]},
    {"q":"面对不确定性，你愿意承担多大风险？","main":"risk_taking","sec":["openness","ambition"]},
    {"q":"做决定时，逻辑与数据对你重要吗？","main":"rationality","sec":["conscientiousness","discipline"]},
    {"q":"在没有监督的情况下，你能否坚持目标？","main":"discipline","sec":["resilience","conscientiousness"]},
    {"q":"理解他人情绪与需求对你来说？","main":"empathy","sec":["agreeableness","extraversion"]},
    {"q":"你对成就与地位的追求程度？","main":"ambition","sec":["leadership","discipline"]},
    {"q":"遭遇失败后，你恢复并继续前行的能力？","main":"resilience","sec":["neuroticism","discipline"]},
]

def build_options(main, sec):
    base = {
        "openness": [0.9,0.5,0.2,0.4], "conscientiousness":[0.7,0.3,0.9,0.8],
        "extraversion":[0.8,0.3,0.5,0.7], "agreeableness":[0.9,0.4,0.3,0.7],
        "neuroticism":[0.2,0.7,0.4,0.3], "leadership":[0.9,0.4,0.6,0.3],
        "risk_taking":[0.9,0.3,0.5,0.7], "rationality":[0.9,0.4,0.7,0.5],
        "discipline":[0.9,0.4,0.6,0.3], "empathy":[0.9,0.3,0.6,0.8],
        "ambition":[0.9,0.4,0.7,0.5], "resilience":[0.9,0.3,0.7,0.5],
    }
    opts = []
    patterns = [
        {main:0.9, sec[0]:0.8, sec[1] if len(sec)>1 else sec[0]:0.5},
        {main:0.6, sec[0]:0.7, sec[1] if len(sec)>1 else sec[0]:0.4},
        {main:0.3, sec[0]:0.4, sec[1] if len(sec)>1 else sec[0]:0.8},
        {main:0.7, sec[0]:0.5, sec[1] if len(sec)>1 else sec[0]:0.9},
    ]
    for pat in patterns:
        values = {d:0.5 for d in DIMENSIONS}
        for k,v in pat.items():
            values[k] = v
        others = [d for d in DIMENSIONS if d not in pat]
        for i,o in enumerate(others):
            values[o] = 0.4 + (i%3)*0.15
        texts = [
            "热情探索，接受不确定性",
            "稳健分析，按部就班",
            "谨慎保守，依赖已有经验",
            "灵活适应，快速行动"
        ]
        opts.append({"text": random.choice(texts), "values": {k:round(values[k],2) for k in DIMENSIONS if values[k]!=0.5 or k in pat}})
    for o in opts:
        for d in DIMENSIONS:
            if d not in o["values"]:
                o["values"][d] = 0.5
    return opts

def main():
    Path("src/data").mkdir(parents=True, exist_ok=True)
    questions = []
    for i in range(60):
        t = TEMPLATES[i % len(TEMPLATES)]
        questions.append({
            "id": i+1,
            "question": f"{t['q']}（第{i+1}题）",
            "dimension": t["main"],
            "options": build_options(t["main"], t["sec"])
        })
    with open("src/data/questions.json","w",encoding="utf-8") as f:
        json.dump({"questions": questions, "total": len(questions)}, f, ensure_ascii=False, indent=2)
    print(f"Generated {len(questions)} questions.")

if __name__ == "__main__":
    main()
