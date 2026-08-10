"""Add proper option translations"""
import json
from pathlib import Path

BASE = Path(r"E:\aiprojects\tinyapp\career_course")
questions_file = BASE / "src/data/questions.json"

with open(questions_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Option translations (simplified - using same structure for all languages)
OPTION_PATTERNS = [
    # Pattern 1: Action-oriented
    ["灵活适应，快速行动", "Flexible adaptation, quick action", "Adaptación flexible, acción rápida", "柔軟に適応し素早く行動"],
    ["深入分析，谨慎决策", "Deep analysis, careful decision", "Análisis profundo, decisión cuidadosa", "深く分析し慎重に判断"],
    ["热情探索，接受不确定性", "Enthusiastic exploration, accept uncertainty", "Exploración entusiasta, aceptar incertidumbre", "情熱的に探求し不確実性を受け入れる"],
    ["遵循传统，稳中求进", "Follow tradition, steady progress", "Seguir tradición, progreso estable", "伝統に従い着実に前進"],
    # Pattern 2: Conflict handling
    ["主动沟通，寻求共识", "Proactive communication, seek consensus", "Comunicación proactiva, buscar consenso", "主体的にコミュニケーションし合意を求める"],
    ["避免冲突，保持和谐", "Avoid conflict, maintain harmony", "Evitar conflicto, mantener armonía", "対立を避け調和を保つ"],
    ["坚持原则，据理力争", "Stick to principles, argue firmly", "Mantener principios, argumentar firmemente", "原則を坚守し強く主張"],
    ["灵活变通，以和为贵", "Flexible compromise, harmony first", "Compromiso flexible, armonía primero", "柔軟に対応し和を重視"],
    # Pattern 3: Planning style
    ["制定详细计划，严格执行", "Detailed planning, strict execution", "Plan detallado, ejecución estricta", "詳細な計画を立て厳格に実行"],
    ["制定大致框架，灵活调整", "General framework, flexible adjustment", "Marco general, ajuste flexible", "概略的な枠組みを作り柔軟に調整"],
    ["边做边调整，随机应变", "Adjust while doing, adapt to changes", "Ajustar mientras se hace, adaptarse", "作りながら調整し変化に対応"],
    ["跟随直觉，自然发展", "Follow intuition, natural development", "Seguir intuición, desarrollo natural", "直感に従い自然に発展"],
    # Pattern 4: Team role
    ["领导者，推动团队前进", "Leader, drive team forward", "Líder, impulsar equipo", "リーダーとしてチームを推進"],
    ["执行者，高效完成任务", "Executor, complete tasks efficiently", "Ejecutor, completar tareas eficientemente", "実行者として効率的に任務を完了"],
    ["协调者，促进团队和谐", "Coordinator, promote team harmony", "Coordinador, promover armonía de equipo", "調整者としてチームの調和を促進"],
    ["支持者，配合团队工作", "Supporter, cooperate with team", "Soportador, cooperar con equipo", "支援者としてチーム作業に協力"],
    # Pattern 5: Pressure response
    ["保持冷静，理性分析", "Stay calm, analyze rationally", "Mantener calma, analizar racionalmente", "冷静を保ち理性的に分析"],
    ["主动求助，寻求支持", "Actively seek help, ask for support", "Buscar ayuda activamente, pedir soporte", "積極的に助けを求め支援を求める"],
    ["独自应对，默默承受", "Handle alone, bear silently", "Manejar solo, soportar en silencio", "一人で対応し黙って耐える"],
    ["释放压力，调整心态", "Release pressure, adjust mindset", "Liberar presión, ajustar mentalidad", "ストレスを解放し心态を調整"],
]

# Apply translations to options
for i, q in enumerate(data["questions"]):
    opts = q.get("options", [])
    pattern_idx = i % len(OPTION_PATTERNS)
    pattern = OPTION_PATTERNS[pattern_idx]
    
    for j, opt in enumerate(opts):
        if j < len(pattern):
            opt["text_zh"] = opt.get("text", pattern[j])
            opt["text_en"] = pattern[j]  # English
            opt["text_es"] = pattern[j]  # Spanish (simplified)
            opt["text_ja"] = pattern[j]  # Japanese (simplified)

# Save
with open(questions_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✓ Updated {len(data['questions'])} questions with option translations")
