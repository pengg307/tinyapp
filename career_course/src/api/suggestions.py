"""建议生成模块 - 完整多语言支持（7种语言）"""
from typing import Any, List, Dict

# 12维性格维度的多语言建议
SUGGESTIONS_ZH = {
    "openness": {"up": ["多尝试新事物，保持好奇心", "阅读不同领域的书籍", "旅行或接触新文化"],
                 "down": ["不要害怕改变", "尝试新的思维方式", "接受不确定性"]},
    "conscientiousness": {"up": ["制定详细计划", "培养时间管理习惯", "注重细节"],
                          "down": ["更加灵活", "学会放手", "接受不完美"]},
    "extraversion": {"up": ["参加社交活动", "主动与人交流", "加入兴趣小组"],
                     "down": ["享受独处时间", "培养内向优势", "深度思考"]},
    "agreeableness": {"up": ["学会说no", "建立边界", "坚持己见"],
                      "down": ["更善于合作", "倾听他人意见", "寻求共赢"]},
    "neuroticism": {"up": ["学习情绪管理", "练习冥想", "保持规律作息"],
                    "down": ["更自信", "减少焦虑", "积极面对挑战"]},
    "leadership": {"up": ["承担领导角色", "学习管理技能", "影响他人"],
                   "down": ["配合团队", "支持领导者", "执行任务"]},
    "risk_taking": {"up": ["勇于尝试", "接受挑战", "冒险精神"],
                    "down": ["谨慎决策", "评估风险", "稳扎稳打"]},
    "rationality": {"up": ["理性分析", "数据驱动", "逻辑思考"],
                    "down": ["跟随直觉", "情感决策", "灵活应变"]},
    "discipline": {"up": ["坚持惯例", "自我控制", "持之以恒"],
                   "down": ["放松自己", "灵活调整", "随性而为"]},
    "empathy": {"up": ["体谅他人", "情感支持", "换位思考"],
                "down": ["独立自主", "理性判断", "保持距离"]},
    "ambition": {"up": ["设定高远目标", "追求卓越", "不断进阶"],
                 "down": ["知足常乐", "享受当下", "平衡生活"]},
    "resilience": {"up": ["抗压能力强", "从失败中学习", "韧性十足"],
                   "down": ["更容易挫折", "需要支持", "学会求助"]}
}

SUGGESTIONS_EN = {
    "openness": {"up": ["Try new things and stay curious", "Read books from different fields", "Travel or experience new cultures"],
                 "down": ["Don't be afraid of change", "Try new ways of thinking", "Accept uncertainty"]},
    "conscientiousness": {"up": ["Make detailed plans", "Develop time management habits", "Pay attention to details"],
                          "down": ["Be more flexible", "Learn to let go", "Accept imperfection"]},
    "extraversion": {"up": ["Attend social activities", "Initiate conversations", "Join interest groups"],
                     "down": ["Enjoy solitude", "Develop introvert strengths", "Deep thinking"]},
    "agreeableness": {"up": ["Learn to say no", "Set boundaries", "Stand your ground"],
                      "down": ["Be more cooperative", "Listen to others", "Seek win-win"]},
    "neuroticism": {"up": ["Learn emotional management", "Practice meditation", "Maintain regular schedule"],
                    "down": ["Be more confident", "Reduce anxiety", "Face challenges positively"]},
    "leadership": {"up": ["Take leadership roles", "Learn management skills", "Influence others"],
                   "down": ["Support the team", "Assist leaders", "Execute tasks"]},
    "risk_taking": {"up": ["Be courageous", "Accept challenges", "Take risks"],
                    "down": ["Make cautious decisions", "Evaluate risks", "Steady progress"]},
    "rationality": {"up": ["Think rationally", "Data-driven", "Logical thinking"],
                    "down": ["Follow intuition", "Emotional decisions", "Adapt flexibly"]},
    "discipline": {"up": ["Maintain routines", "Self-control", "Perseverance"],
                   "down": ["Relax yourself", "Flexible adjustment", "Be spontaneous"]},
    "empathy": {"up": ["Understand others", "Emotional support", "Put yourself in others' shoes"],
                "down": ["Be independent", "Rational judgment", "Keep distance"]},
    "ambition": {"up": ["Set high goals", "Pursue excellence", "Keep advancing"],
                 "down": ["Content with less", "Enjoy the moment", "Balance life"]},
    "resilience": {"up": ["Strong stress resistance", "Learn from failure", "Resilient"],
                   "down": ["More vulnerable", "Need support", "Learn to ask for help"]}
}

SUGGESTIONS_ES = {
    "openness": {"up": ["Intenta cosas nuevas y mantén la curiosidad", "Lee libros de diferentes campos", "Viaja o experimenta nuevas culturas"],
                 "down": ["No tengas miedo al cambio", "Prueba nuevas formas de pensar", "Acepta la incertidumbre"]},
    "conscientiousness": {"up": ["Haz planes detallados", "Desarrolla hábitos de gestión del tiempo", "Presta atención a los detalles"],
                          "down": ["Sé más flexible", "Aprende a soltar", "Acepta la imperfección"]},
    "extraversion": {"up": ["Asiste a actividades sociales", "Inicia conversaciones", "Únete a grupos de interés"],
                     "down": ["Disfruta la soledad", "Desarrolla fortalezas introvertidas", "Pensamiento profundo"]},
    "agreeableness": {"up": ["Aprende a decir no", "Establece límites", "Mantén tu postura"],
                      "down": ["Sé más cooperativo", "Escucha a los demás", "Busca ganar-ganar"]},
    "neuroticism": {"up": ["Aprende gestión emocional", "Practica meditación", "Mantén horario regular"],
                    "down": ["Sé más confiado", "Reduce ansiedad", "Enfrenta desafíos positivamente"]},
    "leadership": {"up": ["Toma roles de liderazgo", "Aprende habilidades de gestión", "Influye en otros"],
                   "down": ["Apoya al equipo", "Asiste a líderes", "Ejecuta tareas"]},
    "risk_taking": {"up": ["Sé valiente", "Acepta desafíos", "Toma riesgos"],
                    "down": ["Toma decisiones cautelosas", "Evalúa riesgos", "Progreso constante"]},
    "rationality": {"up": ["Piensa racionalmente", "Basado en datos", "Pensamiento lógico"],
                    "down": ["Sigue la intuición", "Decisiones emocionales", "Adaptación flexible"]},
    "discipline": {"up": ["Mantén rutinas", "Autocontrol", "Perseverancia"],
                   "down": ["Relájate", "Ajuste flexible", "Sé espontáneo"]},
    "empathy": {"up": ["Entiende a otros", "Apoyo emocional", "Ponte en lugar de otros"],
                "down": ["Sé independiente", "Juicio racional", "Mantén distancia"]},
    "ambition": {"up": ["Establece metas altas", "Busca la excelencia", "Sigue avanzando"],
                 "down": ["Contento con menos", "Disfruta el momento", "Equilibra la vida"]},
    "resilience": {"up": ["Fuerte resistencia al estrés", "Aprende del fracaso", "Resiliente"],
                   "down": ["Más vulnerable", "Necesita apoyo", "Aprende a pedir ayuda"]}
}

SUGGESTIONS_JA = {
    "openness": {"up": ["新しいことに挑戦し好奇心を保つ", "異なる分野の本を読む", "旅行や新しい文化を体験する"],
                 "down": ["変化を恐れない", "新しい考え方に挑戦する", "不確実性を受け入れる"]},
    "conscientiousness": {"up": ["詳細な計画を立てる", "タイムマネジメントの習慣を養う", "細部に注意する"],
                          "down": ["より柔軟になる", "手放すことを学ぶ", "不完全さを受け入れる"]},
    "extraversion": {"up": ["社交活動に参加する", "会話を始める", "興味グループに参加する"],
                     "down": ["静かな時間を楽しむ", "内向的な強みをdevelopする", "深い思考"]},
    "agreeableness": {"up": ["ノーと言うことを学ぶ", "境界を設定する", "自分の立場を守る"],
                      "down": ["より協力的になる", "他人の意見に耳を傾ける", "ウィンウィンを求める"]},
    "neuroticism": {"up": ["感情管理を学ぶ", "瞑想を実践する", "規則正しい生活を維持する"],
                    "down": ["もっと自信を持つ", "不安を減らす", "ポジティブに挑戦する"]},
    "leadership": {"up": ["リーダーシップ役を取る", "管理スキルを学ぶ", "他人に影響を与える"],
                   "down": ["チームを支援する", "リーダーを支援する", "タスクを実行する"]},
    "risk_taking": {"up": ["勇気を持つ", "挑戦を受け入れる", "リスクを取る"],
                    "down": ["慎重な意思決定", "リスクを評価する", "着実な進歩"]},
    "rationality": {"up": ["合理的に考える", "データ主導", "論理的思考"],
                    "down": ["直感を従う", "感情的な意思決定", "柔軟に対応する"]},
    "discipline": {"up": ["ルーティンを維持する", "自己管理", "粘り強さ"],
                   "down": ["リラックスする", "柔軟に調整する", " spontaneouslyに行動する"]},
    "empathy": {"up": ["他人を理解する", "感情的サポート", "他人の立場に立つ"],
                "down": ["自立する", "合理的判断", "距離を保つ"]},
    "ambition": {"up": ["高い目標を設定する", "卓越性を追求する", "前進し続ける"],
                 "down": ["少ないもので満足する", "瞬間を楽しむ", "生活をバランスする"]},
    "resilience": {"up": ["強いストレス耐性", "失敗から学ぶ", "回復力がある"],
                   "down": ["より脆弱", "サポートが必要", "助けを求めることを学ぶ"]}
}

SUGGESTIONS_DE = {
    "openness": {"up": ["Probiere neue Dinge und bleib neugierig", "Lies Bücher aus verschiedenen Bereichen", "Reise oder erlebe neue Kulturen"],
                 "down": ["Habe keine Angst vor Veränderungen", "Probiere neue Denkweisen aus", "Akzeptiere Unsicherheit"]},
    "conscientiousness": {"up": ["Mache detaillierte Pläne", "Entwickle Zeitmanagement-Gewohnheiten", "Achte auf Details"],
                          "down": ["Sei flexibler", "Lerne loszulassen", "Akzeptiere Unvollkommenheit"]},
    "extraversion": {"up": ["Nimm an sozialen Aktivitäten teil", "Starte Gespräche", "Tritt Interessen Gruppen bei"],
                     "down": ["Genieße die Einsamkeit", "Entwickle introvertierte Stärken", "Tiefes Denken"]},
    "agreeableness": {"up": ["Lerne nein zu sagen", "Setze Grenzen", "Behalte deinen Standpunkt"],
                      "down": ["Sei kooperativer", "Höre anderen zu", "Suche Win-Win"]},
    "neuroticism": {"up": ["Lerne Emotionsmanagement", "Praktiziere Meditation", "Halte regelmäßigen Zeitplan"],
                    "down": ["Sei selbstbewusster", "Reduziere Angst", "Stelle dich positiv Herausforderungen"]},
    "leadership": {"up": ["Übernehme Führungsrollen", "Lerne Managementfähigkeiten", "Influenziere andere"],
                   "down": ["Unterstütze das Team", "Hilf Führungskräften", "Führe Aufgaben aus"]},
    "risk_taking": {"up": ["Sei mutig", "Akzeptiere Herausforderungen", "Gehe Risiken ein"],
                    "down": ["Triff vorsichtige Entscheidungen", "Bewerte Risiken", "Stetige Fortschritte"]},
    "rationality": {"up": ["Denke rational", "Datengetrieben", "Logisches Denken"],
                    "down": ["Folge der Intuition", "Emotionale Entscheidungen", "Flexibel anpassen"]},
    "discipline": {"up": ["Behalte Routinen bei", "Selbstkontrolle", "Ausdauer"],
                   "down": ["Entspanne dich", "Flexible Anpassung", "Sei spontan"]},
    "empathy": {"up": ["Verstehe andere", "Emotionale Unterstützung", "Setz dich in die Lage anderer"],
                "down": ["Sei unabhängig", "Rationales Urteilen", "Halte Distanz"]},
    "ambition": {"up": ["Setze hohe Ziele", "Strebe nach Exzellenz", "Bleib am Vorantreiben"],
                 "down": ["Zufrieden mit weniger", "Genieß den Moment", "Balance im Leben"]},
    "resilience": {"up": ["Starke Stressresistenz", "Lerne aus dem Versagen", "Widerstandsfähig"],
                   "down": ["Anfälliger", "Brauche Unterstützung", "Lerne um Hilfe zu bitten"]}
}

SUGGESTIONS_RU = {
    "openness": {"up": ["Попробуй новое и сохрани любопытство", "Читай книги из разных областей", "Путешествуй или испытывай новые культуры"],
                 "down": ["Не бойся перемен", "Попробуй новые способы мышления", "Прими неопределенность"]},
    "conscientiousness": {"up": ["Составляй подробные планы", "Развивай привычки управления временем", "Обращай внимание на детали"],
                          "down": ["Будь более гибким", "Научись отпускать", "Прими несовершенство"]},
    "extraversion": {"up": ["Посещай социальные мероприятия", "Начинай разговоры", "Присоединяйся к группам по интересам"],
                     "down": ["Наслаждайся одиночеством", "Развивай сильные стороны интроверта", "Глубокое мышление"]},
    "agreeableness": {"up": ["Научись говорить нет", "Устанавливай границы", "Стой на своем"],
                      "down": ["Будь более кооперативным", "Слушай других", "Ищи взаимную выгоду"]},
    "neuroticism": {"up": ["Научись управлять эмоциями", "Практикуй медитацию", "Соблюдай регулярный распорядок"],
                    "down": ["Будь увереннее", "Снизь тревожность", "Позитивно面对挑战"]},
    "leadership": {"up": ["Бери на себя лидерские роли", "Изучай управленческие навыки", "Влияй на других"],
                   "down": ["Поддерживай команду", "Помогай лидерам", "Выполняй задачи"]},
    "risk_taking": {"up": ["Будь смелым", "Принимай вызовы", "Иди на риск"],
                    "down": ["Принимай осторожные решения", "Оценивай риски", "Постепенный прогресс"]},
    "rationality": {"up": ["Мысли рационально", "Основано на данных", "Логическое мышление"],
                    "down": ["Следуй интуиции", "Эмоциональные решения", "Гибкая адаптация"]},
    "discipline": {"up": ["Соблюдай режимы", "Самоконтроль", "Настойчивость"],
                   "down": ["Расслабься", "Гибкая корректировка", "Будь спонтанным"]},
    "empathy": {"up": ["Понимай других", "Эмоциональная поддержка", "Поставь себя на место других"],
                "down": ["Будь независимым", "Рациональное суждение", "Сохрани дистанцию"]},
    "ambition": {"up": ["Ставь высокие цели", "Стремись к совершенству", "Продолжай продвигаться"],
                 "down": ["Будь доволен меньшим", "Наслаждайся моментом", "Баланс в жизни"]},
    "resilience": {"up": ["Сильная стрессоустойчивость", "Учись на ошибках", "Стрессоустойчивый"],
                   "down": ["Более уязвимый", "Нуждается в поддержке", "Научись просить помощи"]}
}

SUGGESTIONS_FR = {
    "openness": {"up": ["Essayez de nouvelles choses et restez curieux", "Lisez des livres de différents domaines", "Voyagez ou découvrez de nouvelles cultures"],
                 "down": ["N'ayez pas peur du changement", "Essayez de nouvelles façons de penser", "Acceptez l'incertitude"]},
    "conscientiousness": {"up": ["Faites des plans détaillés", "Développez des habitudes de gestion du temps", "Faites attention aux détails"],
                          "down": ["Soyez plus flexible", "Apprenez à lâcher prise", "Acceptez l'imperfection"]},
    "extraversion": {"up": ["Participez à des activités sociales", "Amorcez des conversations", "Rejoignez des groupes d'intérêt"],
                     "down": ["Profitez du temps seul", "Développez vos forces introverties", "Pensée profonde"]},
    "agreeableness": {"up": ["Apprenez à dire non", "Établissez des limites", "Tenez-vous en à vos convictions"],
                      "down": ["Soyez plus coopératif", "Écoutez les autres", "Cherchez le gagnant-gagnant"]},
    "neuroticism": {"up": ["Apprenez la gestion émotionnelle", "Pratiquez la méditation", "Maintenez un horaire régulier"],
                    "down": ["Soyez plus confiant", "Réduisez l'anxiété", "Affrontez positivement les défis"]},
    "leadership": {"up": ["Prenez des rôles de leadership", "Apprenez les compétences de gestion", "Influencez les autres"],
                   "down": ["Soutenez l'équipe", "Assistez les leaders", "Exécutez les tâches"]},
    "risk_taking": {"up": ["Soyez courageux", "Acceptez les défis", "Prenez des risques"],
                    "down": ["Prenez des décisions prudents", "Évaluez les risques", "Progrès constant"]},
    "rationality": {"up": ["Pensez de manière rationnelle", "Axé sur les données", "Pensée logique"],
                    "down": ["Suivez l'intuition", "Décisions émotionnelles", "Adaptation flexible"]},
    "discipline": {"up": ["Maintenez vos routines", "Auto-contrôle", "Persévérance"],
                   "down": ["Détendez-vous", "Ajustement flexible", "Soyez spontané"]},
    "empathy": {"up": ["Comprenez les autres", "Support émotionnel", "Mettez-vous à la place des autres"],
                "down": ["Soyez indépendant", "Jugement rationnel", "Gardez vos distances"]},
    "ambition": {"up": ["Fixez des objectifs élevés", "Poursuivez l'excellence", "Continuez à avancer"],
                 "down": ["Soyez satisfait de moins", "Profitez du moment", "Équilibre de vie"]},
    "resilience": {"up": [" Forte résistance au stress", "Apprenez de l'échec", "Résilient"],
                   "down": ["Plus vulnérable", "Besoin de soutien", "Apprenez à demander de l'aide"]}
}


SUGGESTIONS_KO = {
    "openness": {"up": ["새로운 것 시도하고 호기심 유지", "다른 분야의 책 읽기", "여행이나 새로운 문화 체험"],
                 "down": ["변화를 두려워하지 마세요", "새로운 사고방식 시도", "불확실성 받아들이기"]},
    "conscientiousness": {"up": ["자세한 계획 세우기", "시간 관리 습관 기르기", "세부 사항에 주의"],
                          "down": ["더 유연하게", "放手를 배우기", "불완전함 받아들이기"]},
    "extraversion": {"up": ["사교 활동 참석", "대화 시작", "관심 그룹 가입"],
                     "down": ["혼자 있는 시간 즐기기", "내향적 강점 개발", "깊은 사고"]},
    "agreeableness": {"up": ["no라고 배우기", "경계 설정", "자신의 입장 고수"],
                      "down": ["더 협조적으로", "다른 사람 듣기", "win-win 추구"]},
    "neuroticism": {"up": ["감정 관리 배우기", "명상 실천", "정규 일정 유지"],
                    "down": ["더 자신 있게", "불안 감소", "도전에 긍정적으로面對"]},
    "leadership": {"up": ["리더십 역할 맡기", "관리 기술 배우기", "다른 사람 영향"],
                   "down": ["팀 지원", "리더 지원", "작업 실행"]},
    "risk_taking": {"up": ["용감하게", "도전受け", "위험 감수"],
                    "down": ["신중한 결정", "위험 평가", "꾸준한 진보"]},
    "rationality": {"up": ["합리적으로 생각", "데이터 기반", "논리적 사고"],
                    "down": ["직관 따르기", "감정적 결정", "유연하게 적응"]},
    "discipline": {"up": ["루틴 유지", "자기 통제", "인내"],
                   "down": [" relax yourself", "유연한 조정", "자발적으로 행동"]},
    "empathy": {"up": ["다른 사람 이해", "감정적 지원", "다른 사람 입장에서 생각"],
                "down": ["독립적", "합리적 판단", "거리 유지"]},
    "ambition": {"up": ["높은 목표 설정", "탁월함 추구", "계속 전진"],
                 "down": ["적은 것에 만족", "현재 순간 즐기기", "생활 균형"]},
    "resilience": {"up": ["강한 스트레스 저항", "실패から 배우기", "회복력 있음"],
                   "down": ["더 취약", "지원 필요", "돕기 요청 배우기"]}
}
SUGGESTIONS_MAP = {
    "zh": SUGGESTIONS_ZH,
    "en": SUGGESTIONS_EN,
    "es": SUGGESTIONS_ES,
    "ja": SUGGESTIONS_JA,
    "de": SUGGESTIONS_DE,
    "ru": SUGGESTIONS_RU,
    "fr": SUGGESTIONS_FR,
    "ko": SUGGESTIONS_KO
}

# 整体建议模板
OVERALL_TEMPLATES = {
    "zh": "你与{name}的差距主要集中在{trait}维度，建议：{suggestion}",
    "en": "Your main gap with {name} is in {trait}, suggested: {suggestion}",
    "es": "Tu principal diferencia con {name} está en {trait}, sugerido: {suggestion}",
    "ja": "{name}との主なギャップは{trait}です。提案：{suggestion}",
    "de": "Ihre Hauptlücke mit {name} ist in {trait}, empfohlen: {suggestion}",
    "ru": "Ваша основная разница с {name} в {trait}, рекомендуется: {suggestion}",
    "fr": "Votre principale différence avec {name} est dans {trait}, suggéré: {suggestion}",
    "ko": "{name}와의 주요 차이점은 {trait}입니다. 제안: {suggestion}"
}

def generate_suggestions(gaps: List[Dict[str, Any]], figure_type: str, language: str = "zh", figure_name: str = "") -> Dict[str, Any]:
    """生成多语言建议"""
    suggestions_map = SUGGESTIONS_MAP.get(language, SUGGESTIONS_EN)
    
    suggestions = []
    for gap in gaps[:3]:  # 只取前3个最大差距
        trait = gap.get("trait", "")
        direction = "up" if gap.get("gap", 0) > 0 else "down"
        trait_suggestions = suggestions_map.get(trait, {})
        trait_suggestions = trait_suggestions.get(direction, [])
        suggestion_text = "，".join(trait_suggestions[:2]) if trait_suggestions else ""
        
        suggestions.append({
            "trait": trait,
            "dimension": gap.get("dimension", trait),
            "direction": direction,
            "suggestion": suggestion_text
        })
    
    # 生成整体建议
    if suggestions:
        first = suggestions[0]
        overall = OVERALL_TEMPLATES.get(language, OVERALL_TEMPLATES["en"]).format(
            name=figure_name,
            trait=first["dimension"],  # 使用翻译后的维度名
            suggestion=first["suggestion"]
        )
    else:
        templates = {
            "zh": f"{figure_name}とよく似ています",
            "en": f"You match well with {figure_name}",
            "es": f"Coincides mucho con {figure_name}",
            "ja": f"{figure_name}とよく似ています",
            "de": f"Sie ähneln stark {figure_name}",
            "ru": f"Вы очень похожи на {figure_name}",
            "fr": f"Vous correspondez bien à {figure_name}"
        }
        overall = templates.get(language, templates["en"])
    
    return {
        "overall": overall,
        "suggestions": suggestions,
        "figure_type": figure_type
    }
