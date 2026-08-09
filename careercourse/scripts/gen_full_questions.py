#!/usr/bin/env python3
"""完整生成20道职业评估题目"""
import json

QUESTIONS = [
    {"id": 1, "category": "education", "question": "What is your current education/skills situation?", "options": [
        {"text": "Still studying, gaining knowledge", "vector": {"openness": 0.6, "resilience": 0.5, "ambition": 0.7}},
        {"text": "Self-learning online/independent study", "vector": {"openness": 0.8, "resilience": 0.7, "ambition": 0.7}},
        {"text": "Just graduated, looking for first job", "vector": {"openness": 0.5, "resilience": 0.5, "ambition": 0.8}},
        {"text": "Working but want to switch careers", "vector": {"openness": 0.7, "resilience": 0.6, "ambition": 0.8}},
        {"text": "Experienced professional seeking advancement", "vector": {"openness": 0.5, "resilience": 0.7, "ambition": 0.9}}
    ]},
    {"id": 2, "category": "finance", "question": "What's your financial situation?", "options": [
        {"text": "Very limited funds, need to survive first", "vector": {"risk_taking": 0.3, "resilience": 0.8, "discipline": 0.7}},
        {"text": "Modest savings, can take some risks", "vector": {"risk_taking": 0.5, "resilience": 0.6, "discipline": 0.6}},
        {"text": "Comfortable, can invest in goals", "vector": {"risk_taking": 0.6, "resilience": 0.5, "discipline": 0.7}},
        {"text": "Well-funded, pursuing ambitious projects", "vector": {"risk_taking": 0.8, "resilience": 0.6, "ambition": 0.9}}
    ]},
    {"id": 3, "category": "work", "question": "What's your current work situation?", "options": [
        {"text": "Unemployed, searching for opportunities", "vector": {"resilience": 0.7, "ambition": 0.8, "risk_taking": 0.5}},
        {"text": "Entry-level job, learning the ropes", "vector": {"openness": 0.7, "resilience": 0.5, "ambition": 0.6}},
        {"text": "Mid-level, feeling stuck or ready for more", "vector": {"resilience": 0.6, "ambition": 0.8, "risk_taking": 0.6}},
        {"text": "Running a team or business already", "vector": {"leadership": 0.8, "risk_taking": 0.7, "ambition": 0.9}}
    ]},
    {"id": 4, "category": "location", "question": "Where are you based?", "options": [
        {"text": "Rural/small town with limited opportunities", "vector": {"resilience": 0.7, "ambition": 0.8, "risk_taking": 0.5}},
        {"text": "Mid-sized city, some opportunities", "vector": {"risk_taking": 0.5, "ambition": 0.6, "openness": 0.5}},
        {"text": "Major city with many options", "vector": {"risk_taking": 0.6, "ambition": 0.7, "openness": 0.6}},
        {"text": "Global/can relocate anywhere", "vector": {"risk_taking": 0.7, "ambition": 0.8, "openness": 0.8}}
    ]},
    {"id": 5, "category": "network", "question": "How's your professional network?", "options": [
        {"text": "Almost no connections in my field", "vector": {"risk_taking": 0.4, "resilience": 0.7, "ambition": 0.7}},
        {"text": "Some acquaintances, limited reach", "vector": {"risk_taking": 0.5, "resilience": 0.6, "ambition": 0.6}},
        {"text": "Good network, can get introductions", "vector": {"risk_taking": 0.6, "resilience": 0.6, "ambition": 0.7}},
        {"text": "Strong network with influential people", "vector": {"risk_taking": 0.7, "resilience": 0.7, "ambition": 0.8}}
    ]},
    {"id": 6, "category": "risk", "question": "How comfortable are you with risk?", "options": [
        {"text": "Very risk-averse, prefer stability", "vector": {"risk_taking": 0.2, "discipline": 0.8, "resilience": 0.5}},
        {"text": "Somewhat cautious but can take calculated risks", "vector": {"risk_taking": 0.4, "discipline": 0.7, "resilience": 0.6}},
        {"text": "Willing to gamble for big rewards", "vector": {"risk_taking": 0.8, "ambition": 0.8, "resilience": 0.7}},
        {"text": "Thrill-seeker, love high-stakes decisions", "vector": {"risk_taking": 0.95, "ambition": 0.9, "resilience": 0.8}}
    ]},
    {"id": 7, "category": "mentorship", "question": "Do you have access to mentors?", "options": [
        {"text": "No mentors, learning from books/internet", "vector": {"resilience": 0.8, "openness": 0.7, "discipline": 0.6}},
        {"text": "One or two informal guides", "vector": {"resilience": 0.6, "openness": 0.6, "discipline": 0.6}},
        {"text": "Several mentors in different fields", "vector": {"risk_taking": 0.6, "openness": 0.7, "discipline": 0.7}},
        {"text": "Strong mentorship network, regular guidance", "vector": {"risk_taking": 0.7, "openness": 0.8, "discipline": 0.7}}
    ]},
    {"id": 8, "category": "time", "question": "How much time can you dedicate to your goal?", "options": [
        {"text": "Very limited, have other responsibilities", "vector": {"discipline": 0.8, "resilience": 0.7, "ambition": 0.5}},
        {"text": "Part-time, evenings and weekends", "vector": {"discipline": 0.7, "resilience": 0.6, "ambition": 0.6}},
        {"text": "Full-time, but other obligations exist", "vector": {"discipline": 0.6, "resilience": 0.7, "ambition": 0.7}},
        {"text": "Unlimited time, fully committed", "vector": {"discipline": 0.7, "resilience": 0.8, "ambition": 0.9}}
    ]},
    {"id": 9, "category": "family", "question": "What's your family situation?", "options": [
        {"text": "Dependents, need stable income", "vector": {"risk_taking": 0.3, "discipline": 0.8, "resilience": 0.7}},
        {"text": "Partner/supportive family, some flexibility", "vector": {"risk_taking": 0.5, "discipline": 0.6, "resilience": 0.6}},
        {"text": "Independent, no major dependencies", "vector": {"risk_taking": 0.7, "ambition": 0.8, "resilience": 0.7}},
        {"text": "Family business/support system in place", "vector": {"risk_taking": 0.6, "leadership": 0.7, "ambition": 0.8}}
    ]},
    {"id": 10, "category": "failure", "question": "How have you handled past failures?", "options": [
        {"text": "Never faced major setbacks", "vector": {"resilience": 0.4, "ambition": 0.6, "risk_taking": 0.4}},
        {"text": "Setbacks but recovered quickly", "vector": {"resilience": 0.7, "ambition": 0.7, "risk_taking": 0.5}},
        {"text": "Multiple failures, learned from each", "vector": {"resilience": 0.9, "rationality": 0.8, "ambition": 0.8}},
        {"text": "Built success from repeated failures", "vector": {"resilience": 0.95, "rationality": 0.85, "ambition": 0.9}}
    ]},
    {"id": 11, "category": "goal", "question": "What's your primary career goal?", "options": [
        {"text": "Financial stability and security", "vector": {"risk_taking": 0.3, "discipline": 0.9, "rationality": 0.8}},
        {"text": "Creative expression and innovation", "vector": {"creativity": 0.9, "risk_taking": 0.6, "ambition": 0.7}},
        {"text": "Power and influence", "vector": {"leadership": 0.9, "ambition": 0.95, "risk_taking": 0.7}},
        {"text": "Making a difference in the world", "vector": {"empathy": 0.9, "resilience": 0.8, "ambition": 0.7}}
    ]},
    {"id": 12, "category": "learning", "question": "How do you prefer to learn?", "options": [
        {"text": "Formal education and structured programs", "vector": {"discipline": 0.8, "rationality": 0.8, "openness": 0.5}},
        {"text": "Self-study through books and online", "vector": {"discipline": 0.7, "openness": 0.8, "resilience": 0.6}},
        {"text": "Learning by doing and experimentation", "vector": {"risk_taking": 0.7, "creativity": 0.8, "resilience": 0.7}},
        {"text": "Mentorship and hands-on guidance", "vector": {"openness": 0.7, "empathy": 0.7, "discipline": 0.6}}
    ]},
    {"id": 13, "category": "age", "question": "What's your age range?", "options": [
        {"text": "Under 25 - early career exploration", "vector": {"openness": 0.8, "ambition": 0.7, "risk_taking": 0.6}},
        {"text": "25-35 - building foundation", "vector": {"ambition": 0.8, "risk_taking": 0.7, "resilience": 0.6}},
        {"text": "35-50 - mid-career pivot or advancement", "vector": {"resilience": 0.7, "rationality": 0.8, "discipline": 0.7}},
        {"text": "50+ - wisdom and legacy building", "vector": {"rationality": 0.9, "discipline": 0.8, "empathy": 0.7}}
    ]},
    {"id": 14, "category": "style", "question": "What work style do you prefer?", "options": [
        {"text": "Solo work, independent projects", "vector": {"risk_taking": 0.5, "discipline": 0.7, "ambition": 0.6}},
        {"text": "Small team, close collaboration", "vector": {"empathy": 0.7, "leadership": 0.5, "discipline": 0.6}},
        {"text": "Large organization, structured growth", "vector": {"discipline": 0.8, "leadership": 0.6, "rationality": 0.7}},
        {"text": "Leading teams, building organizations", "vector": {"leadership": 0.9, "ambition": 0.8, "risk_taking": 0.7}}
    ]},
    {"id": 15, "category": "geography", "question": "Where do you want to build your career?", "options": [
        {"text": "Local community, close to home", "vector": {"risk_taking": 0.3, "discipline": 0.7, "empathy": 0.8}},
        {"text": "National opportunities, willing to relocate", "vector": {"risk_taking": 0.5, "ambition": 0.6, "resilience": 0.6}},
        {"text": "International, open to global movement", "vector": {"risk_taking": 0.7, "openness": 0.9, "ambition": 0.8}},
        {"text": "Borderless, remote work from anywhere", "vector": {"openness": 0.8, "risk_taking": 0.6, "creativity": 0.7}}
    ]},
    {"id": 16, "category": "resilience", "question": "How do you handle criticism?", "options": [
        {"text": "Take it personally, struggle to move on", "vector": {"resilience": 0.3, "empathy": 0.6, "discipline": 0.5}},
        {"text": "Learn from it but feel discouraged", "vector": {"resilience": 0.5, "rationality": 0.6, "discipline": 0.6}},
        {"text": "Use it as fuel to prove them wrong", "vector": {"resilience": 0.8, "ambition": 0.8, "risk_taking": 0.7}},
        {"text": "Welcome feedback, constantly improve", "vector": {"resilience": 0.9, "openness": 0.9, "rationality": 0.85}}
    ]},
    {"id": 17, "category": "resources", "question": "What resources do you have access to?", "options": [
        {"text": "Very limited - starting from scratch", "vector": {"resilience": 0.8, "risk_taking": 0.4, "discipline": 0.7}},
        {"text": "Some savings and basic tools", "vector": {"risk_taking": 0.5, "discipline": 0.6, "resilience": 0.6}},
        {"text": "Good resources, can invest strategically", "vector": {"risk_taking": 0.6, "rationality": 0.7, "ambition": 0.7}},
        {"text": "Abundant resources, can take big bets", "vector": {"risk_taking": 0.8, "ambition": 0.9, "leadership": 0.7}}
    ]},
    {"id": 18, "category": "pressure", "question": "How much time pressure do you feel?", "options": [
        {"text": "Urgent - must succeed soon", "vector": {"risk_taking": 0.6, "resilience": 0.7, "ambition": 0.9}},
        {"text": "Moderate - can take a few years", "vector": {"risk_taking": 0.5, "discipline": 0.7, "resilience": 0.6}},
        {"text": "Relaxed - long-term perspective", "vector": {"rationality": 0.8, "discipline": 0.8, "resilience": 0.7}},
        {"text": "No pressure - exploring possibilities", "vector": {"openness": 0.8, "ambition": 0.5, "risk_taking": 0.4}}
    ]},
    {"id": 19, "category": "rolemodel", "question": "Which type of success inspires you?", "options": [
        {"text": "Business tycoons and billionaires", "vector": {"ambition": 0.95, "risk_taking": 0.8, "leadership": 0.7}},
        {"text": "Scientists and innovators", "vector": {"creativity": 0.9, "rationality": 0.85, "resilience": 0.7}},
        {"text": "Political leaders and changemakers", "vector": {"leadership": 0.9, "resilience": 0.8, "ambition": 0.8}},
        {"text": "Artists and cultural figures", "vector": {"creativity": 0.95, "openness": 0.8, "risk_taking": 0.6}}
    ]},
    {"id": 20, "category": "support", "question": "What's your support system like?", "options": [
        {"text": "Alone, building from zero", "vector": {"resilience": 0.9, "risk_taking": 0.5, "discipline": 0.8}},
        {"text": "Some supportive people around", "vector": {"resilience": 0.7, "empathy": 0.6, "discipline": 0.6}},
        {"text": "Strong network of allies and mentors", "vector": {"risk_taking": 0.7, "leadership": 0.6, "ambition": 0.7}},
        {"text": "Built-in support system, resources ready", "vector": {"risk_taking": 0.8, "ambition": 0.8, "leadership": 0.7}}
    ]}
]

with open("/c/Users/Pactera/projects/careercourse/src/data/questions.json", "w", encoding="utf-8") as f:
    json.dump(QUESTIONS, f, ensure_ascii=False, indent=2)

print(f"Created {len(QUESTIONS)} questions")
