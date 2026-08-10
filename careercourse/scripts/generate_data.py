"""Generate 100 historical figures for CareerCourse."""
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "src" / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

FIGURES = [
    # Real historical figures (20)
    {"id": "newton", "name": "Isaac Newton", "name_cn": "牛顿", "era": "1643-1727", "period": "17世纪", "type": "科学家",
     "vector": {"openness": 0.6, "conscientiousness": 0.9, "extraversion": 0.2, "agreeableness": 0.2, "neuroticism": 0.4, "leadership": 0.5, "risk_taking": 0.4, "rationality": 0.95, "discipline": 0.9, "empathy": 0.2, "ambition": 0.7, "resilience": 0.8},
     "early_career": "剑桥大学三一学院学生，瘟疫爆发期间居家18个月", "early_actions": "在隔离期间发展出微积分、光学理论和万有引力定律", "breakthrough": "发表《自然哲学的数学原理》，建立经典力学体系，成为皇家学会会长", "key_lesson": "Standing on the shoulders of giants. 站在巨人的肩膀上。"},
    {"id": "einstein", "name": "Albert Einstein", "name_cn": "爱因斯坦", "era": "1879-1955", "period": "20世纪", "type": "科学家",
     "vector": {"openness": 0.98, "conscientiousness": 0.6, "extraversion": 0.3, "agreeableness": 0.5, "neuroticism": 0.4, "leadership": 0.5, "risk_taking": 0.6, "rationality": 0.9, "discipline": 0.65, "empathy": 0.6, "ambition": 0.7, "resilience": 0.7},
     "early_career": "瑞士专利局三级技术员，1905年被称为奇迹年", "early_actions": "利用业余时间研究物理，发表4篇开创性论文", "breakthrough": "提出相对论、E=mc²，获得1921年诺贝尔物理学奖", "key_lesson": "Imagination is more important than knowledge. 想象力比知识更重要。"},
    {"id": "tesla", "name": "Nikola Tesla", "name_cn": "特斯拉", "era": "1856-1943", "period": "19世纪", "type": "发明家",
     "vector": {"openness": 0.95, "conscientiousness": 0.7, "extraversion": 0.3, "agreeableness": 0.4, "neuroticism": 0.6, "leadership": 0.6, "risk_taking": 0.8, "rationality": 0.85, "discipline": 0.75, "empathy": 0.3, "ambition": 0.85, "resilience": 0.8},
     "early_career": "移民美国的塞尔维亚裔工程师，曾在爱迪生公司工作", "early_actions": "设计交流电系统，与爱迪生展开电流战争", "breakthrough": "发明特斯拉线圈，奠定现代电力系统基础", "key_lesson": "The present is theirs; the future, for which I really worked, is mine. 现在是他们，未来属于我。"},
    {"id": "galileo", "name": "Galileo Galilei", "name_cn": "伽利略", "era": "1564-1642", "period": "16世纪", "type": "科学家",
     "vector": {"openness": 0.9, "conscientiousness": 0.75, "extraversion": 0.4, "agreeableness": 0.3, "neuroticism": 0.5, "leadership": 0.6, "risk_taking": 0.85, "rationality": 0.9, "discipline": 0.8, "empathy": 0.4, "ambition": 0.8, "resilience": 0.85},
     "early_career": "医学院学生，转向数学和物理研究", "early_actions": "改进望远镜，系统观测天体", "breakthrough": "支持日心说，现代观测天文学之父", "key_lesson": "All truths are easy to understand once they are discovered. 真理一旦被发现就很简单。"},
    {"id": "mozart", "name": "Wolfgang Mozart", "name_cn": "莫扎特", "era": "1756-1791", "period": "18世纪", "type": "艺术家",
     "vector": {"openness": 0.95, "conscientiousness": 0.85, "extraversion": 0.6, "agreeableness": 0.5, "neuroticism": 0.6, "leadership": 0.4, "risk_taking": 0.5, "rationality": 0.7, "discipline": 0.9, "empathy": 0.6, "ambition": 0.7, "resilience": 0.6},
     "early_career": "神童，4岁开始作曲，6岁巡演欧洲", "early_actions": "为宫廷作曲，争取创作自由", "breakthrough": "创作41部交响曲，歌剧大师", "key_lesson": "The music is not in the notes, but in the silence between. 音乐不在音符中，而在音符之间的沉默里。"},
    {"id": "shakespeare", "name": "William Shakespeare", "name_cn": "莎士比亚", "era": "1564-1616", "period": "16世纪", "type": "作家",
     "vector": {"openness": 0.9, "conscientiousness": 0.7, "extraversion": 0.5, "agreeableness": 0.4, "neuroticism": 0.4, "leadership": 0.6, "risk_taking": 0.5, "rationality": 0.8, "discipline": 0.75, "empathy": 0.85, "ambition": 0.7, "resilience": 0.7},
     "early_career": "埃文河畔斯特拉特福的抄写员之子，到伦敦谋生", "early_actions": "加入剧团，从演员成长为剧作家", "breakthrough": "创作37部戏剧，奠定英语文学基础", "key_lesson": "All the world's a stage. 全世界是一个舞台。"},
    {"id": "curie", "name": "Marie Curie", "name_cn": "居里夫人", "era": "1867-1934", "period": "19世纪", "type": "科学家",
     "vector": {"openness": 0.85, "conscientiousness": 0.95, "extraversion": 0.3, "agreeableness": 0.6, "neuroticism": 0.3, "leadership": 0.7, "risk_taking": 0.6, "rationality": 0.9, "discipline": 0.95, "empathy": 0.5, "ambition": 0.9, "resilience": 0.9},
     "early_career": "华沙女子大学辍学，到巴黎留学，生活贫困", "early_actions": "在简陋棚屋提炼沥青铀矿", "breakthrough": "发现钋和镭，两获诺贝尔奖", "key_lesson": "Nothing in life is to be feared, it is only to be understood. 生活中没有什么可怕，只有需要理解。"},
    {"id": "lincoln", "name": "Abraham Lincoln", "name_cn": "林肯", "era": "1809-1865", "period": "19世纪", "type": "政治家",
     "vector": {"openness": 0.6, "conscientiousness": 0.9, "extraversion": 0.4, "agreeableness": 0.7, "neuroticism": 0.5, "leadership": 0.9, "risk_taking": 0.6, "rationality": 0.75, "discipline": 0.85, "empathy": 0.8, "ambition": 0.7, "resilience": 0.9},
     "early_career": "穷苦出身，自学法律，当过邮递员", "early_actions": "从律师步入政坛，领导国家度过内战", "breakthrough": "废除奴隶制，维护国家统一", "key_lesson": "Be sure you put your feet in the right place. 确保你的脚步踏在正确的位置。"},
    {"id": "steve_jobs", "name": "Steve Jobs", "name_cn": "乔布斯", "era": "1955-2011", "period": "现代", "type": "企业家",
     "vector": {"openness": 0.85, "conscientiousness": 0.7, "extraversion": 0.5, "agreeableness": 0.3, "neuroticism": 0.6, "leadership": 0.95, "risk_taking": 0.9, "rationality": 0.75, "discipline": 0.8, "empathy": 0.4, "ambition": 0.95, "resilience": 0.85},
     "early_career": "大学辍学，在家打草稿，创立苹果", "early_actions": "被自己创立的公司开除，后重返", "breakthrough": "创造个人电脑、iPhone、iPad革命", "key_lesson": "Stay hungry, stay foolish. 求知若饥，虚心若愚。"},
    {"id": "elon_musk", "name": "Elon Musk", "name_cn": "马斯克", "era": "1971-至今", "period": "现代", "type": "企业家",
     "vector": {"openness": 0.9, "conscientiousness": 0.8, "extraversion": 0.6, "agreeableness": 0.3, "neuroticism": 0.5, "leadership": 0.9, "risk_taking": 0.95, "rationality": 0.85, "discipline": 0.85, "empathy": 0.4, "ambition": 0.95, "resilience": 0.9},
     "early_career": "南非移民，宾夕法尼亚大学辍学，创办Zip2", "early_actions": "卖掉Zip2用所得创办PayPal", "breakthrough": "创立SpaceX、Tesla，推动太空和商业电动车", "key_lesson": "When something is important enough, you do it even if the odds are not in your favor. 事情重要到一定程度，就要去做。"},
    {"id": "mark_zuckerberg", "name": "Mark Zuckerberg", "name_cn": "扎克伯格", "era": "1984-至今", "period": "现代", "type": "企业家",
     "vector": {"openness": 0.85, "conscientiousness": 0.6, "extraversion": 0.4, "agreeableness": 0.3, "neuroticism": 0.4, "leadership": 0.75, "risk_taking": 0.7, "rationality": 0.6, "discipline": 0.7, "empathy": 0.3, "ambition": 0.9, "resilience": 0.7},
     "early_career": "哈佛大二学生，创建Facemash", "early_actions": "每天编码16小时，向35位投资人推销", "breakthrough": "创立Facebook，发展为Meta平台", "key_lesson": "Move fast and break things. 快速行动，打破常规。"},
    {"id": "bill_gates", "name": "Bill Gates", "name_cn": "比尔·盖茨", "era": "1955-至今", "period": "现代", "type": "企业家",
     "vector": {"openness": 0.75, "conscientiousness": 0.9, "extraversion": 0.4, "agreeableness": 0.5, "neuroticism": 0.3, "leadership": 0.8, "risk_taking": 0.6, "rationality": 0.9, "discipline": 0.9, "empathy": 0.5, "ambition": 0.85, "resilience": 0.75},
     "early_career": "哈佛辍学，与沃兹尼克创办微软", "early_actions": "专注软件授权模式，与IBM合作", "breakthrough": "创立微软，成为全球首富", "key_lesson": "Success is a lousy teacher. 成功是糟糕的老师。"},
    {"id": "warren_buffett", "name": "Warren Buffett", "name_cn": "沃伦·巴菲特", "era": "1930-至今", "period": "现代", "type": "投资者",
     "vector": {"openness": 0.6, "conscientiousness": 0.95, "extraversion": 0.3, "agreeableness": 0.7, "neuroticism": 0.2, "leadership": 0.6, "risk_taking": 0.4, "rationality": 0.95, "discipline": 0.95, "empathy": 0.6, "ambition": 0.6, "resilience": 0.8},
     "early_career": "大学时阅读格雷厄姆的《证券分析》，开始投资", "early_actions": "建立合伙企业，后收购伯克希尔", "breakthrough": "成为价值投资大师，全球最富有人物之一", "key_lesson": "Price is what you pay. Value is what you get. 价格是支付的，价值是得到的。"},
    {"id": "edison", "name": "Thomas Edison", "name_cn": "爱迪生", "era": "1847-1931", "period": "19世纪", "type": "发明家",
     "vector": {"openness": 0.8, "conscientiousness": 0.85, "extraversion": 0.5, "agreeableness": 0.4, "neuroticism": 0.4, "leadership": 0.7, "risk_taking": 0.7, "rationality": 0.8, "discipline": 0.9, "empathy": 0.4, "ambition": 0.85, "resilience": 0.9},
     "early_career": "小学被退学，母亲在家教育，做过报童", "early_actions": "发明留声机、改进电灯，建立实验室", "breakthrough": "拥有1093项专利，建立现代工业研发体系", "key_lesson": "Genius is one percent inspiration and ninety-nine percent perspiration. 天才就是1%灵感加99%汗水。"},
    {"id": "freud", "name": "Sigmund Freud", "name_cn": "弗洛伊德", "era": "1856-1939", "period": "19世纪", "type": "心理学家",
     "vector": {"openness": 0.85, "conscientiousness": 0.8, "extraversion": 0.3, "agreeableness": 0.5, "neuroticism": 0.6, "leadership": 0.6, "risk_taking": 0.5, "rationality": 0.75, "discipline": 0.85, "empathy": 0.7, "ambition": 0.8, "resilience": 0.75},
     "early_career": "维也纳大学医学博士，研究神经系统", "early_actions": "创立精神分析学派，研究潜意识", "breakthrough": "提出本我、自我、超我理论", "key_lesson": "Unexpressed emotions will never die. 未表达的情绪永远不会消失。"},
    {"id": "darwin", "name": "Charles Darwin", "name_cn": "达尔文", "era": "1809-1882", "period": "19世纪", "type": "科学家",
     "vector": {"openness": 0.9, "conscientiousness": 0.85, "extraversion": 0.3, "agreeableness": 0.6, "neuroticism": 0.5, "leadership": 0.5, "risk_taking": 0.6, "rationality": 0.85, "discipline": 0.9, "empathy": 0.7, "ambition": 0.7, "resilience": 0.8},
     "early_career": "医学辍学，随小猎犬号环球考察", "early_actions": "收集标本，研究物种变异", "breakthrough": "提出进化论，发表《物种起源》", "key_lesson": "It is not the strongest that survive. 不是最强者生存，而是最能适应者。"},
    {"id": "pasteur", "name": "Louis Pasteur", "name_cn": "巴斯德", "era": "1822-1895", "period": "19世纪", "type": "科学家",
     "vector": {"openness": 0.8, "conscientiousness": 0.9, "extraversion": 0.4, "agreeableness": 0.6, "neuroticism": 0.4, "leadership": 0.6, "risk_taking": 0.5, "rationality": 0.85, "discipline": 0.9, "empathy": 0.5, "ambition": 0.75, "resilience": 0.8},
     "early_career": "化学博士，研究晶体学", "early_actions": "研究发酵和疾病微生物理论", "breakthrough": "发明巴氏消毒法，创立免疫学", "key_lesson": "Chance favors the prepared mind. 机会眷顾有准备的心灵。"},
    {"id": "ada_lovelace", "name": "Ada Lovelace", "name_cn": "阿达·洛芙莱斯", "era": "1815-1852", "period": "19世纪", "type": "科学家",
     "vector": {"openness": 0.95, "conscientiousness": 0.8, "extraversion": 0.4, "agreeableness": 0.5, "neuroticism": 0.5, "leadership": 0.6, "risk_taking": 0.6, "rationality": 0.9, "discipline": 0.8, "empathy": 0.6, "ambition": 0.8, "resilience": 0.7},
     "early_career": "诗人拜伦之女，自学数学", "early_actions": "与巴贝奇合作，撰写分析机笔记", "breakthrough": "世界上第一位程序员，预见计算机潜力", "key_lesson": "The Analytical Engine weaves algebraic patterns. 分析机编织代数模式。"},
    {"id": "florence_nightingale", "name": "Florence Nightingale", "name_cn": "南丁格尔", "era": "1820-108", "period": "19世纪", "type": "护士",
     "vector": {"openness": 0.7, "conscientiousness": 0.95, "extraversion": 0.5, "agreeableness": 0.8, "neuroticism": 0.4, "leadership": 0.7, "risk_taking": 0.5, "rationality": 0.85, "discipline": 0.9, "empathy": 0.9, "ambition": 0.75, "resilience": 0.85},
     "early_career": "贵族出身，拒绝婚姻，坚持学医", "early_actions": "克里米亚战争中护理伤员", "breakthrough": "创立现代护理学，统计学家", "key_lesson": "The greatest value of a picture is the truth it conveys. 图片的价值在于传达真理。"},
    {"id": "helen_keller", "name": "Helen Keller", "name_cn": "海伦·凯勒", "era": "1880-1968", "period": "20世纪", "type": "作家",
     "vector": {"openness": 0.85, "conscientiousness": 0.9, "extraversion": 0.6, "agreeableness": 0.85, "neuroticism": 0.4, "leadership": 0.6, "risk_taking": 0.5, "rationality": 0.8, "discipline": 0.95, "empathy": 0.9, "ambition": 0.8, "resilience": 0.95},
     "early_career": "19个月大时失明失聪，安妮·沙利文老师教育", "early_actions": "学习语言，考入哈佛大学拉德克利夫学院", "breakthrough": "成为作家、演说家，推动残障人士权利", "key_lesson": "Optimism is the faith that leads to achievement. 乐观是成就的信念。"},
    # Generic historical figures (80)
]

# Generate 80 generic figures
first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Quinn", "Avery", "Cameron", "Dakota",
               "Reese", "Sage", "Skyler", "Rowan", "Emery", "Finley", "Harper", "Jordan", "Kendall", "Logan",
               "Marcus", "Nadia", "Oscar", "Paula", "Quincy", "Robin", "Sam", "Tessa", "Uma", "Victor",
               "Wendy", "Xavier", "Yolanda", "Zara", "Adam", "Bella", "Chris", "Diana", "Ethan", "Fiona",
               "George", "Hannah", "Ivan", "Julia", "Kevin", "Laura", "Michael", "Nancy", "Owen", "Paula",
               "Rachel", "Steven", "Tina", "Ursula", "Vincent", "Wendy", "Xena", "Yuri", "Zoe", "Alan",
               "Beth", "Carl", "Doris", "Erik", "Fay", "Greg", "Holly", "Ian", "Joan", "Ken", "Lynn",
               "Mike", "Nora", "Ora", "Phil", "Rita", "Stan", "Tara", "Udo", "Vera", "Walt", "Xia", "Yao", "Zed"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
              "Anderson", "Taylor", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Moore", "Allen",
              "Young", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams",
              "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts", "Gomez", "Phillips",
              "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris",
              "Morales", "Murphy", "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey",
              "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson", "Brooks",
              "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes", "Price", "Alvarez"]

types = ["企业家", "科学家", "艺术家", "政治家", "军事家", "哲学家", "教育家", "文学家", "运动员", "发明家", "音乐家", "建筑师"]

for i in range(80):
    first = first_names[i]
    last = last_names[i]
    fig_type = types[i % len(types)]
    
    # Generate random vector with bias toward high values
    import random
    random.seed(i + 100)  # For reproducibility
    
    fig = {
        "id": f"history_figure_{i+1}",
        "name": f"{first} {last}",
        "name_cn": f"历史人物{i+1}",
        "era": f"未知时期",
        "period": "古代",
        "type": fig_type,
        "vector": {
            "openness": round(random.uniform(0.4, 0.95), 2),
            "conscientiousness": round(random.uniform(0.4, 0.95), 2),
            "extraversion": round(random.uniform(0.2, 0.8), 2),
            "agreeableness": round(random.uniform(0.3, 0.8), 2),
            "neuroticism": round(random.uniform(0.2, 0.7), 2),
            "leadership": round(random.uniform(0.3, 0.9), 2),
            "risk_taking": round(random.uniform(0.3, 0.9), 2),
            "rationality": round(random.uniform(0.4, 0.95), 2),
            "discipline": round(random.uniform(0.4, 0.95), 2),
            "empathy": round(random.uniform(0.3, 0.85), 2),
            "ambition": round(random.uniform(0.4, 0.95), 2),
            "resilience": round(random.uniform(0.4, 0.9), 2)
        },
        "early_career": f"早年经历坎坷，{fig_type}道路充满挑战",
        "early_actions": f"坚持不懈，{fig_type}事业逐渐起步",
        "breakthrough": f"最终成为{fig_type}领域的杰出代表",
        "key_lesson": f"坚持就是胜利。"
    }
    FIGURES.append(fig)

with open(DATA_DIR / "figures.json", "w", encoding="utf-8") as f:
    json.dump(FIGURES, f, ensure_ascii=False, indent=2)

print(f"Generated {len(FIGURES)} figures")
