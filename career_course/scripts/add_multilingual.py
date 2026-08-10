"""Add multilingual names to career_course figures"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
figs_file = BASE / "src/data/figures.json"

with open(figs_file, encoding="utf-8") as f:
    data = json.load(f)

figures = data["figures"]

# 为每个历史人物添加多语言名字
MULTILINGUAL_NAMES = {
    "newton": {
        "name": "Isaac Newton",
        "names": {
            "zh": "牛顿",
            "en": "Isaac Newton",
            "es": "Isaac Newton",
            "ja": "アイザック・ニュートン",
            "de": "Isaac Newton",
            "ru": "Исаак Ньютон",
            "fr": "Isaac Newton"
        }
    },
    "einstein": {
        "name": "Albert Einstein",
        "names": {
            "zh": "爱因斯坦",
            "en": "Albert Einstein",
            "es": "Albert Einstein",
            "ja": "アルバート・アインシュタイン",
            "de": "Albert Einstein",
            "ru": "Альберт Эйнштейн",
            "fr": "Albert Einstein"
        }
    },
    "tesla": {
        "name": "Nikola Tesla",
        "names": {
            "zh": "特斯拉",
            "en": "Nikola Tesla",
            "es": "Nikola Tesla",
            "ja": "ニコラ・テスラ",
            "de": "Nikola Tesla",
            "ru": "Никола Тесла",
            "fr": "Nikola Tesla"
        }
    },
    "galileo": {
        "name": "Galileo Galilei",
        "names": {
            "zh": "伽利略",
            "en": "Galileo Galilei",
            "es": "Galileo Galilei",
            "ja": "ガリレオ・ガリレイ",
            "de": "Galileo Galilei",
            "ru": "Галилео Галилей",
            "fr": "Galileo Galilei"
        }
    },
    "mozart": {
        "name": "Wolfgang Amadeus Mozart",
        "names": {
            "zh": "莫扎特",
            "en": "Wolfgang Amadeus Mozart",
            "es": "Wolfgang Amadeus Mozart",
            "ja": "ヴォルフガング・アマデウス・モーツァルト",
            "de": "Wolfgang Amadeus Mozart",
            "ru": "Вольфганг Амадей Моцарт",
            "fr": "Wolfgang Amadeus Mozart"
        }
    },
    "shakespeare": {
        "name": "William Shakespeare",
        "names": {
            "zh": "莎士比亚",
            "en": "William Shakespeare",
            "es": "William Shakespeare",
            "ja": "ウィリアム・シェイクスピア",
            "de": "William Shakespeare",
            "ru": "Уильям Шекспир",
            "fr": "William Shakespeare"
        }
    },
    "curie": {
        "name": "Marie Curie",
        "names": {
            "zh": "居里夫人",
            "en": "Marie Curie",
            "es": "Marie Curie",
            "ja": "マリー・キュリー",
            "de": "Marie Curie",
            "ru": "Мария Кюри",
            "fr": "Marie Curie"
        }
    },
    "lincoln": {
        "name": "Abraham Lincoln",
        "names": {
            "zh": "林肯",
            "en": "Abraham Lincoln",
            "es": "Abraham Lincoln",
            "ja": "エイブラハム・リンカーン",
            "de": "Abraham Lincoln",
            "ru": "Авраам Линкольн",
            "fr": "Abraham Lincoln"
        }
    },
    "steve_jobs": {
        "name": "Steve Jobs",
        "names": {
            "zh": "史蒂夫·乔布斯",
            "en": "Steve Jobs",
            "es": "Steve Jobs",
            "ja": "スティーブ・ジョブズ",
            "de": "Steve Jobs",
            "ru": "Стив Джобс",
            "fr": "Steve Jobs"
        }
    },
    "elon_musk": {
        "name": "Elon Musk",
        "names": {
            "zh": "埃隆·马斯克",
            "en": "Elon Musk",
            "es": "Elon Musk",
            "ja": "イーロン・マスク",
            "de": "Elon Musk",
            "ru": "Илон Маск",
            "fr": "Elon Musk"
        }
    }
}

# Update figures with multilingual names
updated = 0
for fig in figures:
    fig_id = fig.get("id", "").lower()
    if fig_id in MULTILINGUAL_NAMES:
        multilingual = MULTILINGUAL_NAMES[fig_id]
        fig["name"] = multilingual["name"]
        fig["names"] = multilingual["names"]
        updated += 1
        print(f"✓ Updated: {fig.get('name_cn', fig.get('name'))}")

print(f"\nUpdated {updated} figures with multilingual names")

# Save
data["figures"] = figures
with open(figs_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Saved to {figs_file}")
