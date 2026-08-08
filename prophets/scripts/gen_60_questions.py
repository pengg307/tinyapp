#!/usr/bin/env python3
"""Generate 60 multilingual questions - 12 dimensions x 5 questions each"""
import json

# Question templates for all 12 dimensions
question_templates = [
    # OPENNESS (5)
    {"trait": "openness", "trait_cn": "开放性",
     "texts": {
         "zh": ["面对全新的领域，你的态度是？", "你更喜欢尝试新事物还是坚持传统？", "当面对一个从未见过的难题时？", "你对不同文化背景的人有什么态度？", "如果给你机会去一个陌生国家生活一年？"],
         "en": ["How do you approach a completely new field?", "Do you prefer trying new things or sticking to tradition?", "When facing an unfamiliar problem?", "What is your attitude toward people from different cultures?", "If given the chance to live in a foreign country for a year?"],
         "es": ["¿Cómo te enfrentas a un campo completamente nuevo?", "¿Prefieres probar cosas nuevas o mantenerte en la tradición?", "¿Cuando te enfrentas a un problema desconocido?", "¿Cuál es tu actitud hacia personas de diferentes culturas?", "¿Si tuvieras la oportunidad de vivir en un país extranjero por un año?"],
         "ja": ["全く新しい分野に直面したとき、あなたの態度は？", "新しい物事を試すことを好むか、伝統を守るかを好むか？", "見たこともない難しい問題に直面したとき？", "異なる文化背景の人々に対してどんな態度を持っていますか？", "一年間外国で生活する機会が与えられたら？"],
         "de": ["Wie gehst du einem völlig neuen Gebiet gegenüber?", "Bevorzugst du neue Dinge auszuprobieren oder an der Tradition festzuhalten?", "Wenn du einem unvertrauten Problem gegenüberstehst?", "Was ist deine Einstellung zu Menschen aus verschiedenen Kulturen?", "Wenn du die Chance hättest, ein Jahr in einem fremden Land zu leben?"],
         "ru": ["Как вы подходите к совершенно новой области?", "Вы предпочитаете пробовать новое или придерживаться традиций?", "Когда сталкиваетесь с незнакомой проблемой?", "Какое у вас отношение к людям из разных культур?", "Если бы вам дали шанс прожить год в иностранной стране?"],
         "fr": ["Comment abordez-vous un domaine complètement nouveau?", "Préférez-vous essayer de nouvelles choses ou rester dans la tradition?", "Lorsque vous faites face à un problème inconnu?", "Quelle est votre attitude envers les personnes de différentes cultures?", "Si vous aviez la chance de vivre un an dans un pays étranger?"]
     },
     "options": {
         "zh": ["充满好奇，积极尝试", "适度接受，但保持谨慎", "更倾向于熟悉的事物", "坚持传统，不喜变化"],
         "en": ["Full of curiosity, actively try", "Moderately accept, but cautious", "Prefer familiar things", "Stick to tradition, dislike change"],
         "es": ["Con mucha curiosidad, probar activamente", "Aceptar moderadamente, pero con cautela", "Prefiero cosas conocidas", "Mantenerse en la tradición, no me gusta el cambio"],
         "ja": ["好奇心満タンで積極的に挑戦", "適度に受け入れるが慎重に", "慣れたものに傾く", "伝統を守り変化を嫌う"],
         "de": ["Voll Neugier, aktiv ausprobieren", "Mäßig akzeptieren, aber vorsichtig", "Eher Vertrautes bevorzugen", "An der Tradition festhalten, keine Veränderung"],
         "ru": ["Полный любопытства, активно пробую", "Умеренно принимаю, но осторожно", "Предпочитаю знакомое", "Держусь традиций, не люблю перемен"],
         "fr": ["Plein de curiosité, j'essaie activement", "J'accepte modérément mais prudemment", "Je préfère les choses familières", "Je reste dans la tradition, je déteste le changement"]
     }},
    # CONSCIENTIOUSNESS (5)
    {"trait": "conscientiousness", "trait_cn": "尽责性",
     "texts": {
         "zh": ["你通常如何规划每天的工作？", "对于答应别人的事情，你会？", "你的工作/学习桌面通常是什么样的？", "deadline临近时，你的反应是？", "对于长期目标，你会？"],
         "en": ["How do you usually plan your daily work?", "What do you do about things you promised to others?", "What is your work/study desk usually like?", "How do you react when a deadline approaches?", "What do you do about long-term goals?"],
         "es": ["¿Cómo sueles planificar tu trabajo diario?", "¿Qué haces con lo que has prometido a otros?", "¿Cómo es generalmente tu escritorio de trabajo/estudio?", "¿Cómo reaccionas cuando se acerca un plazo?", "¿Qué haces con los objetivos a largo plazo?"],
         "ja": ["あなたは通常、毎日の仕事をどのように計画しますか？", "他の人に約束した事柄について、あなたはどうしますか？", "あなたの仕事/学習机は通常どんな状態ですか？", "期限が近づいたとき、あなたはどのように反応しますか？", "長期的な目標についてはどうしますか？"],
         "de": ["Wie planen Sie normalerweise Ihre tägliche Arbeit?", "Was tun Sie über Dinge, die Sie anderen versprochen haben?", "Wie ist Ihr Arbeits-/Schreibtisch normalerweise?", "Wie reagieren Sie, wenn eine Frist näher rückt?", "Was tun Sie mit langfristigen Zielen?"],
         "ru": ["Как вы обычно планируете свою ежедневную работу?", "Что вы делаете с тем, что пообещали другим?", "Как обычно выглядит ваш рабочий/учебный стол?", "Как вы реагируете, когда приближается дедлайн?", "Что вы делаете с долгосрочными целями?"],
         "fr": ["Comment planifiez-vous généralement votre travail quotidien ?", "Que faites-vous pour les choses que vous avez promises aux autres ?", "À quoi ressemble généralement votre bureau/travail ?", "Comment réagissez-vous quand une deadline approche ?", "Que faites-vous pour les objectifs à long terme ?"]
     },
     "options": {
         "zh": ["详细列出计划，严格执行", "有大致方向，灵活调整", "随性而为，见机行事", "很少规划，容易拖延"],
         "en": ["Detailed plan, strict execution", "General direction, flexible adjustment", "Go with the flow, adapt as you go", "Rarely plan, easily procrastinate"],
         "es": ["Plan detallado, ejecución estricta", "Dirección general, ajuste flexible", "Ir sobre la marcha, adaptarse", "Rara vez planificar, fácilmente procrastinar"],
         "ja": ["詳細な計画を立て厳格に実行", "おおまかな方向性で柔軟に調整", "その場で対応し適応する", "めったに計画せず、容易に遅らせる"],
         "de": ["Detaillierter Plan, strenge Ausführung", "Allgemeine Richtung, flexible Anpassung", "Dem Strom folgen, sich anpassen", "Selten planen, leicht procrastinieren"],
         "ru": ["Детальный план, строгое исполнение", "Общее направление, гибкая корректировка", "Действовать по ситуации", "Редко планирую, легко откладываю"],
         "fr": ["Plan détaillé, exécution stricte", "Direction générale, ajustement flexible", "Suivre le courant, s'adapter", "Rarement planifier, facilement procrastiner"]
     }},
    # EXTROVERSION (5)
    {"trait": "extraversion", "trait_cn": "外向性",
     "texts": {
         "zh": ["在社交聚会中，你通常会？", "周末你更愿意？", "新认识一个人时，你会？", "团队项目中，你通常扮演什么角色？", "参加完大型活动后，你通常需要？"],
         "en": ["In social gatherings, you usually?", "What do you prefer on weekends?", "When meeting someone new, you?", "In team projects, what role do you usually play?", "After attending a large event, you usually need?"],
         "es": ["En reuniones sociales, ¿tú usualmente?", "¿Qué prefieres los fines de semana?", "Cuando conoces a alguien nuevo, ¿tú?", "En proyectos de equipo, ¿qué rol usualmente juegas?", "Después de asistir a un evento grande, ¿qué necesitas usualmente?"],
         "ja": ["社交の集まりでは、あなたは通常？", "週末はどちらかというと？", "新しい人に出会ったとき、あなたは？", "チームプロジェクトでは、あなたは通常どんな役割？", "大きなイベントに参加した後、あなたは通常需要？"],
         "de": ["In sozialen gatherings, was tun Sie normalerweise?", "Was bevorzugen Sie am Wochenende?", "Wenn Sie jemanden neu kennenlernen, tun Sie?", "In Team-Projekten, welche Rolle spielen Sie normalerweise?", "Nach einer großen Veranstaltung, was brauchen Sie normalerweise?"],
         "ru": ["На социальных встречах, вы обычно?", "Что вы предпочитаете на выходные?", "Когда встречаете нового человека, вы?", "В командных проектах, какую роль вы обычно играете?", "После крупного мероприятия, что вам обычно нужно?"],
         "fr": ["Dans les réunions sociales, vous faites quoi habituellement ?", "Que préférez-vous le week-end ?", "Quand vous rencontrez quelqu'un de nouveau, vous?", "Dans les projets d'équipe, quel rôle jouez-vous habituellement ?", "Après un grand événement, qu'avez-vous généralement besoin ?"]
     },
     "options": {
         "zh": ["主动与人交流，享受其中", "与熟人交谈，偶尔结识新人", "在一旁观察，不多说话", "寻找角落，希望早点离开"],
         "en": ["Actively communicate with others, enjoy it", "Talk with acquaintances, occasionally meet new people", "Observe from the side, don't talk much", "Find a corner, hope to leave early"],
         "es": ["Comunicarme activamente con otros, disfrutarlo", "Hablar con conocidos, ocasionalmente conocer gente nueva", "Observar desde un lado, no hablar mucho", "Buscar un rincón, esperar salir temprano"],
         "ja": ["積極的に他人と交流し楽しむ", "知人と話し、たまに新しい人に出会う", "横で観察しあまり話さない", "隅を見つけて早く去りたい"],
         "de": ["Aktiv mit anderen kommunizieren, es genießen", "Mit Bekannten sprechen, gelegentlich neue Leute treffen", "Von der Seite beobachten, nicht viel reden", "Eine Ecke suchen, hoffe früh zu gehen"],
         "ru": ["Активно общаться с другими, получать удовольствие", "Говорить с знакомыми, иногда встречать новых людей", "Наблюдать со стороны, мало говорить", "Искать угол, надеюсь уйти рано"],
         "fr": ["Communiquer activement avec les autres, profiter", "Parler avec des connaissances, rencontrer occasionnellement de nouvelles personnes", "Observer de côté, pas beaucoup parler", "Trouver un coin, espérer partir tôt"]
     }},
    # AGREEABLENESS (5)
    {"trait": "agreeableness", "trait_cn": "宜人性",
     "texts": {
         "zh": ["当别人和你意见不同时，你会？", "你更愿意相信大多数人还是坚持自己的观点？", "对于不熟悉的人，你的态度是？", "团队合作中，你更愿意？", "当有人需要帮助时，你会？"],
         "en": ["When others disagree with you, you?", "Do you prefer to trust most people or stick to your own view?", "What is your attitude toward strangers?", "In team collaboration, you prefer?", "When someone needs help, you?"],
         "es": ["Cuando otros están en desacuerdo contigo, ¿tú?", "¿Prefieres confiar en la mayoría o mantener tu propia opinión?", "¿Cuál es tu actitud hacia los desconocidos?", "En colaboración de equipo, ¿qué prefieres?", "Cuando alguien necesita ayuda, ¿tú?"],
         "ja": ["他の人があなたと意見を異にするとき、あなたは？", "あなたは大多数を信じることを好むか、自分の意見を堅持することを好むか？", "見知らぬ人に対してどんな態度を持っていますか？", "チーム協力の中では、あなたはどちらを好むか？", "誰かが助けを必要としているとき、あなたは？"],
         "de": ["Wenn andere nicht mit Ihnen einverstanden sind, tun Sie?", "Bevorzugen Sie den meisten Menschen zu vertrauen oder an Ihrer eigenen Meinung festzuhalten?", "Was ist Ihre Einstellung gegenüber Fremden?", "In Team-Zusammenarbeit, was bevorzugen Sie?", "Wenn jemand Hilfe braucht, tun Sie?"],
         "ru": ["Когда другие не согласны с вами, вы?", "Вы предпочитаете доверять большинству или придерживаться своего мнения?", "Какое у вас отношение к незнакомцам?", "В командной работе, что вы предпочитаете?", "Когда кто-то нуждается в помощи, вы?"],
         "fr": ["Quand les autres sont en désaccord avec vous, vous?", "Préférez-vous faire confiance à la majorité ou rester sur votre propre avis?", "Quelle est votre attitude envers les inconnus?", "Dans la collaboration d'équipe, que préférez-vous?", "Quand quelqu'un a besoin d'aide, vous?"]
     },
     "options": {
         "zh": ["理解包容，寻求共识", "坚持己见，据理力争", "保持距离，避免冲突", "顺从妥协，不想争论"],
         "en": ["Understand and seek consensus", "Stand your ground, argue your case", "Keep distance, avoid conflict", "Comply and compromise, don't want to argue"],
         "es": ["Entender y buscar consenso", "Mantener tu postura, argumentar tu caso", "Mantener distancia, evitar conflicto", "Cumplir y comprometerse, no quiero discutir"],
         "ja": ["理解し合意を求める", "自分の立場を貫き、主張する", "距離を保ち、衝突を避ける", "従い妥協し、議論したくない"],
         "de": ["Verstehen und Konsens suchen", "An Ihrer Position festhalten, Ihren Fall argumentieren", "Distanz wahren, Konflikt vermeiden", "Zustimmen und kompromittieren, nicht streiten wollen"],
         "ru": ["Понимать и искать консенсус", "Настаивать на своем, спорить", "Держать дистанцию, избегать конфликта", "Соглашаться и компромисс, не хочу спорить"],
         "fr": ["Comprendre et chercher consensus", "Rester ferme sur votre position, argumenter", "Garder vos distances, éviter le conflit", "Se conformer et faire des compromis, ne pas vouloir discuter"]
     }},
    # NEUROTICISM (5)
    {"trait": "neuroticism", "trait_cn": "情绪稳定性",
     "texts": {
         "zh": ["面对压力时，你的反应是？", "你对未来的担忧程度如何？", "遇到挫折时，你通常？", "你的情绪波动大吗？", "你容易焦虑吗？"],
         "en": ["When facing pressure, how do you react?", "How worried are you about the future?", "When encountering setbacks, you usually?", "Do you have big mood swings?", "Are you prone to anxiety?"],
         "es": ["Cuando enfrentas presión, ¿cómo reaccionas?", "¿Qué tanto te preocupas por el futuro?", "Cuando encuentras contratiempos, ¿tú usualmente?", "¿Tienes grandes cambios de humor?", "¿Eres propenso a la ansiedad?"],
         "ja": ["プレッシャーに直面したとき、あなたはどのように反応しますか？", "あなたは未来についてどれくらい心配していますか？", "挫折に出会ったとき、あなたは通常？", "あなたの気分の浮き沈みは大きいですか？", "あなたは不安になりやすいですか？"],
         "de": ["Wenn Sie unter Druck stehen, wie reagieren Sie?", "Wie besorgt sind Sie über die Zukunft?", "Wenn Sie Rückschläge erleben, tun Sie normalerweise?", "Haben Sie große Stimmungsschwankungen?", "Sind Sie anfällig für Angst?"],
         "ru": ["Когда сталкиваетесь с давлением, как вы реагируете?", "Насколько вы беспокоитесь о будущем?", "Когда сталкиваетесь с неудачами, вы обычно?", "У вас большие перепады настроения?", "Вы склонны к тревоге?"],
         "fr": ["Lorsque vous faites face à la pression, comment réagissez-vous ?", "À quel point vous inquiétez-vous de l'avenir ?", "Lorsque vous rencontrez des revers, vous faites quoi habituellement ?", "Avez-vous de grands sauts d'humeur ?", "Êtes-vous sujet à l'anxiété ?"]
     },
     "options": {
         "zh": ["从容应对，很快恢复", "适度紧张，但能控制", "容易焦虑，需要时间平复", "经常焦虑，难以放松"],
         "en": ["Handle calmly, recover quickly", "Moderately nervous, but can control", "Easily anxious, need time to calm down", "Often anxious, hard to relax"],
         "es": ["Manejar con calma, recuperarse rápidamente", "Moderadamente nervioso, pero puedo controlar", "Fácilmente ansioso, necesito tiempo para calmarme", "A menudo ansioso, difícil relajarse"],
         "ja": ["落ち着いて対応し、すぐに回復する", "適度に緊張するがコントロールできる", "簡単に不安になり、落ち着くのに時間がかかる", "頻繁に不安で、リラックス难以"],
         "de": ["Ruhig handeln, schnell erholen", "Mäßig nervös, aber kontrollieren können", "Leicht ängstlich, brauche Zeit zum Beruhigen", "Oft ängstlich, schwer zu entspannen"],
         "ru": ["Спокойно справляться, быстро восстановиться", "Умеренно нервно, но могу контролировать", "Легко тревожусь, нужно время чтобы успокоиться", "Часто тревожусь, трудно расслабиться"],
         "fr": ["Gérer calmement, récupérer rapidement", "Modérément nerveux, mais peux contrôler", "Facilement anxieux, besoin de temps pour me calmer", "Souvent anxieux, difficile de se détendre"]
     }},
    # LEADERSHIP (5)
    {"trait": "leadership", "trait_cn": "领导力",
     "texts": {
         "zh": ["在团队中，你更愿意？", "面对分歧时，你会？", "分配任务时，你通常？", "团队遇到困难时，你？", "对于团队目标，你？"],
         "en": ["In a team, you prefer?", "When facing disagreements, you?", "When assigning tasks, you usually?", "When the team faces difficulties, you?", "Regarding team goals, you?"],
         "es": ["En un equipo, ¿qué prefieres?", "Cuando enfrentas desacuerdos, ¿tú?", "Cuando asignas tareas, ¿tú usualmente?", "Cuando el equipo enfrenta dificultades, ¿tú?", "En cuanto a objetivos del equipo, ¿tú?"],
         "ja": ["チームの中で、あなたはどちらを好むか？", "意見の相違に直面したとき、あなたは？", "タスクを割り当てる際、あなたは通常？", "チームが困難に直面したとき、あなたは？", "チームの目標に関して、あなたは？"],
         "de": ["In einem Team, was bevorzugen Sie?", "Wenn Sie unterschiedlicher Meinung sind, tun Sie?", "Wenn Sie Aufgaben zuweisen, tun Sie normalerweise?", "Wenn das Team Schwierigkeiten hat, tun Sie?", "Bezüglich Team-Ziele, tun Sie?"],
         "ru": ["В команде, что вы предпочитаете?", "Когда сталкиваетесь с разногласиями, вы?", "Когда назначаете задачи, вы обычно?", "Когда команда сталкивается с трудностями, вы?", "Относительно командных целей, вы?"],
         "fr": ["Dans une équipe, que préférez-vous ?", "Lorsque vous avez des désaccords, vous?", "Lorsque vous assignez des tâches, vous faites quoi habituellement ?", "Quand l'équipe fait face à des difficultés, vous?", "En ce qui concerne les objectifs d'équipe, vous?"]
     },
     "options": {
         "zh": ["主动承担领导责任", "积极参与讨论", "配合他人，执行任务", "较少参与决策"],
         "en": ["Take initiative to lead", "Actively participate in discussion", "Cooperate with others, execute tasks", "Less involved in decision making"],
         "es": ["Tomar la iniciativa de liderar", "Participar activamente en la discusión", "Cooperar con otros, ejecutar tareas", "Menos involucrado en la toma de decisiones"],
         "ja": ["リーダーシップを取るのが好き", "議論に積極的に参加する", "他人と協力し、タスクを執行する", "意思決定への参加は少ない"],
         "de": ["Initiative ergreifen zu führen", "Aktiv an der Diskussion teilnehmen", "Mit anderen zusammenarbeiten, Aufgaben ausführen", "Weniger in Entscheidungsprozessen involviert"],
         "ru": ["Взять на себя ответственность лидера", "Активно участвовать в обсуждении", "Сотрудничать с другими, выполнять задачи", "Мало участвует в принятии решений"],
         "fr": ["Prendre l'initiative de diriger", "Participer activement à la discussion", "Coopérer avec les autres, exécuter les tâches", "Moins impliqué dans la prise de décision"]
     }},
    # RISK TAKING (5)
    {"trait": "risk_taking", "trait_cn": "风险偏好",
     "texts": {
         "zh": ["面对高风险高回报的机会，你会？", "做重大决定时，你通常？", "你对未知事物的态度是？", "在投资方面，你更倾向？", "面对人生重大选择时？"],
         "en": ["When facing high risk high return opportunities, you?", "When making major decisions, you usually?", "What is your attitude toward the unknown?", "In investments, you tend to?", "When facing major life choices?"],
         "es": ["Cuando enfrentas oportunidades de alto riesgo alto retorno, ¿tú?", "Cuando tomas decisiones importantes, ¿tú usualmente?", "¿Cuál es tu actitud hacia lo desconocido?", "En inversiones, ¿tú tiendes a?", "¿Cuando enfrentas elecciones importantes de vida?"],
         "ja": ["高いリスクと高いリターンの機会に直面したとき、あなたは？", "重要な決断をするとき、あなたは通常？", "未知の事物に対するあなたの態度は？", "投資面では、あなたはどちらを倾向するか？", "人生の重要な選択に直面したとき？"],
         "de": ["Wenn Sie Chancen mit hohem Risiko und hoher Rendite haben, tun Sie?", "Wenn Sie wichtige Entscheidungen treffen, tun Sie normalerweise?", "Was ist Ihre Einstellung zum Unbekannten?", "Bei Investitionen, neigen Sie zu?", "Wenn Sie wichtige Lebensentscheidungen treffen?"],
         "ru": ["Когда сталкиваетесь с возможностями высокого риска и высокой доходности, вы?", "Когда принимаете важные решения, вы обычно?", "Какое у вас отношение к неизвестному?", "В инвестициях, вы склонны к?", "Когда сталкиваетесь с важными жизненными выборами?"],
         "fr": ["Lorsque vous faites face à des opportunités à haut risque et haut rendement, vous?", "Lorsque vous prenez des décisions importantes, vous faites quoi habituellement ?", "Quelle est votre attitude envers l'inconnu ?", "En investissement, vous tendez à?", "Lorsque vous faites face à des choix importants de vie?"]
     },
     "options": {
         "zh": ["果断接受，敢于冒险", "谨慎评估，适度冒险", "偏向保守，规避风险", "坚决拒绝，安全第一"],
         "en": ["Decisively accept, dare to take risks", "Carefully evaluate, moderate risk", "Lean conservative, avoid risks", "Firmly refuse, safety first"],
         "es": ["Aceptar decididamente, atreverse a correr riesgos", "Evaluar cuidadosamente, riesgo moderado", "Tender conservador, evitar riesgos", "Rechazar firmemente, seguridad primero"],
         "ja": ["断固として受け入れ、冒険する", "慎重に評価し、適度なリスク", "保守的に傾き、リスクを回避", "坚决に拒绝し、安全第一"],
         "de": ["Entschieden akzeptieren, Risiken eingehen", "Sorgfältig bewerten, moderates Risiko", "Konservativ neigen, Risiken vermeiden", "Bestimmt ablehnen, Sicherheit zuerst"],
         "ru": ["Решительно принять, осмелиться рисковать", "Тщательно оценить, умеренный риск", "Склоняться к консерватизму, избегать рисков", "Категорически отказаться, безопасность прежде всего"],
         "fr": ["Accepter décisivement, oser prendre des risques", "Évaluer soigneusement, risque modéré", "Tendre vers la prudence, éviter les risques", "Refuser fermement, sécurité d'abord"]
     }},
    # RATIONALITY (5)
    {"trait": "rationality", "trait_cn": "理性思维",
     "texts": {
         "zh": ["做重要决定前，你会？", "面对情绪化的人，你的反应是？", "处理问题时，你更偏向？", "你相信直觉还是逻辑？", "遇到争议时，你通常？"],
         "en": ["Before making important decisions, you?", "Facing emotional people, how do you react?", "When handling problems, you lean toward?", "Do you believe in intuition or logic?", "When encountering disputes, you usually?"],
         "es": ["Antes de tomar decisiones importantes, ¿tú?", "Cuando te enfrentas a personas emocionales, ¿cómo reaccionas?", "Cuando manejas problemas, ¿tú tiendes a?", "¿Crees en la intuición o en la lógica?", "Cuando encuentras disputas, ¿tú usualmente?"],
         "ja": ["重要な決断をする前に、あなたは？", "感情的な人に向き合ったとき、あなたはどのように反応しますか？", "問題を処理する際、あなたはどちらに傾くか？", "あなたは直感を信じるか、論理を信じるか？", "紛争に出会ったとき、あなたは通常？"],
         "de": ["Bevor Sie wichtige Entscheidungen treffen, tun Sie?", "Wenn Sie emotionalen Menschen gegenüberstehen, wie reagieren Sie?", "Bei der Bewältigung von Problemen, neigen Sie zu?", "Glauben Sie an Intuition oder Logik?", "Wenn Sie auf Streitigkeiten stoßen, tun Sie normalerweise?"],
         "ru": ["Перед важными решениями, вы?", "Когда сталкиваетесь с эмоциональными людьми, как вы реагируете?", "Когда решаете проблемы, вы склонны к?", "Вы верите в интуицию или логику?", "Когда сталкиваетесь с спорами, вы обычно?"],
         "fr": ["Avant de prendre des décisions importantes, vous?", "Face à des personnes émotionnelles, comment réagissez-vous ?", "Lorsque vous gérez des problèmes, vous penchez vers?", "Croyez-vous en l'intuition ou la logique ?", "Lorsque vous rencontrez des disputes, vous faites quoi habituellement ?"]
     },
     "options": {
         "zh": ["理性分析，权衡利弊", "考虑情感因素，适度理性", "依赖直觉，偶尔分析", "凭感觉行事，很少思考"],
         "en": ["Rational analysis, weigh pros and cons", "Consider emotional factors, moderately rational", "Rely on intuition, occasionally analyze", "Act on feeling, rarely think"],
         "es": ["Análisis racional, sopesar pros y contras", "Considerar factores emocionales, moderadamente racional", "Confiar en la intuición, ocasionalmente analizar", "Actuar por sentimiento, rara vez pensar"],
         "ja": ["理性的に分析し、利弊を权衡する", "感情的要素を考慮し、適度に理性的", "直感に頼り、 occasionally 分析", "感覚で行動し、めったに考えない"],
         "de": ["Rationale Analyse, Vor- und Nachteile abwägen", "Emotionale Faktoren berücksichtigen, mäßig rational", "Auf Intuition verlassen, gelegentlich analysieren", "Nach Gefühl handeln, selten denken"],
         "ru": ["Рациональный анализ, взвешивать плюсы и минусы", "Учитывать эмоциональные факторы, умеренно рационально", "Полагаться на интуицию, иногда анализировать", "Действовать по ощущениям, редко думать"],
         "fr": ["Analyse rationnelle, peser le pour et le contre", "Considérer les facteurs émotionnels, modérément rationnel", "Compter sur l'intuition, analyser occasionnellement", "Agir selon le sentiment, rarement réfléchir"]
     }},
    # DISCIPLINE (5)
    {"trait": "discipline", "trait_cn": "自律性",
     "texts": {
         "zh": ["你很难抵制诱惑吗？", "你能坚持每天锻炼吗？", "对于制定的计划，你？", "你容易分心吗？", "你有固定的作息吗？"],
         "en": ["Is it hard for you to resist temptation?", "Can you stick to daily exercise?", "Regarding made plans, you?", "Do you get distracted easily?", "Do you have a fixed routine?"],
         "es": ["¿Te cuesta resistir las tentaciones?", "¿Puedes mantener el ejercicio diario?", "Respecto a los planes hechos, ¿tú?", "¿Te distraes fácilmente?", "¿Tienes una rutina fija?"],
         "ja": ["誘惑に抵抗するのは難しいですか？", "毎日運動を続けることができますか？", "作った計画については、あなたは？", "あなたは簡単に気を散らされますか？", "決まった生活リズムがありますか？"],
         "de": ["Ist es schwer für Sie, Versuchungen zu widerstehen?", "Können Sie täglich Sport machen?", "Bezüglich gemachter Pläne, tun Sie?", "Lassen Sie sich leicht ablenken?", "Haben Sie eine feste Routine?"],
         "ru": ["Вам трудно сопротивляться искушениям?", "Можете ли вы придерживаться ежедневных упражнений?", "Относительно составленных планов, вы?", "Легко ли вы отвлекаетесь?", "У вас есть фиксированный режим?"],
         "fr": ["Est-ce difficile pour vous de résister aux tentations ?", "Pouvez-vous tenir le coup avec l'exercice quotidien ?", "En ce qui concerne les plans faits, vous?", "Vous distrait facilement ?", "Avez-vous une routine fixe ?"]
     },
     "options": {
         "zh": ["有很强的自控力", "基本能控制，偶尔失控", "经常需要他人督促", "很难坚持，容易放弃"],
         "en": ["Strong self-control", "Basically can control, occasionally lose control", "Often need others to urge", "Hard to persist, easy to give up"],
         "es": ["Fuerte autocontrol", "Básicamente puedo controlar, ocasionalmente perder el control", "A menudo necesito que otros me impulsen", "Difícil persistir, fácil abandonar"],
         "ja": ["強い自己管理能力", "基本的にコントロール可能、時々制御不能", "よく他人に促される必要がある", "続けるのが難しく、簡単に諦める"],
         "de": ["Starke Selbstkontrolle", "Grundsätzlich kontrollieren, gelegentlich Kontrolle verlieren", "Oft brauchen anderen zu drängen", "Schwer durchzuhalten, leicht aufzugeben"],
         "ru": ["Сильная самоконтроль", "В основном могу контролировать, иногда теряю контроль", "Часто нужно чтобы другие подгоняли", "Трудно坚持， легко сдаться"],
         "fr": ["Fort autocontrôle", "Fondamentalement peux contrôler, occasionnellement perdre le contrôle", "Souvent besoin que d'autres m'encouragent", "Difficile de persévérer, facile d'abandonner"]
     }},
    # EMPATHY (5)
    {"trait": "empathy", "trait_cn": "共情能力",
     "texts": {
         "zh": ["别人难过时，你的反应是？", "你能理解他人的感受吗？", "面对他人的困境，你？", "你容易与人产生共鸣吗？", "看到不公平的事，你？"],
         "en": ["When others are sad, how do you react?", "Can you understand others' feelings?", "Facing others' difficulties, you?", "Do you easily resonate with others?", "Seeing unfair things, you?"],
         "es": ["Cuando otros están tristes, ¿cómo reaccionas?", "¿Puedes entender los sentimientos de otros?", "Cuando enfrentas las dificultades de otros, ¿tú?", "¿Te resuenas fácilmente con otros?", "Viendo cosas injustas, ¿tú?"],
         "ja": ["他の人が悲しんでいるとき、あなたはどのように反応しますか？", "あなたは他人の感情を理解できますか？", "他人の困難に向き合ったとき、あなたは？", "あなたは其他人と簡単に共鳴しますか？", "不公平な目撃したとき、あなたは？"],
         "de": ["Wenn andere traurig sind, wie reagieren Sie?", "Können Sie die Gefühle anderer verstehen?", "Wenn Sie den Schwierigkeiten anderer gegenüberstehen, tun Sie?", "Resonieren Sie leicht mit anderen?", "Ungerechte Dinge sehend, tun Sie?"],
         "ru": ["Когда другие грустят, как вы реагируете?", "Можете ли вы понять чувства других?", "Когда сталкиваетесь с трудностями других, вы?", "Легко ли вы сопереживаете другим?", "Видя несправедливость, вы?"],
         "fr": ["Quand les autres sont tristes, comment réagissez-vous ?", "Pouvez-vous comprendre les sentiments des autres ?", "Lorsque vous faites face aux difficultés des autres, vous?", "Vous ressentez facilement avec les autres ?", "Voyant des choses injustes, vous?"]
     },
     "options": {
         "zh": ["感同身受，全力帮助", "理解但不知如何帮助", "有些感同身受但不多表露", "难以理解，保持距离"],
         "en": ["Deeply feel, help with all my strength", "Understand but don't know how to help", "Somewhat empathize but don't show much", "Hard to understand, keep distance"],
         "es": ["Sentir profundamente, ayudar con toda mi fuerza", "Entender pero no sé cómo ayudar", "Algo empatizar pero no mostrar mucho", "Difícil entender, mantener distancia"],
         "ja": ["深く感じ取り、全力で助ける", "理解するがどう助ければいいか分からない", "多少共感するが多弁しない", "理解难以，距離を保つ"],
         "de": ["Tief fühlen, mit aller Kraft helfen", "Verstehen aber nicht wissen wie helfen", "Ein wenig empatieren aber nicht viel zeigen", "Schwer verstehen, Distanz halten"],
         "ru": ["Глубоко чувствовать, помогать всей силой", "Понимать но не знать как помочь", "Немного сопереживать но не показывать", "Трудно понять, держать дистанцию"],
         "fr": ["Profondément ressentir, aider de toute mon énergie", "Comprendre mais ne pas savoir comment aider", "Un peu empathiser mais pas montrer beaucoup", "Difficile de comprendre, garder la distance"]
     }},
    # AMBITION (5)
    {"trait": "ambition", "trait_cn": "野心",
     "texts": {
         "zh": ["你对成功的定义是？", "你愿意为了目标牺牲什么？", "面对失败，你的态度是？", "你更想要安稳还是成就？", "你对自己的期望是？"],
         "en": ["What is your definition of success?", "What are you willing to sacrifice for goals?", "Facing failure, your attitude is?", "Do you prefer stability or achievement?", "What are your expectations of yourself?"],
         "es": ["¿Cuál es tu definición de éxito?", "¿Qué estás dispuesto a sacrificar por metas?", "Frente al fracaso, ¿tu actitud es?", "¿Prefieres estabilidad o logros?", "¿Cuáles son tus expectativas de ti mismo?"],
         "ja": ["あなたの成功の定義は何ですか？", "目標のために何を犠牲にする気がありますか？", "失敗に直面したとき、あなたの態度は？", "あなたは安穏を望むか、成취を望むか？", "あなた自身の期待は何ですか？"],
         "de": ["Was ist Ihre Definition von Erfolg?", "Was sind Sie bereit für Ziele zu opfern?", "Beim Scheitern, was ist Ihre Einstellung?", "Bevorzugen Sie Stabilität oder Errungenschaften?", "Was sind Ihre Erwartungen an sich selbst?"],
         "ru": ["Что такое ваше определение успеха?", "Что вы готовы пожертвовать ради целей?", "Столкнувшись с неудачей, ваше отношение?", "Вы предпочитаете стабильность или достижения?", "Какие ваши ожидания от себя?"],
         "fr": ["Quelle est votre définition du succès ?", "Qu'est-ce que vous êtes prêt à sacrifier pour les objectifs ?", "Face à l'échec, quelle est votre attitude ?", "Préférez-vous la stabilité ou les réalisations ?", "Quelles sont vos attentes envers vous-même ?"]
     },
     "options": {
         "zh": ["功成名就，改变世界", "有所成就，但不强求", "安稳生活，知足常乐", "随遇而安，不追求成功"],
         "en": ["Achieve fame and success, change the world", "Achieve something, but not insist", "Stable life, content with what I have", "Go with the flow, don't pursue success"],
         "es": ["Lograr fama y éxito, cambiar el mundo", "Lograr algo, pero no insistir", "Vida estable, contento con lo que tengo", "Ir sobre la marcha, no perseguir el éxito"],
         "ja": ["成功を収め、世界を変える", "何か成し遂げるが、無理しない", "安穏な生活、知足楽観", "流れに任せる、成功を追求しない"],
         "de": ["Ruhm und Erfolg erreichen, die Welt verändern", "Etwas erreichen, aber nicht darauf bestehen", "Stabiles Leben, zufrieden mit dem was ich habe", "Mit dem Strom gehen, Erfolg nicht verfolgen"],
         "ru": ["Достичь славы и успеха, изменить мир", "Достичь чего-то, но не настаивать", "Стабильная жизнь, доволен тем что имею", "Идти по течению, не преследовать успех"],
         "fr": ["Atteindre la gloire et le succès, changer le monde", "Atteindre quelque chose, mais pas insister", "Vie stable, content de ce que j'ai", "Suivre le courant, ne pas poursuivre le succès"]
     }},
    # RESILIENCE (5)
    {"trait": "resilience", "trait_cn": "韧性",
     "texts": {
         "zh": ["遇到重大挫折后，你能恢复吗？", "面对连续失败，你会？", "困难时期，你的态度是？", "你容易从打击中恢复吗？", "对于逆境，你通常？"],
         "en": ["After a major setback, can you recover?", "Facing continuous failure, you?", "During difficult times, your attitude is?", "Do you recover easily from blows?", "Regarding adversity, you usually?"],
         "es": ["Después de un revés importante, ¿puedes recuperarte?", "Frente al fracaso continuo, ¿tú?", "Durante tiempos difíciles, ¿tu actitud es?", "¿Te recuperas fácilmente de los golpes?", "Respecto a la adversidad, ¿tú usualmente?"],
         "ja": ["大きな挫折の後、回復できますか？", "継続的な失敗に直面したとき、あなたは？", "困難な時期、あなたの態度は？", "あなたは打撃から回復しやすいですか？", "逆境について、あなたは通常？"],
         "de": ["Nach einem großen Rückschlag, können Sie sich erholen?", "Beim kontinuierlichen Scheitern, tun Sie?", "In schwierigen Zeiten, was ist Ihre Einstellung?", "Erholen Sie sich leicht von Schlägen?", "Bezüglich Widrigkeiten, tun Sie normalerweise?"],
         "ru": ["После серьезного поражения, можете ли вы восстановиться?", "Перед непрерывным провалом, вы?", "В трудные времена, ваше отношение?", "Вы легко восстанавливаетесь после ударов?", "Относительно невзгод, вы обычно?"],
         "fr": ["Après un revers majeur, pouvez-vous récupérer ?", "Face à l'échec continu, vous?", "Pendant les temps difficiles, quelle est votre attitude ?", "Vous remettez-vous facilement des coups ?", "Concernant l'adversité, vous faites quoi habituellement ?"]
     },
     "options": {
         "zh": ["很快恢复，愈挫愈勇", "需要时间但能恢复", "恢复较慢，偶尔消沉", "难以恢复，一蹶不振"],
         "en": ["Recover quickly, stronger after setbacks", "Need time but can recover", "Recover slowly, occasionally depressed", "Hard to recover, crushed"],
         "es": ["Recuperarme rápido, más fuerte después de contratiempos", "Necesito tiempo pero puedo recuperarme", "Recuperarme lento, ocasionalmente deprimido", "Difícil recuperarme, derrotado"],
         "ja": ["すぐに回復し、挫折後に強くなる", "時間がかかるが回復できる", "ゆっくり回復し、 occasionally 憂うつ", "回復难以，打ちのめされる"],
         "de": ["Schnell erholen, stärker nach Rückschlägen", "Brauche Zeit aber kann erholen", "Langsam erholen, gelegentlich depressiv", "Schwer erholen, niedergeschlagen"],
         "ru": ["Быстро восстановиться, сильнее после поражений", "Нужно время но могу восстановиться", "Медленно восстановиться, иногда подавлен", "Трудно восстановиться, раздавлен"],
         "fr": ["Récupérer vite, plus fort après les revers", "Besoin de temps mais peux récupérer", "Récupérer lentement, occasionnellement dépressif", "Difficile de récupérer, écrasé"]
     }}
]

# Build questions array
questions = []
for template in question_templates:
    for i in range(5):
        q = {
            "id": len(questions) + 1,
            "trait": template["trait"],
            "trait_cn": template["trait_cn"],
            "text": template["texts"]["zh"][i],
            "translations": {}
        }
        # Add translations for each language
        for lang in ["zh", "en", "es", "ja", "de", "ru", "fr"]:
            q["translations"][lang] = template["options"][lang] if lang in template["options"] else template["texts"][lang][i]
        questions.append(q)

print(f"Generated {len(questions)} questions")

# Write to file
import json
with open("E:/aiprojects/tinyapp/prophets/src/data/questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Written to questions.json")

# Verify
for i, q in enumerate(questions[:3], 1):
    print(f"Q{i}: {q['text'][:30]}... -> {q['translations']['en'][0][:30]}...")
