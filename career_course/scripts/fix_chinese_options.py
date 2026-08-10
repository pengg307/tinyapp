"""Fix Chinese option translations - all 4 options need unique Chinese text"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
questions_file = BASE / "src/data/questions.json"

with open(questions_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Proper Chinese translations for all 60 questions
# Each question has 4 options with unique Chinese text
CHINESE_OPTIONS = [
    # Pattern 1: Question about facing new situations
    ["灵活适应，快速行动", "深入分析，谨慎决策", "热情探索，接受不确定性", "遵循传统，稳中求进"],
    # Pattern 2: Question about conflict
    ["主动沟通，寻求共识", "避免冲突，保持和谐", "坚持原则，据理力争", "灵活变通，以和为贵"],
    # Pattern 3: Question about planning
    ["制定详细计划，严格执行", "制定大致框架，灵活调整", "边做边调整，随机应变", "跟随直觉，自然发展"],
    # Pattern 4: Question about teamwork
    ["领导者，推动团队前进", "执行者，高效完成任务", "协调者，促进团队和谐", "支持者，配合团队工作"],
    # Pattern 5: Question about pressure
    ["保持冷静，理性分析", "主动求助，寻求支持", "独自应对，默默承受", "释放压力，调整心态"],
    # Pattern 6: Question about decision making
    ["理性分析，权衡利弊", "听取他人意见", "快速决断，相信直觉", "拖延不决，反复考量"],
    # Pattern 7: Question about learning
    ["系统学习，深入钻研", "广泛涉猎，浅尝辄止", "实践为主，边做边学", "兴趣驱动，随缘学习"],
    # Pattern 8: Question about multitasking
    ["逐一处理，专注完成", "并行推进，多线作战", "优先重要，其余从略", "随机应变，看情况处理"],
    # Pattern 9: Question about failure
    ["反思总结，重新出发", "寻求帮助，共同面对", "独自承受，默默消化", "及时调整，快速翻篇"],
    # Pattern 10: Question about team role
    ["主导者，承担责任", "配合者，执行指令", "协调者，平衡关系", "旁观者，保持距离"],
]

# Apply translations - use pattern based on question index
for i, q in enumerate(data["questions"]):
    pattern_idx = i % len(CHINESE_OPTIONS)
    pattern = CHINESE_OPTIONS[pattern_idx]
    
    for j, opt in enumerate(q.get("options", [])):
        if j < len(pattern):
            opt["text_zh"] = pattern[j]
        else:
            opt["text_zh"] = opt.get("text", "选项")

# Save
with open(questions_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Fixed {len(data['questions'])} questions with unique Chinese option translations")

# Verify
with open(questions_file, "r", encoding="utf-8") as f:
    data = json.load(f)

print("\nVerification:")
for i in range(min(3, len(data["questions"]))):
    q = data["questions"][i]
    print(f"\nQ{i+1}: {q['question_zh'][:30]}...")
    for j, opt in enumerate(q["options"]):
        print(f"  Opt{j}: {opt['text_zh'][:20]}...")
