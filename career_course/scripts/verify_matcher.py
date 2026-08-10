"""Verify career_course matcher works with 60 questions"""
import json, sys
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
errors = []

# 1. Check vector format
figs = json.load(open(BASE/"src/data/figures.json", encoding="utf-8"))["figures"]
bad = [f["name"] for f in figs if not isinstance(f.get("vector"), dict)]
if bad:
    errors.append(f"{len(bad)} figures have list vectors")
else:
    print("✓ All vectors are dicts")

# 2. Test matcher
sys.path.insert(0, str(BASE))
from src.engine.matcher import match_user
answers = [{"question_id":i+1,"option_index":i%4} for i in range(60)]
try:
    r = match_user(answers, top_n=3)
    print(f"✓ Matcher: {len(r['matches'])} matches")
except Exception as e:
    errors.append(f"Matcher error: {e}")

# 3. Check radar
if r["matches"][0]["suggestion"].get("radar"):
    print("✓ Radar data present")
else:
    errors.append("missing radar")

if errors:
    print(f"\nFAIL ({len(errors)}):")
    for e in errors:
        print(f"  ✗ {e}")
    exit(1)
print("\n✓ All checks passed")