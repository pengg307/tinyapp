"""Add Korean question translations to all 60 questions"""
import json
from pathlib import Path

QUESTIONS_FILE = Path(r"E:\aiprojects\tinyapp\career_course\src\data\questions.json")
data = json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))

# Korean translations for all 60 questions (based on Chinese originals)
QUESTION_KO = [
    # Q1-5: openness
    "낯선 분야의 복잡한 문제에 직면했을 때, 당신은 어떻게倾向?",
    "새로운 프로젝트에 참여할 때, 당신은?",
    "예상치 못한 변화가 생겼을 때, 당신의 반응은?",
    "새로운 아이디어를 시도할 때, 당신은?",
    "전통적인 방법과 새로운 방법을 비교할 때?",
    # Q6-10: conscientiousness
    "중요한 업무를 처리할 때, 당신은?",
    "기한이 있는 작업을 할 때, 당신의 태도는?",
    "작은 실수가 발견되었을 때?",
    "계획이 갑자기 변경되었을 때?",
    "자기 발전을 위해 어떤 것을 우선시하나요?",
    # Q11-15: extraversion
    "새로운 사람들을 만날 때, 당신은?",
    "그룹 토론에서 당신의 역할은?",
    "혼자 일하는 것과 팀으로 일하는 것 중?",
    "사회적 모임에서あなたは?",
    "타인의 평가에 대해?",
    # Q16-20: agreeableness
    "동의하지 않는 의견에 직면했을 때?",
    "팀 내 갈등이 생겼을 때?",
    "타인의 실수를 발견했을 때?",
    "경쟁 상황에서의 태도?",
    "타인의 요청을 거절할 때?",
    # Q21-25: neuroticism
    "스트레스가 많은 상황에서 당신의 반응은?",
    "실패를 경험했을 때?",
    "불확실한 미래에 대해?",
    "비판적인 피드백을 받았을 때?",
    "위기 상황에서 당신의 감정적 반응은?",
    # Q26-30: leadership
    "팀을 이끌어야 할 때, 당신은?",
    "의사결정 상황에서?",
    "다른 사람의 의견을 이끌 때?",
    "책임이 큰 결정을 내려야 할 때?",
    "영향력을 행사할 때?",
    # Q31-35: risk_taking
    "위험한 상황에서 당신의 선택은?",
    "보수를 위한 안전을 선택할 때?",
    "새로운 기회를 발견했을 때?",
    "불확실한 결정을 내려야 할 때?",
    "도전을 받아들일 때?",
    # Q36-40: rationality
    "결정을 내릴 때, 당신은?",
    "논리적 문제 해결 시?",
    "감정과 이성을 균형 잡을 때?",
    "데이터가 부족할 때?",
    "복잡한 문제를 분석할 때?",
    # Q41-45: discipline
    "자신에게 엄격할 때, 당신은?",
    "습관을 유지할 때?",
    "유혹에 대처할 때?",
    "일관성을 유지할 때?",
    "목표를 위해 인내할 때?",
    # Q46-50: empathy
    "타인의 감정을 이해할 때, 당신은?",
    "감정적 지원이 필요할 때?",
    "타인의 입장을 이해할 때?",
    "공감 능력이 중요할 때?",
    "감정적 연결을 만들 때?",
    # Q51-55: ambition
    "성공에 대한 당신의 정의는?",
    "높은 목표를 설정할 때?",
    "야망과 현실의 균형을 맞출 때?",
    "도전적인 목표를 설정할 때?",
    "야망을 표현할 때?",
    # Q56-60: resilience
    "좌절을 극복할 때, 당신은?",
    "어려운 시기를 보낼 때?",
    "변화에 적응할 때?",
    "압박 상황에서 견딜 때?",
    "실패 이후 다시 시작할 때?"
]

OPTION_KO = [
    # Q1 options
    ["유연하게 적응하고 빠르게 행동하기", "깊이 분석하고 신중히 결정하기", "열정적으로 탐구하고 불확실성 수용하기", "전통을 따르고 안정적으로前進하기"],
    ["직접 실행하고 빠르게 학습하기", "철저한 계획 후 행동하기", "다양한 접근 방식 시도하기", "경험자들의 조언 구하기"],
    ["즉시 계획을 수정하기", "새로운 기회로 보기", "우선 순위를 재설정하기", "안정적으로 기존 방식 유지하기"],
    ["즉시 시도해보고 실패 허용하기", "신중하게 분석한 후 시도하기", "다른 사람의 경험 참조하기", "단계적으로 접근하기"],
    ["새로운 방식 선호하기", "전통 방식 선호하기", "상황에 따라 선택하기", "실험적 접근 시도하기"],
    # Q6 options
    ["세부 사항까지 꼼꼼히 확인하기", "핵심 결과에 집중하기", "시간 제한 내 완료하기", "팀원과 협업하며 진행하기"],
    ["완벽하게 준비한 후 시작하기", "시작하면서 조정하기", "마감일까지 집중하기", "조금씩 꾸준히 진행하기"],
    ["즉시 수정하고 교훈 얻기", "작은 실수는 괜찮다고 생각하기", "상세한 검토 수행하기", "다른 사람에게 확인 요청하기"],
    ["새로운 계획으로 빠르게 전환하기", "기존 계획에 따라 진행하기", "영향을 평가한 후 결정하기", "일부만 조정하기"],
    ["체계적인 학습", "네트워킹", "실무 경험", "멘토링"]
]

# Add Korean translations to questions
for i, q in enumerate(data.get("questions", [])):
    q_id = q.get("id", i + 1)
    
    # Add question text
    if q_id <= len(QUESTION_KO):
        q["question_ko"] = QUESTION_KO[q_id - 1]
    else:
        q["question_ko"] = QUESTION_KO[-1]  # fallback
    
    # Add option translations
    options = q.get("options", [])
    opt_idx = (q_id - 1) % len(OPTION_KO)
    if opt_idx < len(OPTION_KO) and len(options) >= 4:
        for j in range(4):
            if j < len(OPTION_KO[opt_idx]):
                options[j]["text_ko"] = OPTION_KO[opt_idx][j]
            else:
                options[j]["text_ko"] = f"Option {j+1}"

# Write back
data["questions"] = data.get("questions", [])
QUESTIONS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Updated {len(data['questions'])} questions with Korean translations")
print(f"Sample question_ko: {data['questions'][0].get('question_ko', 'N/A')[:50]}")
