"""Replace placeholder names with real historical figures"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
figs_file = BASE / "src/data/figures.json"

# Load existing figures
with open(figs_file, encoding="utf-8") as f:
    data = json.load(f)

figures = data["figures"]

# Real historical figures to replace placeholders
REAL_FIGURES = [
    {"name": "Leonardo da Vinci", "name_cn": "达·芬奇", "era": "文艺复兴", "type": "艺术家",
     "vector": [0.95, 0.85, 0.7, 0.8, 0.3, 0.6, 0.7, 0.9, 0.7, 0.8, 0.9, 0.8],
     "early_career": "学徒于韦罗基奥工作室，绘制《基督受洗》",
     "early_actions": "研究解剖、光学、飞行器，创作《最后的晚餐》",
     "breakthrough": "《蒙娜丽莎》成为史上最著名画作",
     "key_lesson": "艺术与科学的融合是创造力的源泉"},
    {"name": "Isaac Newton", "name_cn": "牛顿", "era": "科学革命", "type": "科学家",
     "vector": [0.8, 0.95, 0.4, 0.5, 0.3, 0.7, 0.6, 0.95, 0.9, 0.4, 0.8, 0.9],
     "early_career": "剑桥三一学院研究光学与微积分",
     "early_actions": "发现万有引力定律，建立经典力学体系",
     "breakthrough": "《自然哲学的数学原理》奠定近代科学基础",
     "key_lesson": "站在巨人肩膀上看得更远"},
    {"name": "Albert Einstein", "name_cn": "爱因斯坦", "era": "现代物理", "type": "科学家",
     "vector": [0.95, 0.7, 0.5, 0.6, 0.4, 0.6, 0.9, 0.95, 0.6, 0.7, 0.8, 0.7],
     "early_career": "专利局职员期间发表奇迹年论文",
     "early_actions": "提出相对论，解释光电效应",
     "breakthrough": "E=mc²改变人类对宇宙的认知",
     "key_lesson": "想象力比知识更重要"},
    {"name": "Marie Curie", "name_cn": "居里夫人", "era": "现代科学", "type": "科学家",
     "vector": [0.85, 0.95, 0.4, 0.7, 0.3, 0.5, 0.8, 0.9, 0.95, 0.6, 0.9, 0.9],
     "early_career": "巴黎理化学校研究放射性物质",
     "early_actions": "发现钋和镭，开创放射性理论",
     "breakthrough": "两获诺贝尔奖，唯一跨物理学和化学",
     "key_lesson": "坚韧不拔是科学的基石"},
    {"name": "Winston Churchill", "name_cn": "丘吉尔", "era": "二战", "type": "政治家",
     "vector": [0.7, 0.85, 0.8, 0.6, 0.4, 0.95, 0.6, 0.7, 0.8, 0.5, 0.9, 0.8],
     "early_career": "记者出身，后进入政坛",
     "early_actions": "二战期间领导英国抵抗纳粹",
     "breakthrough": "赢得二战，发表《铁幕演说》",
     "key_lesson": "永不言败是胜利的关键"},
    {"name": "Nelson Mandela", "name_cn": "曼德拉", "era": "现代", "type": "政治家",
     "vector": [0.8, 0.75, 0.6, 0.95, 0.2, 0.9, 0.4, 0.6, 0.8, 0.95, 0.85, 0.9],
     "early_career": "律师，反对种族隔离运动",
     "early_actions": "27年监禁中坚持抗争",
     "breakthrough": "成为南非首位黑人总统",
     "key_lesson": "宽恕比复仇更有力量"},
    {"name": "Steve Jobs", "name_cn": "乔布斯", "era": "现代", "type": "企业家",
     "vector": [0.9, 0.85, 0.7, 0.5, 0.5, 0.85, 0.9, 0.7, 0.8, 0.4, 0.95, 0.7],
     "early_career": "创立苹果电脑公司",
     "early_actions": "推出Macintosh，创建皮克斯",
     "breakthrough": "iPhone重新定义智能手机",
     "key_lesson": "保持饥饿，保持愚蠢"},
    {"name": "Thomas Edison", "name_cn": "爱迪生", "era": "工业革命", "type": "发明家",
     "vector": [0.75, 0.9, 0.5, 0.6, 0.3, 0.6, 0.8, 0.85, 0.95, 0.5, 0.85, 0.9],
     "early_career": "电报员出身，创立门洛帕克实验室",
     "early_actions": "发明留声机、改进电灯",
     "breakthrough": "建立第一个工业研究实验室",
     "key_lesson": "天才就是1%灵感加99%汗水"},
    {"name": "Abraham Lincoln", "name_cn": "林肯", "era": "美国历史", "type": "政治家",
     "vector": [0.6, 0.9, 0.5, 0.85, 0.3, 0.9, 0.4, 0.75, 0.85, 0.9, 0.8, 0.9],
     "early_career": "自学法律，进入政坛",
     "early_actions": "领导南北战争，废除奴隶制",
     "breakthrough": "葛底斯堡演说定义民主精神",
     "key_lesson": "民有、民治、民享的政府"},
    {"name": "Galileo Galilei", "name_cn": "伽利略", "era": "文艺复兴", "type": "科学家",
     "vector": [0.95, 0.8, 0.6, 0.5, 0.4, 0.7, 0.85, 0.9, 0.7, 0.5, 0.8, 0.7],
     "early_career": "医学院辍学，转向数学物理",
     "early_actions": "改进望远镜，发现木星卫星",
     "breakthrough": "支持日心说，现代观测天文学之父",
     "key_lesson": "自然之书用数学语言书写"},
    {"name": "Ada Lovelace", "name_cn": "洛夫莱斯", "era": "工业革命", "type": "数学家",
     "vector": [0.9, 0.85, 0.5, 0.7, 0.3, 0.6, 0.7, 0.95, 0.8, 0.6, 0.85, 0.8],
     "early_career": "拜伦之女，自学数学",
     "early_actions": "为分析机编写第一个算法",
     "breakthrough": "预见计算机的普遍用途",
     "key_lesson": "想象力的边界决定创新的极限"},
    {"name": "Florence Nightingale", "name_cn": "南丁格尔", "era": "工业革命", "type": "护士",
     "vector": [0.7, 0.95, 0.5, 0.9, 0.3, 0.7, 0.4, 0.8, 0.9, 0.95, 0.6, 0.85],
     "early_career": "放弃上流社会生活，学习护理",
     "early_actions": "克里米亚战争改革护理制度",
     "breakthrough": "现代护理学奠基人",
     "key_lesson": "细节决定生命的价值"},
    {"name": "Helen Keller", "name_cn": "海伦·凯勒", "era": "现代", "type": "作家",
     "vector": [0.85, 0.9, 0.4, 0.85, 0.2, 0.75, 0.5, 0.7, 0.95, 0.9, 0.8, 0.95],
     "early_career": "失明失聪后学习手语和盲文",
     "early_actions": "哈佛拉德克利夫学院毕业",
     "breakthrough": "《我的人生故事》激励全世界",
     "key_lesson": "乐观是信念成功的钥匙"},
    {"name": "Wolfgang Mozart", "name_cn": "莫扎特", "era": "古典时期", "type": "音乐家",
     "vector": [0.95, 0.75, 0.8, 0.7, 0.5, 0.6, 0.85, 0.8, 0.6, 0.9, 0.7, 0.6],
     "early_career": "神童演出，后成为宫廷乐师",
     "early_actions": "创作41部交响曲、27部钢琴协奏曲",
     "breakthrough": "《费加罗的婚礼》《魔笛》永垂不朽",
     "key_lesson": "音乐是心灵的直接语言"},
    {"name": "William Shakespeare", "name_cn": "莎士比亚", "era": "文艺复兴", "type": "作家",
     "vector": [0.9, 0.7, 0.6, 0.75, 0.4, 0.65, 0.7, 0.85, 0.6, 0.8, 0.75, 0.65],
     "early_career": "剧团演员，开始创作戏剧",
     "early_actions": "写作37部戏剧、154首十四行诗",
     "breakthrough": "《哈姆雷特》《李尔王》成为永恒",
     "key_lesson": "文字可以穿越时间"},
    {"name": "Charles Darwin", "name_cn": "达尔文", "era": "维多利亚", "type": "科学家",
     "vector": [0.85, 0.8, 0.4, 0.65, 0.3, 0.5, 0.75, 0.9, 0.75, 0.6, 0.7, 0.8],
     "early_career": "小猎犬号环球航行考察",
     "early_actions": "研究物种变异，提出自然选择",
     "breakthrough": "《物种起源》改变人类自我认知",
     "key_lesson": "适应者生存，而非最强者"},
    {"name": "Louis Pasteur", "name_cn": "巴斯德", "era": "维多利亚", "type": "科学家",
     "vector": [0.8, 0.9, 0.4, 0.7, 0.3, 0.55, 0.7, 0.9, 0.85, 0.6, 0.75, 0.85],
     "early_career": "化学家，研究发酵与微生物",
     "early_actions": "发明巴氏消毒法，研发狂犬疫苗",
     "breakthrough": "微生物学奠基人，挽救百万生命",
     "key_lesson": "机遇偏爱有准备的头脑"},
    {"name": "Sigmund Freud", "name_cn": "弗洛伊德", "era": "现代", "type": "心理学家",
     "vector": [0.9, 0.7, 0.5, 0.6, 0.6, 0.65, 0.75, 0.85, 0.65, 0.75, 0.7, 0.6],
     "early_career": "维也纳神经学家，研究癔症",
     "early_actions": "创立精神分析学派",
     "breakthrough": "潜意识理论改变心理学",
     "key_lesson": "梦是通往潜意识的皇家大道"},
    {"name": "Mark Zuckerberg", "name_cn": "扎克伯格", "era": "现代", "type": "企业家",
     "vector": [0.75, 0.8, 0.6, 0.5, 0.4, 0.85, 0.8, 0.75, 0.7, 0.45, 0.9, 0.7],
     "early_career": "哈佛学生创建Facebook",
     "early_actions": "扩张社交平台，收购Instagram",
     "breakthrough": "连接数十亿用户，重塑社交方式",
     "key_lesson": "移动优先是全球化的关键"},
]

# Get placeholder figures
placeholders = [f for f in figures if "历史人物" in f.get("name_cn", "")]
print(f"Found {len(placeholders)} placeholders to replace")

# Replace in order
for i, placeholder in enumerate(placeholders):
    if i < len(REAL_FIGURES):
        real = REAL_FIGURES[i]
        placeholder["name"] = real["name"]
        placeholder["name_cn"] = real["name_cn"]
        placeholder["era"] = real["era"]
        placeholder["type"] = real["type"]
        placeholder["vector"] = real["vector"]
        placeholder["early_career"] = real["early_career"]
        placeholder["early_actions"] = real["early_actions"]
        placeholder["breakthrough"] = real["breakthrough"]
        placeholder["key_lesson"] = real["key_lesson"]
        print(f"  {i+1}. {placeholder['name_cn']} ({placeholder['name']})")

# Save
data["figures"] = figures
with open(figs_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✓ Updated {len(placeholders)} figures")
print(f"✓ Saved to {figs_file}")
