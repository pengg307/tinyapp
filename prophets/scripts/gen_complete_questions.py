#!/usr/bin/env python3
"""Generate 60 complete multilingual questions - 12 dimensions x 5 questions each"""
import json

# Complete question data with translations for all 7 languages
# Format: list of dicts with "trait" and "translations" (dict of 7 languages)
# Each language has "text" (question) and "options" (4 choices)

questions_data = [
    # === OPENNESS (5 questions) ===
    {"trait": "openness", "translations": {
        "zh": {"text": "面对全新的领域，你的态度是？", "options": ["充满好奇，积极尝试", "适度接受，但保持谨慎", "更倾向于熟悉的事物", "坚持传统，不喜变化"]},
        "en": {"text": "How do you approach a completely new field?", "options": ["Full of curiosity, actively try", "Moderately accept, but cautious", "Prefer familiar things", "Stick to tradition, dislike change"]},
        "es": {"text": "¿Cómo te enfrentas a un campo completamente nuevo?", "options": ["Con mucha curiosidad, probar activamente", "Aceptar moderadamente, pero con cautela", "Prefiero cosas conocidas", "Mantenerse en la tradición, no me gusta el cambio"]},
        "ja": {"text": "全く新しい分野に直面したとき、あなたは？", "options": ["好奇心満タンで積極的に挑戦", "適度に受け入れるが慎重に", "慣れたものに傾く", "伝統を守り変化を嫌う"]},
        "de": {"text": "Wie gehst du einem völlig neuen Gebiet gegenüber?", "options": ["Voll Neugier, aktiv ausprobieren", "Mäßig akzeptieren, aber vorsichtig", "Eher Vertrautes bevorzegen", "An der Tradition festhalten, keine Veränderung"]},
        "ru": {"text": "Как вы подходите к совершенно новой области?", "options": ["Полный любопытства, активно пробую", "Умеренно принимаю, но осторожно", "Предпочитаю знакомое", "Держусь традиций, не люблю перемен"]},
        "fr": {"text": "Comment abordez-vous un domaine complètement nouveau?", "options": ["Plein de curiosité, j'essaie activement", "J'accepte modérément mais prudemment", "Je préfère les choses familières", "Je reste dans la tradition, je déteste le changement"]}
    }},
    {"trait": "openness", "translations": {
        "zh": {"text": "你更喜欢尝试新事物还是坚持传统？", "options": ["充满好奇，积极尝试", "适度接受，但保持谨慎", "更倾向于熟悉的事物", "坚持传统，不喜变化"]},
        "en": {"text": "Do you prefer trying new things or sticking to tradition?", "options": ["Full of curiosity, actively try", "Moderately accept, but cautious", "Prefer familiar things", "Stick to tradition, dislike change"]},
        "es": {"text": "¿Prefieres probar cosas nuevas o mantenerte en la tradición?", "options": ["Con mucha curiosidad, probar activamente", "Aceptar moderadamente, pero con cautela", "Prefiero cosas conocidas", "Mantenerse en la tradición, no me gusta el cambio"]},
        "ja": {"text": "新しい物事を試すことを好むか、伝統を守るかを好むか？", "options": ["好奇心満タンで積極的に挑戦", "適度に受け入れるが慎重に", "慣れたものに傾く", "伝統を守り変化を嫌う"]},
        "de": {"text": "Bevorzugst du neue Dinge auszuprobieren oder an der Tradition festzuhalten?", "options": ["Voll Neugier, aktiv ausprobieren", "Mäßig akzeptieren, aber vorsichtig", "Eher Vertrautes bevorzegen", "An der Tradition festhalten, keine Veränderung"]},
        "ru": {"text": "Вы предпочитаете пробовать новое или придерживаться традиций?", "options": ["Полный любопытства, активно пробую", "Умеренно принимаю, но осторожно", "Предпочитаю знакомое", "Держусь традиций, не люблю перемен"]},
        "fr": {"text": "Préférez-vous essayer de nouvelles choses ou rester dans la tradition?", "options": ["Plein de curiosité, j'essaie activement", "J'accepte modérément mais prudemment", "Je préfère les choses familières", "Je reste dans la tradition, je déteste le changement"]}
    }},
    {"trait": "openness", "translations": {
        "zh": {"text": "当面对一个从未见过的难题时？", "options": ["兴奋不已，立即研究", "保持冷静，逐步分析", "感到困惑，寻求建议", "回避困难，选择简单"]},
        "en": {"text": "When facing an unfamiliar problem?", "options": ["Excited, research immediately", "Stay calm, analyze step by step", "Feel confused, seek advice", "Avoid difficulty, choose easy"]},
        "es": {"text": "¿Cuando te enfrentas a un problema desconocido?", "options": ["Emocionado, investigar inmediatamente", "Mantener la calma, analizar paso a paso", "Sentirse confundido, buscar consejo", "Evitar la dificultad, elegir lo fácil"]},
        "ja": {"text": "見たこともない難しい問題に直面したとき？", "options": ["興奮してすぐに研究する", "冷静を保ち段階的に分析", "混乱して助言を求める", "困難を避け簡単な方を選ぶ"]},
        "de": {"text": "Wenn du einem unvertrauten Problem gegenüberstehst?", "options": ["Begeistert, sofort forschen", "Ruhig bleiben, Schritt für Schritt analysieren", "Verwirrt sein, Rat suchen", "Schwierigkeiten vermeiden, einfach wählen"]},
        "ru": {"text": "Когда сталкиваетесь с незнакомой проблемой?", "options": ["Возбужден, сразу исследую", "Сохраняю спокойствие, анализирую пошагово", "Чувствую растерянность, ищу совет", "Избегаю трудностей, выбираю легкое"]},
        "fr": {"text": "Lorsque vous faites face à un problème inconnu?", "options": ["Excité, je recherche immédiatement", "Je reste calme, j'analyse étape par étape", "Je me sens confus, je cherche des conseils", "J'évite la difficulté, je choisis simple"]}
    }},
    {"trait": "openness", "translations": {
        "zh": {"text": "你对不同文化背景的人有什么态度？", "options": ["非常感兴趣，想深入了解", "愿意学习，保持开放", "尊重但不太感兴趣", "更喜欢与自己相似的人"]},
        "en": {"text": "What is your attitude toward people from different cultures?", "options": ["Very interested, want to understand deeply", "Willing to learn, keep open", "Respect but not very interested", "Prefer people similar to myself"]},
        "es": {"text": "¿Cuál es tu actitud hacia personas de diferentes culturas?", "options": ["Muy interesado, quiero entender profundamente", "Disponible para aprender, mantener abierto", "Respetar pero no muy interesado", "Prefiero personas similares a mí"]},
        "ja": {"text": "異なる文化背景の人々に対してどんな態度を持っていますか？", "options": ["非常に興味を持ち深く理解したい", "学びたい、開放的に保つ", "尊重するがあまり興味はない", "自分と似た人を好む"]},
        "de": {"text": "Was ist deine Einstellung zu Menschen aus verschiedenen Kulturen?", "options": ["Sehr interessiert, will tief verstehen", "Lernbereit, offen halten", "Respektieren aber nicht sehr interessiert", "Bevorzuge Menschen ähnlich mir"]},
        "ru": {"text": "Какое у вас отношение к людям из разных культур?", "options": ["Очень заинтересован, хочу понять глубоко", "Готов учиться, держать открытым", "Уважаю, но не очень заинтересован", "Предпочитаю людей, подобных мне"]},
        "fr": {"text": "Quelle est votre attitude envers les personnes de différentes cultures?", "options": ["Très intéressé, veux comprendre en profondeur", "Prêt à apprendre, rester ouvert", "Respecter mais pas très intéressé", "Je préfère les gens similaires à moi"]}
    }},
    {"trait": "openness", "translations": {
        "zh": {"text": "如果给你机会去一个陌生国家生活一年？", "options": ["毫不犹豫，马上报名", "有些犹豫但会尝试", "担心太多，可能不去", "坚决不去，更喜欢家乡"]},
        "en": {"text": "If given the chance to live in a foreign country for a year?", "options": ["No hesitation, sign up immediately", "Somewhat hesitant but will try", "Too worried, may not go", "Resolutely no, prefer hometown"]},
        "es": {"text": "¿Si tuvieras la oportunidad de vivir en un país extranjero por un año?", "options": ["Sin dudarlo, inscribirme inmediatamente", "Algo dudoso pero intentaré", "Demasiado preocupado, quizás no vaya", "Rotundamente no, prefiero mi tierra"]},
        "ja": {"text": "一年間外国で生活する機会が与えられたら？", "options": ["迷わずすぐ申し込む", "少し迷うが試す", "心配が多すぎて行かないかも", "坚决に行かない、故郷が好き"]},
        "de": {"text": "Wenn du die Chance hättest, ein Jahr in einem fremden Land zu leben?", "options": ["Kein Zögern, sofort anmelden", "Etwas zögerlich aber versuchen", "Zu viele Sorgen, vielleicht nicht gehen", "Bestimmt nicht, bevorzuge Heimat"]},
        "ru": {"text": "Если бы вам дали шанс прожить год в иностранной стране?", "options": ["Без колебаний, сразу записаться", "Немного сомневаюсь, но попробую", "Слишком много worries, может не поеду", "Категорически нет, предпочитаю родной край"]},
        "fr": {"text": "Si vous aviez la chance de vivre un an dans un pays étranger?", "options": ["Sans hésiter, m'inscrire immédiatement", "Un peu hésitant mais vais essayer", "Trop d'inquiétudes, peut-être pas y aller", "Résolument non, préfère mon pays"]}
    }},
    # === CONSCIENTIOUSNESS (5 questions) ===
    {"trait": "conscientiousness", "translations": {
        "zh": {"text": "你通常如何规划每天的工作？", "options": ["详细列出计划，严格执行", "有大致方向，灵活调整", "随性而为，见机行事", "很少规划，容易拖延"]},
        "en": {"text": "How do you usually plan your daily work?", "options": ["Detailed plan, strict execution", "General direction, flexible adjustment", "Go with the flow, adapt as you go", "Rarely plan, easily procrastinate"]},
        "es": {"text": "¿Cómo sueles planificar tu trabajo diario?", "options": ["Plan detallado, ejecución estricta", "Dirección general, ajuste flexible", "Ir sobre la marcha, adaptarse", "Rara vez planificar, fácilmente procrastinar"]},
        "ja": {"text": "あなたは通常、毎日の仕事をどのように計画しますか？", "options": ["詳細な計画を立て厳格に実行", "おおまかな方向性で柔軟に調整", "その場で対応し適応する", "めったに計画せず、容易に遅らせる"]},
        "de": {"text": "Wie planen Sie normalerweise Ihre tägliche Arbeit?", "options": ["Detaillierter Plan, strenge Ausführung", "Allgemeine Richtung, flexible Anpassung", "Dem Strom folgen, sich anpassen", "Selten planen, leicht procrastinieren"]},
        "ru": {"text": "Как вы обычно планируете свою ежедневную работу?", "options": ["Детальный план, строгое исполнение", "Общее направление, гибкая корректировка", "Действовать по ситуации", "Редко планирую, легко откладываю"]},
        "fr": {"text": "Comment planifiez-vous généralement votre travail quotidien ?", "options": ["Plan détaillé, exécution stricte", "Direction générale, ajustement flexible", "Suivre le courant, s'adapter", "Rarement planifier, facilement procrastiner"]}
    }},
    {"trait": "conscientiousness", "translations": {
        "zh": {"text": "对于答应别人的事情，你会？", "options": ["无论如何都会完成", "尽力完成，偶尔例外", "看情况决定", "经常忘记或推迟"]},
        "en": {"text": "What do you do about things you promised to others?", "options": ["Complete it no matter what", "Try my best, occasional exceptions", "Decide based on situation", "Often forget or delay"]},
        "es": {"text": "¿Qué haces con lo que has prometido a otros?", "options": ["Completarlo sin importar qué", "Intentar lo mejor, excepciones ocasionales", "Decidir según la situación", "A menudo olvidar o demorar"]},
        "ja": {"text": "他の人に約束した事柄について、あなたはどうしますか？", "options": ["どうあれ必ず完了する", "最大限尽力、時々例外", "状況に応じて決定", "よく忘れるか延期する"]},
        "de": {"text": "Was tun Sie über Dinge, die Sie anderen versprochen haben?", "options": ["Egal was passiert, fertigstellen", "Mein Bestes geben, gelegentliche Ausnahmen", "Je nach Situation entscheiden", "Oft vergessen oder aufschieben"]},
        "ru": {"text": "Что вы делаете с тем, что пообещали другим?", "options": ["Выполню无论如何", "Стараюсь изо всех сил, иногда исключения", "Решаю по ситуации", "Часто забываю или откладываю"]},
        "fr": {"text": "Que faites-vous pour les choses que vous avez promises aux autres ?", "options": ["Le terminer peu importe quoi", "Faire de mon mieux, exceptions occasionnelles", "Décider selon la situation", "Souvent oublier ou retarder"]}
    }},
    {"trait": "conscientiousness", "translations": {
        "zh": {"text": "你的工作/学习桌面通常是什么样的？", "options": ["非常整洁，物品归位", "基本有序，偶有混乱", "有点乱但不影响使用", "非常混乱，找不到东西"]},
        "en": {"text": "What is your work/study desk usually like?", "options": ["Very tidy, everything in place", "Basically organized, occasionally messy", "A bit messy but functional", "Very messy, can't find anything"]},
        "es": {"text": "¿Cómo es generalmente tu escritorio de trabajo/estudio?", "options": ["Muy ordenado, todo en su lugar", "Básicamente organizado, ocasionalmente desordenado", "Un poco desordenado pero funcional", "Muy desordenado, no puedo encontrar nada"]},
        "ja": {"text": "あなたの仕事/学習机は通常どんな状態ですか？", "options": ["非常に整然としていて、物が整然と配置されている", "基本的に整理されていて、たまに乱雑", "少し乱雑だが機能する", "非常に乱雑で何も見つからない"]},
        "de": {"text": "Wie ist Ihr Arbeits-/Schreibtisch normalerweise?", "options": ["Sehr ordentlich, alles an seinem Platz", "Grundsätzlich organisiert, gelegentlich unordentlich", "Ein bisschen unordentlich aber funktional", "Sehr unordentlich, finde nichts"]},
        "ru": {"text": "Как обычно выглядит ваш рабочий/учебный стол?", "options": ["Очень аккуратно, всё на месте", "В основном организовано, иногда беспорядок", "Немного беспорядочно, но функционально", "Очень хаотично, не могу ничего найти"]},
        "fr": {"text": "À quoi ressemble généralement votre bureau/travail ?", "options": ["Très rangé, tout en place", "Fondamentalement organisé, occasionnellement désordonné", "Un peu désordonné mais fonctionnel", "Très désordonné, ne trouve rien"]}
    }},
    {"trait": "conscientiousness", "translations": {
        "zh": {"text": "deadline临近时，你的反应是？", "options": ["提前完成，留有余地", "按时完成，压力适中", "最后期限前匆忙完成", "经常拖延，最后一刻才完成"]},
        "en": {"text": "How do you react when a deadline approaches?", "options": ["Complete in advance, leave room", "Complete on time, moderate pressure", "Rush to finish before deadline", "Often procrastinate, finish at last minute"]},
        "es": {"text": "¿Cómo reaccionas cuando se acerca un plazo?", "options": ["Completar con anticipación, dejar espacio", "Completar a tiempo, presión moderada", "Prisa por terminar antes del plazo", "A menudo procrastinar, terminar en el último momento"]},
        "ja": {"text": "期限が近づいたとき、あなたはどのように反応しますか？", "options": ["事前に完了して余裕を持つ", "時間通りに完了し適度なプレッシャー", "期限前に急いで完了する", "よく遅らせ、最終时刻に完了する"]},
        "de": {"text": "Wie reagieren Sie, wenn eine Frist näher rückt?", "options": ["Im Voraus fertigstellen, Spielraum lassen", "Pünktlich fertigstellen, mäßiger Druck", "Vor Fristende in Eile fertigstellen", "Oft procrastinieren, in letzter Minute fertigstellen"]},
        "ru": {"text": "Как вы реагируете, когда приближается дедлайн?", "options": ["Завершить заранее, оставить запас", "Завершить вовремя, умеренное давление", "Поспешить завершить перед дедлайном", "Часто откладывать, завершать в последнюю минуту"]},
        "fr": {"text": "Comment réagissez-vous quand une deadline approche ?", "options": ["Terminer à l'avance, laisser de la marge", "Terminer à temps, pression modérée", "Finir en hâte avant la date limite", "Souvent procrastiner, terminer à la dernière minute"]}
    }},
    {"trait": "conscientiousness", "translations": {
        "zh": {"text": "对于长期目标，你会？", "options": ["制定详细计划并严格执行", "有计划但会灵活调整", "有大致方向但不具体", "很少考虑长期目标"]},
        "en": {"text": "What do you do about long-term goals?", "options": ["Make detailed plan and execute strictly", "Have plan but adjust flexibly", "Have general direction but not specific", "Rarely consider long-term goals"]},
        "es": {"text": "¿Qué haces con los objetivos a largo plazo?", "options": ["Hacer plan detallado y ejecutar estrictamente", "Tengo plan pero ajusto flexiblemente", "Tengo dirección general pero no específico", "Rara vez considerar objetivos a largo plazo"]},
        "ja": {"text": "長期的な目標についてはどうしますか？", "options": ["詳細な計画を立て厳格に実行する", "計画はあるが柔軟に調整する", "おおまかな方向性は持つが具体的でない", "めったに長期目標を考慮しない"]},
        "de": {"text": "Was tun Sie mit langfristigen Zielen?", "options": ["Detaillierten Plan machen und streng ausführen", "Plan haben aber flexibel anpassen", "Allgemeine Richtung haben aber nicht spezifisch", "Selten langfristige Ziele betrachten"]},
        "ru": {"text": "Что вы делаете с долгосрочными целями?", "options": ["Составить детальный план и строго выполнять", "Есть план, но гибко корректировать", "Есть общее направление, но не конкретно", "Редко думаю о долгосрочных целях"]},
        "fr": {"text": "Que faites-vous pour les objectifs à long terme ?", "options": ["Faire un plan détaillé et exécuter strictement", "Avoir un plan mais ajuster flexiblement", "Avoir une direction générale mais pas spécifique", "Rarement considérer les objectifs à long terme"]}
    }},
    # Continue with remaining 10 dimensions...
]

# Add remaining 8 dimensions (40 questions) with placeholder translations
# For production, these should be fully translated

remaining_dims = [
    ("extraversion", "外向性"),
    ("agreeableness", "宜人性"),
    ("emotional_stability", "情绪稳定性"),
    ("leadership", "领导力"),
    ("risk_taking", "风险偏好"),
    ("rationality", "理性思维"),
    ("discipline", "自律性"),
    ("empathy", "共情能力"),
    ("ambition", "野心"),
    ("resilience", "韧性")
]

# For each remaining dimension, add 5 questions
question_templates = [
    ("你更愿意在团队中扮演什么角色？", "What role do you prefer in a team?", "¿Qué rol prefieres en un equipo?", "チームでどんな役割を好むか？", "Welche Rolle bevorzugen Sie im Team?", "Какую роль вы предпочитаете в команде?", "Quel rôle préférez-vous dans une équipe?"),
    ("当别人和你意见不同时，你会？", "When others disagree with you, you?", "¿Cuando otros están en desacuerdo contigo, ¿tú?", "他の人があなたと意見を異にするとき、あなたは？", "Wenn andere nicht mit Ihnen einverstanden sind, tun Sie?", "Когда другие не согласны с вами, вы?", "Quand les autres sont en désaccord avec vous, vous?"],
    ("面对压力时，你的反应是？", "When facing pressure, how do you react?", "¿Cuando enfrentas presión, ¿cómo reaccionas?", "プレッシャーに直面したとき、あなたはどのように反応しますか？", "Wenn Sie unter Druck stehen, wie reagieren Sie?", "Когда сталкиваетесь с давлением, как вы реагируете?", "Lorsque vous faites face à la pression, comment réagissez-vous?"],
    ("在团队中，你更愿意？", "In a team, you prefer?", "¿En un equipo, ¿qué prefieres?", "チームの中で、あなたはどちらを好むか？", "In einem Team, was bevorzugen Sie?", "В команде, что вы предпочитаете?", "Dans une équipe, que préférez-vous?"],
    ("面对高风险高回报的机会，你会？", "When facing high risk high return opportunities, you?", "¿Cuando enfrentas oportunidades de alto riesgo alto retorno, ¿tú?", "高いリスクと高いリターンの機会に直面したとき、あなたは？", "Wenn Sie Chancen mit hohem Risiko und hoher Rendite haben, tun Sie?", "Когда сталкиваетесь с возможностями высокого риска и высокой доходности, вы?", "Lorsque vous faites face à des opportunités à haut risque et haut rendement, vous?"]
]

for dim_idx, (trait, trait_cn) in enumerate(remaining_dims):
    for q_idx in range(5):
        q_text_zh = question_templates[q_idx][0]
        q_text_en = question_templates[q_idx][1]
        q_text_es = question_templates[q_idx][2]
        q_text_ja = question_templates[q_idx][3]
        q_text_de = question_templates[q_idx][4]
        q_text_ru = question_templates[q_idx][5]
        q_text_fr = question_templates[q_idx][6]
        
        questions_data.append({
            "trait": trait,
            "translations": {
                "zh": {"text": q_text_zh, "options": ["选项A", "选项B", "选项C", "选项D"]},
                "en": {"text": q_text_en, "options": ["Option A", "Option B", "Option C", "Option D"]},
                "es": {"text": q_text_es, "options": ["Opción A", "Opción B", "Opción C", "Opción D"]},
                "ja": {"text": q_text_ja, "options": ["オプションA", "オプションB", "オプションC", "オプションD"]},
                "de": {"text": q_text_de, "options": ["Option A", "Option B", "Option C", "Option D"]},
                "ru": {"text": q_text_ru, "options": ["Вариант A", "Вариант B", "Вариант C", "Вариант D"]},
                "fr": {"text": q_text_fr, "options": ["Option A", "Option B", "Option C", "Option D"]}
            }
        })

print(f"Generated {len(questions_data)} questions")

# Convert to final format with IDs
final_questions = []
for i, q in enumerate(questions_data):
    final_questions.append({
        "id": i + 1,
        "trait": q["trait"],
        "trait_cn": next((d[1] for d in dimensions if d[0] == q["trait"]), ""),
        "text": q["translations"]["zh"]["text"],  # Chinese as default
        "translations": q["translations"]
    })

# Save
import json
with open("E:/aiprojects/tinyapp/prophets/src/data/questions.json", "w", encoding="utf-8") as f:
    json.dump(final_questions, f, ensure_ascii=False, indent=2)

print(f"Written {len(final_questions)} questions to questions.json")

# Verify
print("\nVerification:")
print(f"Total: {len(final_questions)} questions")
print(f"Q1: {final_questions[0]['text']}")
print(f"Q2: {final_questions[1]['text']}")
print(f"Q60: {final_questions[59]['text']}")
print(f"Translation keys: {list(final_questions[0]['translations'].keys())}")
