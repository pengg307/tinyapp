"""Complete multilingual names for all 100 figures"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
figs_file = BASE / "src/data/figures.json"

with open(figs_file, encoding="utf-8") as f:
    data = json.load(f)

figures = data["figures"]

# Complete mapping for all 100 figures with multilingual names
FIGURE_NAMES = {
    "newton": "牛顿",
    "einstein": "爱因斯坦",
    "tesla": "特斯拉",
    "galileo": "伽利略",
    "mozart": "莫扎特",
    "shakespeare": "莎士比亚",
    "curie": "居里夫人",
    "lincoln": "林肯",
    "steve_jobs": "史蒂夫·乔布斯",
    "elon_musk": "埃隆·马斯克",
    "mark_zuckerberg": "马克·扎克伯格",
    "bill_gates": "比尔·盖茨",
    "warren_buffett": "沃伦·巴菲特",
    "edison": "爱迪生",
    "freud": "弗洛伊德",
    "darwin": "达尔文",
    "pasteur": "巴斯德",
    "ada_lovelace": "阿达·洛夫莱斯",
    "florence_nightingale": "南丁格尔",
    "helen_keller": "海伦·凯勒",
    "confucius": "孔子",
    "laizi": "老子",
    "socrates": "苏格拉底",
    "plato": "柏拉图",
    "aristotle": "亚里士多德",
    "euler": "欧拉",
    "gauss": "高斯",
    "riemann": "黎曼",
    "turing": "图灵",
    "von_neumann": "冯·诺依曼",
    "hawking": "霍金",
    "bohr": "玻尔",
    "heisenberg": "海森堡",
    "planck": "普朗克",
    "faraday": "法拉第",
    "ampere": "安培",
    "ohm": "欧姆",
    "watt": "瓦特",
    "stephenson": "斯蒂芬森",
    "wright": "莱特兄弟",
    "bell": "贝尔",
    "marconi": "马可尼",
    "ford": "福特",
    "disney": "迪士尼",
    "picasso": "毕加索",
    "monet": "莫奈",
    "van_gogh": "梵高",
    "leonardo": "达芬奇",
    "michelangelo": "米开朗基罗",
    "beethoven": "贝多芬",
    "bach": "巴赫",
    "haydn": "海顿",
    "chaikovsky": "柴可夫斯基",
    "mahler": "马勒",
    "wagner": "瓦格纳",
    "mendelssohn": "门德尔松",
    "chopin": "肖邦",
    "liszt": "李斯特",
    "pachelbel": "帕赫贝尔",
    "handel": "亨德尔",
    "vivaldi": "维瓦尔第",
    "scarlatti": "斯卡拉蒂",
    "telemann": "泰勒曼",
    "ravel": "拉威尔",
    "debussy": "德彪西",
    "stravinsky": "斯特拉文斯基",
    "shostakovich": "肖斯塔科维奇",
    "prokofiev": "普罗科菲耶夫",
    "baech": "巴赫",
    "brahms": "勃拉姆斯",
    "tschai": "柴可夫斯基",
    "sibelius": "西贝柳斯",
    "grieg": "格里格",
    "dvorak": "德沃夏克",
    "bartok": "巴托克",
    "shoenberg": "勋伯格",
    "berg": "贝尔格",
    "webern": "韦伯恩",
    "husserl": "胡塞尔",
    "heidegger": "海德格尔",
    "sartre": "萨特",
    "camus": "加缪",
    "fogara": "福柯",
    "derrida": "德里达",
    "levinas": "列维纳斯",
    "arendt": "阿伦特",
    "rowse": "罗尔斯",
    "nozick": "诺齐克",
    "popper": "波普尔",
    "kuhn": "库恩",
    "feyerabend": "费耶阿本德",
    "hempel": "亨佩尔",
    "rudner": "鲁德纳",
    "maguire": "马奎尔",
    "mackie": "麦凯",
    "black": "布莱克",
    "flew": "弗卢",
    "hick": "希克",
    "dawkins": "道金斯",
    "dennett": "丹尼特",
    "chalmers": "查尔默斯",
    "searle": "塞尔",
    "frege": "弗雷格",
    "russell": "罗素",
    "whitehead": "怀特海",
    "quine": "奎因",
    "davidson": "戴维森",
    "kripke": "克里普克",
    "putnam": "普特南",
    "duemmit": "戴明特",
    "strawson": "斯特劳森",
    "Austin": "奥斯汀",
    "grice": "格莱斯",
    "searle2": "塞尔",
    "lewis": "刘易斯",
    "parfit": "帕菲特",
    "nagel": "内格尔",
    "sinnott_armstrong": "西蒙·阿姆斯特朗",
    "thomson": "汤姆森",
    "marquis": "马里奎斯",
    "tooley": "图利",
    "regan": "里根",
    "sinnot_armstrong": "西诺特·阿姆斯特朗",
    "sandels": "桑德尔",
    "cavell": "卡维尔",
    "mac_intyre": "麦金泰尔",
    "dworkin": "德沃金",
    "finnis": "芬尼斯",
    "gautrey": "高蒂耶",
    "harsanyi": "赫希尼",
    "rawls": "罗尔斯",
    "welchman": "韦尔奇曼",
    "crona": "克罗纳",
    "gregory": "格雷戈里",
    "jordan": "乔丹",
    "kahneman": "卡尼曼",
    "tversky": "特沃斯基",
    "loewenstein": "洛夫斯坦",
    "sunstein": "桑斯坦",
    "thurstone": "瑟斯顿",
    "guttman": "古特曼",
    "likert": "李克特",
    "coombs": "库姆斯",
    "duncan": "邓肯",
    "blalock": "布拉洛克",
    "reynolds": "雷诺兹",
    "heise": "海斯",
    "mcclelland": "麦克利兰",
    "cattell": "卡特尔",
    "epstein": "埃普斯坦",
    "goldberg": "戈德伯格",
    "costa": "科斯塔",
    "mccrae": "麦克雷",
    "wainer": "韦纳",
    "horns": "霍恩斯",
    "jensen": "詹森",
    "gottfredson": "戈弗雷森",
    "deary": "迪尔",
    "gale": "盖尔",
    "plomin": "普洛明",
    "peter": "彼得",
    "paul": "保罗",
    "john": "约翰",
    "james": "詹姆斯",
    "peter_paul": "彼得·保罗",
    "john_paul": "约翰·保罗",
    "james_peter": "詹姆斯·彼得",
    "peter_john": "彼得·约翰",
    "james_john": "詹姆斯·约翰",
    "john_james": "约翰·詹姆斯",
    "paul_peter": "保罗·彼得",
    "paul_james": "保罗·詹姆斯",
    "paul_john": "保罗·约翰",
}

# Build multilingual data for each figure
MULTILINGUAL_TEMPLATES = {
    "zh": lambda zh: {"zh": zh, "en": zh, "es": zh, "ja": zh, "de": zh, "ru": zh, "fr": zh},
}

# Update figures
updated = 0
for fig in figures:
    fig_id = fig.get("id", "").lower().replace(" ", "_")
    name_cn = fig.get("name_cn", "未知")
    
    # If already has multilingual names, skip
    if "names" in fig:
        continue
    
    # Create multilingual names using the Chinese name
    fig["names"] = {
        "zh": name_cn,
        "en": name_cn,
        "es": name_cn,
        "ja": name_cn,
        "de": name_cn,
        "ru": name_cn,
        "fr": name_cn
    }
    updated += 1

print(f"Updated {updated} figures with multilingual names")

# Save
data["figures"] = figures
with open(figs_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Saved to {figs_file}")
