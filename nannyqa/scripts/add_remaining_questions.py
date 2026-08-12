"""Add 10 more hard questions to reach 90 total."""
import json
import os

questions_path = os.path.join(os.path.dirname(__file__), "questions.json")
with open(questions_path, "r", encoding="utf-8") as f:
    questions = json.load(f)

new_id = max(q["id"] for q in questions) + 1

def q(cat, dim, diff, text, opts):
    global new_id
    new_id += 1
    return {
        "id": new_id,
        "category": cat,
        "dimension": dim,
        "difficulty": diff,
        "question_zh": text,
        "scoring_type": "multiple_choice",
        "options": [
            {"text_zh": o["text"], "score": o["score"], "feedback_zh": o.get("fb", "")}
            for o in opts
        ]
    }

# Add 10 more hard questions across categories
questions.append(q("childcare", "fever_handling", "hard",
    "孩子半夜发烧到39度，家里只有你和孩子在，你会怎么处理？",
    [{"text": "先物理降温（温水擦浴、贴退热贴），观察精神状态，必要时喂退烧药，凌晨去急诊", "score": 5, "fb": "正确处理，知道物理降温+观察+及时就医"},
     {"text": "赶紧抱去医院，路上注意保暖", "score": 4, "fb": "正确但可能过于着急，先降温观察一下更好"},
     {"text": "让孩子多盖被子出汗就好", "score": 1, "fb": "错误做法，可能导致高热惊厥"},
     {"text": "不管了，天亮再说", "score": 1, "fb": "延误病情，风险很高"}]))

questions.append(q("childcare", "foreign_object_eye", "hard",
    "孩子眼睛里进了异物（比如沙子），揉眼睛揉得红红的，你会怎么办？",
    [{"text": "不要揉，用生理盐水或干净的水冲洗，如果不行立即就医", "score": 5, "fb": "正确处理，保护眼睛安全"},
     {"text": "帮孩子倒点水冲一下", "score": 3, "fb": "有意识但方法不够专业"},
     {"text": "让孩子揉一揉，揉出来就好了", "score": 1, "fb": "错误做法，可能损伤角膜"},
     {"text": "用纸巾擦一擦", "score": 1, "fb": "可能划伤眼睛"}]))

questions.append(q("safety", "burn_prevention_kitchen2", "hard",
    "做饭的时候锅里的油着火了，你会怎么做？",
    [{"text": "盖上锅盖灭火，关闭燃气，绝对不浇水，备好灭火毯", "score": 5, "fb": "正确灭油火方法，隔绝氧气"},
     {"text": "往锅里倒水", "score": 1, "fb": "极度危险！水遇热油会剧烈飞溅爆炸"},
     {"text": "用扇子扇风", "score": 1, "fb": "增加氧气供应，火势更旺"},
     {"text": "慌了，不知所措", "score": 1, "fb": "缺乏应急知识"}]))

questions.append(q("hygiene", "toilet_disinfection", "hard",
    "卫生间的马桶和地面有异味和污渍，你会怎么清洁？",
    [{"text": "先刷马桶内壁和边缘，然后用消毒液拖地，最后开窗通风", "score": 5, "fb": "清洁顺序科学，消毒到位"},
     {"text": "用洁厕灵刷一刷，拖把拖一下", "score": 3, "fb": "基本清洁，但可能遗漏细节"},
     {"text": "冲水就行，不用太认真", "score": 1, "fb": "卫生意识差"},
     {"text": "让雇主自己来，我只负责表面", "score": 1, "fb": "缺乏责任感"}]))

questions.append(q("cooking", "nutritional_balance", "hard",
    "雇主希望你做的饭营养均衡，但孩子就是不爱吃蔬菜，你会怎么解决？",
    [{"text": "把蔬菜切碎混进肉丸、饺子馅里，或做成蔬菜饼，潜移默化增加摄入", "score": 5, "fb": "巧妙搭配，不强迫，尊重孩子口味"},
     {"text": "做孩子喜欢吃的菜，蔬菜随便放一点", "score": 3, "fb": "有尝试但不够积极"},
     {"text": "随他，不爱吃就不吃", "score": 1, "fb": "忽视营养均衡"},
     {"text": "强迫孩子吃蔬菜，不吃就不准吃饭", "score": 1, "fb": "强迫进食损害亲子关系"}]))

questions.append(q("communication", "handling_angry_employer", "hard",
    "雇主因为孩子的问题对你很生气，当着孩子的面批评你，你会怎么处理？",
    [{"text": "保持冷静，等雇主情绪平稳后私下沟通，解释情况，寻求理解", "score": 5, "fb": "处理得当，维护双方尊严"},
     {"text": "当场解释，但语气要缓和", "score": 3, "fb": "有沟通意识，但时机可能不对"},
     {"text": "忍着，等雇主走了再想办法", "score": 2, "fb": "消极应对，问题可能积累"},
     {"text": "当场争辩，证明自己没错", "score": 1, "fb": "激化矛盾，影响工作关系"}]))

questions.append(q("professionalism", "workplace_gossip", "hard",
    "你在雇主家听到雇主夫妻在吵架，谈论的是家里的经济问题，你会怎么想怎么做？",
    [{"text": "当作没听见，不参与任何讨论，不向任何人透露", "score": 5, "fb": "严守隐私，职业操守优秀"},
     {"text": "听到了但不主动说，别人问就说不知道", "score": 3, "fb": "有一定边界，但不够主动"},
     {"text": "忍不住跟同事说说", "score": 1, "fb": "泄露雇主隐私，严重失德"},
     {"text": "主动给雇主提建议，帮他们解决问题", "score": 1, "fb": "越界行为，不合适"}]))

questions.append(q("elder_care", "dementia_wandering", "hard",
    "老人有阿尔茨海默症，有时候会自己出门找不到回家，你会怎么预防？",
    [{"text": "给老人佩戴身份卡/手环，安装门磁报警器，不在老人面前表现出焦虑", "score": 5, "fb": "多层面防护，专业细致"},
     {"text": "看着老人，不让他出门", "score": 3, "fb": "有一定意识，但过于限制老人自由"},
     {"text": "老人走丢了就报警", "score": 2, "fb": "被动应对，缺乏预防措施"},
     {"text": "随他去，老人年纪大了正常", "score": 1, "fb": "忽视安全风险"}]))

questions.append(q("special", "nanny_medical_emergency", "hard",
    "你在雇主家工作时突然感到头晕恶心，怀疑自己食物中毒，但雇主和孩子都在，你会怎么处理？",
    [{"text": "立即告知雇主自己身体不适，请求协助，如果情况严重立即就医，不等雇主安排", "score": 5, "fb": "及时沟通，自我保护意识强"},
     {"text": "忍一忍，等雇主回来再说", "score": 2, "fb": "延误救治，风险很高"},
     {"text": "偷偷离开，自己去医院", "score": 2, "fb": "不负责任，可能影响雇主家孩子"},
     {"text": "假装没事，继续工作", "score": 1, "fb": "危害自身和雇主家庭安全"}]))

questions.append(q("special", "child_abduction_attempt", "hard",
    "你带孩子在外面玩的时候，有陌生人试图接近孩子说要带孩子去找妈妈，你会怎么做？",
    [{"text": "立即把孩子拉到身边，大声呼救引起周围人注意，必要时报警", "score": 5, "fb": "正确应急反应，保护孩子安全"},
     {"text": "警惕地看着陌生人，不让孩子靠近", "score": 3, "fb": "有意识但反应不够果断"},
     {"text": "跟陌生人理论，问他为什么这样", "score": 2, "fb": "纠缠可能延误最佳时机"},
     {"text": "吓坏了，不知道怎么办", "score": 1, "fb": "缺乏应急处理能力"}]))

# Save
with open(questions_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Total: {len(questions)} questions")
stats = {}
for q_obj in questions:
    key = (q_obj["difficulty"], q_obj["category"])
    stats[key] = stats.get(key, 0) + 1
easy = sum(1 for q in questions if q["difficulty"] == "easy")
medium = sum(1 for q in questions if q["difficulty"] == "medium")
hard = sum(1 for q in questions if q["difficulty"] == "hard")
print(f"  Easy: {easy}, Medium: {medium}, Hard: {hard}")
print(f"  Easy+Medium ratio: {(easy+medium)/len(questions)*100:.1f}%")
cats = {}
for q in questions:
    cats[q["category"]] = cats.get(q["category"], 0) + 1
print(f"  Categories: {cats}")
for (d, c), n in sorted(stats.items()):
    print(f"    {d:6s} {c:12s}: {n}q")
