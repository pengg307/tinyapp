"""Final verification: 7-language complete translation"""
import json, urllib.request, sys
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
errors = []

EXPECTED_DIM = {"zh": "外向性", "en": "Extraversion", "es": "Extraversión",
                "ja": "外向性", "de": "Extravertiertheit", "ru": "Экстраверсия", "fr": "Extraversion"}

for lang, exp in EXPECTED_DIM.items():
    try:
        r = urllib.request.urlopen(f"http://localhost:8006/api/questions?language={lang}", timeout=5)
        opts = [o["text"] for o in json.loads(r.read())["questions"][0]["options"]]
        if len(set(opts)) != 4:
            errors.append(f"{lang}: duplicate opts")
        
        data = json.dumps({"answers": [{"question_id": i, "option_index": i%4} for i in range(60)], "top_n": 1, "language": lang}).encode()
        req = urllib.request.Request("http://localhost:8006/api/match", data=data, headers={"Content-Type": "application/json"})
        r = urllib.request.urlopen(req, timeout=10)
        m = json.loads(r.read())["matches"][0]["suggestion"]
        
        dim = m["gaps"][0]["dimension"] if m.get("gaps") else ""
        if dim != exp:
            errors.append(f"{lang}: expected {exp}, got {dim}")
        
        print(f"✓ {lang.upper()}: {dim}")
    except Exception as e:
        errors.append(f"{lang}: {e}")

html = (BASE/"static/index.html").read_text()
for l in EXPECTED_DIM:
    if f"setLanguage('{l}')" not in html:
        errors.append(f"missing {l} button")

vc = json.loads(Path(r"E:\aiprojects\tinyapp\vercel.json").read_text())
if "career_course" not in str(vc):
    errors.append("vercel wrong path")

if errors:
    print(f"\nFAIL: {errors}")
    sys.exit(1)
print("\n✓ All 7 languages verified")
