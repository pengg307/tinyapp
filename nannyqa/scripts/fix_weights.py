"""Fix missing dimension weights and add master identification."""
import json
import os

questions_path = "E:/aiprojects/tinyapp/nannyqa/src/data/questions.json"
with open(questions_path, 'r', encoding='utf-8') as f:
    qs = json.load(f)

# Find all unique dimensions
all_dims = set(q['dimension'] for q in qs)
print(f"Total unique dimensions: {len(all_dims)}")

# Default weight for missing dimensions
DEFAULT_WEIGHT = 0.05

# Check which ones need fixing
fixed = 0
for q in qs:
    dim = q['dimension']
    if 'weight' not in q or q.get('weight') is None:
        q['weight'] = DEFAULT_WEIGHT
        fixed += 1

print(f"Fixed {fixed} questions with missing weights")

# Save
with open(questions_path, 'w', encoding='utf-8') as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)

print(f"Updated {questions_path}")