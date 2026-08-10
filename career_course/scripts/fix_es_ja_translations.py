"""Add proper Spanish and Japanese translations for all 60 questions"""
import json
from pathlib import Path

QUESTIONS_FILE = Path(r"E:\aiprojects\tinyapp\career_course\src\data\questions.json")
data = json.loads(QUESTIONS_FILE.read_text(encoding="utf-8"))

# Spanish translations for 60 questions
QUESTION_ES = [
    "¿Cómo tiende a actuar cuando se enfrenta a problemas complejos en un campo desconocido?",
    "Cuando se le presenta un nuevo proyecto, usted prefiere:",
    "Cuando ocurre un cambio inesperado, su primera reacción es:",
    "Ante una nueva idea, usted prefiere:",
    "Al comparar métodos tradicionales con nuevos, usted:",
    "Cuando tiene una tarea importante, usted:",
    "Ante una fecha límite ajustada, usted:",
    "Cuando encuentra un error pequeño, usted:",
    "Cuando los planes cambianrepentinamente, usted:",
    "Para su desarrollo personal, usted prioriza:",
    "Cuando conoce gente nueva, usted:",
    "En una discusión grupal, su papel es:",
    "Prefiere trabajar:",
    "En una fiesta social, usted:",
    "La opinión de otros sobre usted:",
    "Cuando no está de acuerdo con alguien, usted:",
    "Cuando hay un conflicto en el equipo, usted:",
    "Cuando alguien comete un error, usted:",
    "En una situación competitiva, usted:",
    "Cuando alguien le pide un favor que no quiere hacer:",
    "Cuando está bajo mucha presión, usted:",
    "Después de un fracaso, usted:",
    "Ante la incertidumbre del futuro, usted:",
    "Cuando recibe críticas, usted:",
    "En una crisis, su respuesta emocional es:",
    "Cuando debe liderar un equipo, usted:",
    "Ante una decisión importante, usted:",
    "Cuando influye en otros, usted:",
    "Ante una responsabilidad grande, usted:",
    "Cuando tiene poder de decisión, usted:",
    "Ante una oportunidad de riesgo, usted:",
    "Cuando hay incertidumbre, usted:",
    "Ante una decisión peligrosa, usted:",
    "Cuando acepta un desafío arriesgado, usted:",
    "Para tomar decisiones, usted:",
    "Cuando resuelve problemas lógicos, usted:",
    "Cuando equilibra emoción e razón, usted:",
    "Cuando faltan datos, usted:",
    "Ante un problema complejo, usted:",
    "Cuando necesita ser estricto consigo mismo, usted:",
    "Para mantener hábitos, usted:",
    "Ante una tentación, usted:",
    "Para mantener la consistencia, usted:",
    "Cuando persigue una meta a largo plazo, usted:",
    "Cuando entiende las emociones de otros, usted:",
    "Cuando alguien necesita apoyo emocional, usted:",
    "Para entender a otros, usted:",
    "Cuando la empatía es importante, usted:",
    "Para crear conexiones emocionales, usted:",
    "Su definición de éxito es:",
    "Cuando se establece una meta alta, usted:",
    "Para equilibrar ambición y realidad, usted:",
    "Cuando se enfrenta a una meta desafiante, usted:",
    "Cuando expresa su ambición, usted:",
    "Cuando supera un contratiempo, usted:",
    "En tiempos difíciles, usted:",
    "Para adaptarse al cambio, usted:",
    "Bajo presión, usted:",
    "Después de un fracaso, usted:"
]

# Japanese translations for 60 questions
QUESTION_JA = [
    "見知らぬ分野の複雑な問題に直面したとき、あなたはどのように傾向するか？",
    "新しいプロジェクトに参加するとき、あなたは？",
    "予期せぬ変化が起きたとき、あなたの反応は？",
    "新しいアイデアを試すとき、あなたは？",
    "伝統的な方法と新しい方法を比較するとき？",
    "重要な業務を処理するとき、あなたは？",
    "期限のある作業をするとき、あなたの態度は？",
    "小さなミスが発見されたとき？",
    "計画が突然変更されたとき？",
    "自己発展のために何を優先しますか？",
    "新しい人と出会ったとき、あなたは？",
    "グループ討論でのあなたの役割は？",
    "一人で働くこととチームで働くことのどちらが好き？",
    "社交的な集まりではあなたは？",
    "他人の評価について？",
    "意見が合わない相手に直面したとき？",
    "チーム内に対立が生じたとき？",
    "他人のミスを見たとき？",
    "競争状況でのあなたの態度？",
    "断りたい頼みをされたとき？",
    "ストレスの多い状況でのあなたの反応は？",
    "失敗を経験したとき？",
    "不確実な未来について？",
    "批判的なフィードバックを受けたとき？",
    "危機的状況での感情反応は？",
    "チームを率いることになったとき、あなたは？",
    "重要な決定をする場面では？",
    "他人に影響を与えるとき？",
    "重い責任を伴う決定を下すとき？",
    "影響力を発揮するとき？",
    "危険な状況でのあなたの選択は？",
    "安全のために報奨を選ぶとき？",
    "新しい機会を見つけたとき？",
    "不確実な決定を下さなければならないとき？",
    "挑戦を受け入れるとき？",
    "決定を下すとき、あなたは？",
    "論理的な問題解決时？",
    "感情と理性のバランスを取る时？",
    "データが足りない时？",
    "複雑な問題を分析するとき？",
    "自分自身に厳しくするとき、あなたは？",
    "習慣を維持するとき？",
    "誘惑に対処するとき？",
    "一貫性を保つとき？",
    "目標に向かって忍耐強さが必要なとき？",
    "他人の感情を理解するとき、あなたは？",
    "感情的なサポートが必要なとき？",
    "他人の立場を理解するとき？",
    "共感力が重要するとき？",
    "感情的なつながりを作るとき？",
    "成功に対するあなたの定義は？",
    "高い目標を設定するとき？",
    "野心と現実のバランスを取る时？",
    "挑戦的な目標を設定するとき？",
    "野心を表すとき？",
    "挫折を乗り越えるとき、あなたは？",
    "困難な時期を過ごすとき？",
    "変化に適応するとき？",
    "圧力に耐えるとき？",
    "失敗の後再び始めるとき？"
]

# Update questions
for i, q in enumerate(data.get("questions", [])):
    q_id = q.get("id", i + 1)
    if q_id <= len(QUESTION_ES):
        q["question_es"] = QUESTION_ES[q_id - 1]
    if q_id <= len(QUESTION_JA):
        q["question_ja"] = QUESTION_JA[q_id - 1]

# Write back
QUESTIONS_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Updated {len(data['questions'])} questions with Spanish and Japanese translations")
print(f"Sample ES: {QUESTION_ES[0][:50]}...")
print(f"Sample JA: {QUESTION_JA[0][:50]}...")
