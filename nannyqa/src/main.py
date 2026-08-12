"""家政面试题库 - 双角色流程 v3.2
流程：雇主生成短码(12小时有效) → 保姆扫码答题 → 雇主查看报告
增强：可读短码、直接链接查看报告
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import json
import os
import time
from datetime import datetime, timedelta
import threading
import secrets
import string

app = FastAPI(title="家政面试题库", description="保姆面试评估系统")

# 读取题目数据
questions_path = os.path.join(os.path.dirname(__file__), "data", "questions.json")
with open(questions_path, "r", encoding="utf-8") as f:
    QUESTIONS = json.load(f)

# ============================================================
# 会话存储
# ============================================================
sessions: Dict[str, dict] = {}
sessions_lock = threading.Lock()

def cleanup_expired_sessions():
    while True:
        time.sleep(60)
        now = time.time()
        with sessions_lock:
            expired = [k for k, v in sessions.items() if now > v.get("expires_at", 0)]
            for k in expired:
                del sessions[k]

threading.Thread(target=cleanup_expired_sessions, daemon=True).start()

# ============================================================
# 维度权重配置
# ============================================================
DIMENSION_WEIGHTS = {
    "experience_level": 0.12, "health": 0.08, "family_situation": 0.05,
    "motivation": 0.06, "learning_attitude": 0.05, "career_plan": 0.04,
    "reference_check": 0.05, "cooking_skill": 0.08, "hygiene_habits": 0.06,
    "baby_food": 0.05, "dietary_restrictions": 0.04, "leftover_handling": 0.03,
    "cooking_under_pressure": 0.04, "cooking_for_sick": 0.03, "taste_adjustment": 0.03,
    "daily_routine": 0.08, "sleep_training": 0.06, "teething_care": 0.04,
    "potty_training": 0.05, "screen_time": 0.04, "sibling_conflict": 0.05,
    "selective_eating": 0.04, "separation_anxiety": 0.05, "allergic_reaction": 0.06,
    "choking_emergency": 0.07, "tantrum_public": 0.04, "daily_cleaning": 0.06,
    "disinfection": 0.06, "laundry_separation": 0.05, "deep_cleaning_schedule": 0.04,
    "pest_control": 0.03, "dishwashing_routine": 0.03, "vacuum_cleaning_detail": 0.03,
    "fire_safety": 0.08, "gas_leak": 0.06, "electrical_safety": 0.05,
    "car_seat_usage": 0.06, "window_falls": 0.07, "poison_identification": 0.06,
    "hot_water_scald": 0.05, "emergency_contact_card": 0.04, "stranger_at_door": 0.06,
    "feedback_reception": 0.06, "boundary_setting": 0.05, "reporting_incidents": 0.07,
    "handling_accusations": 0.06, "scheduling_conflict": 0.05, "dealing_with_rude_family": 0.05,
    "giving_bad_news": 0.06, "privacy_protection": 0.08, "honesty_about_mistakes": 0.07,
    "handling_found_money": 0.06, "social_media_boundaries": 0.06, "conflict_of_interest": 0.05,
    "work_attitude": 0.06, "time_management": 0.05, "dress_code": 0.04,
    "time_management2": 0.04, "job_stability": 0.06, "salary_negotiation": 0.04,
    "continuing_education": 0.05, "elder_experience": 0.05, "medication_management": 0.05,
    "fall_response": 0.06, "feeding_assistance": 0.05, "end_of_life_communication": 0.04,
    "infant_colic": 0.05, "premature_baby_care": 0.05, "multi_child_chaos": 0.05,
    "nanny_dispute_with_parent": 0.05, "working_parent_commuting": 0.05,
    "nanny_overnight_call": 0.06, "pet_allergy_child": 0.04, "single_parent_stress": 0.04,
    "elder_abuse_suspected": 0.05, "food_poisoning_outbreak": 0.06,
    "nanny_wrongful_accusation": 0.05, "emergency_natural_disaster": 0.06,
    "misunderstanding_with_children": 0.04, "elder_memory_loss_paranoia": 0.05,
    "fever_handling": 0.05, "foreign_object_eye": 0.05,
    "burn_prevention_kitchen2": 0.05, "toilet_disinfection": 0.05,
    "nutritional_balance": 0.05, "handling_angry_employer": 0.05,
    "workplace_gossip": 0.05, "dementia_wandering": 0.05,
    "nanny_medical_emergency": 0.05, "child_abduction_attempt": 0.05,
}

CATEGORY_DESCRIPTIONS = {
    "basic": "基本信息", "cooking": "烹饪技能", "childcare": "育儿能力",
    "hygiene": "卫生习惯", "safety": "安全意识", "communication": "沟通能力",
    "ethics": "职业道德", "professionalism": "职业素养", "elder_care": "老人照护", "special": "特殊情况",
}

# ============================================================
# 辅助函数
# ============================================================

def generate_short_code(length=6):
    """生成易记的短码: ABC123格式"""
    chars = string.ascii_uppercase + string.digits
    # 避免易混淆字符: 0/O, 1/I/l
    safe_chars = [c for c in chars if c not in '0O1Il']
    return ''.join(secrets.choice(safe_chars) for _ in range(length))

def generate_report(answers: List[dict]) -> dict:
    """生成评估报告"""
    dimension_scores: Dict[str, List[int]] = {}
    dimension_questions: Dict[str, int] = {}
    
    for answer in answers:
        question = next((q for q in QUESTIONS if q["id"] == answer["question_id"]), None)
        if not question:
            continue
        
        dimension = question["dimension"]
        if dimension not in dimension_scores:
            dimension_scores[dimension] = []
            dimension_questions[dimension] = 0
        dimension_scores[dimension].append(answer["score"])
        dimension_questions[dimension] += 1
    
    # 计算各维度平均分
    dimension_averages = {}
    for dim, scores in dimension_scores.items():
        if scores:
            dimension_averages[dim] = sum(scores) / len(scores)
        else:
            dimension_averages[dim] = 0
    
    # 计算加权总分
    total_score = 0
    total_weight = 0
    for dim, avg_score in dimension_averages.items():
        weight = DIMENSION_WEIGHTS.get(dim, 0.05)
        total_score += avg_score * weight
        total_weight += weight
    
    # 归一化到100分制
    if total_weight > 0:
        final_score = (total_score / total_weight) * 20
    else:
        final_score = 0
    
    # NaN检查
    if not (final_score == final_score):
        final_score = 0
    final_score = min(100, max(0, final_score))
    
    # 生成评级
    if final_score >= 90:
        rating = "⭐⭐⭐⭐⭐ 优秀"
        suggestion = "强烈推荐录用，各方面表现突出，具备优秀的家政服务素质。"
    elif final_score >= 80:
        rating = "⭐⭐⭐⭐ 良好"
        suggestion = "推荐录用，具备良好的家政服务能力和职业素质。"
    elif final_score >= 70:
        rating = "⭐⭐⭐ 合格"
        suggestion = "可以考虑录用，某些方面需要进一步提升。"
    elif final_score >= 60:
        rating = "⭐⭐ 需改进"
        suggestion = "不建议直接录用，除非有特别优势或经过培训。"
    else:
        rating = "⭐ 不推荐"
        suggestion = "不适合从事家政工作，建议重新考虑。"
    
    # 强项和弱项
    sorted_dimensions = sorted(dimension_averages.items(), key=lambda x: x[1], reverse=True)
    strong_points = sorted_dimensions[:5]
    weak_points = sorted_dimensions[-5:]
    
    # 题目详情
    question_details = []
    for answer in answers:
        question = next((q for q in QUESTIONS if q["id"] == answer["question_id"]), None)
        if not question or not question.get("options"):
            continue
        selected_opt = next((o for o in question["options"] if o.get("score") == answer["score"]), None)
        best_opt = max(question["options"], key=lambda o: o.get("score", 0))
        question_details.append({
            "id": question["id"],
            "question": question["question_zh"],
            "category": CATEGORY_DESCRIPTIONS.get(question["category"], question["category"]),
            "difficulty": question.get("difficulty", "medium"),
            "selected_answer": selected_opt.get("text_zh", "") if selected_opt else "",
            "selected_feedback": selected_opt.get("feedback_zh", "") if selected_opt else "",
            "best_score": best_opt.get("score", 0),
            "is_best": answer["score"] >= best_opt.get("score", 0),
            "score": answer["score"],
        })
    
    return {
        "total_score": round(final_score, 1),
        "total_questions": len(QUESTIONS),
        "answered_count": len(answers),
        "rating": rating,
        "suggestion": suggestion,
        "dimension_details": [
            {
                "dimension": dim,
                "avg_score": round(avg, 1) if avg == avg else 0,
                "weight": round(DIMENSION_WEIGHTS.get(dim, 0.05) * 100, 1),
                "category": CATEGORY_DESCRIPTIONS.get(next((q["category"] for q in QUESTIONS if q["dimension"] == dim), ""), "其他"),
                "answered": dimension_questions.get(dim, 0)
            }
            for dim, avg in sorted_dimensions
        ],
        "strong_points": [
            {"dimension": dim, "score": round(score, 1) if score == score else 0}
            for dim, score in strong_points
        ],
        "weak_points": [
            {"dimension": dim, "score": round(score, 1) if score == score else 0}
            for dim, score in weak_points
        ],
        "question_details": question_details,
    }

# ============================================================
# Pydantic Models
# ============================================================
class Answer(BaseModel):
    question_id: int
    score: int

class CreateSessionRequest(BaseModel):
    master_name: str = ""
    company: str = ""
    contact_phone: str = ""
    contact_email: str = ""
    notes: str = ""

class SubmitAnswerRequest(BaseModel):
    answers: List[Answer]

# ============================================================
# API 端点
# ============================================================

@app.get("/api/questions")
async def get_questions(difficulty: str = None):
    if difficulty:
        return [q for q in QUESTIONS if q.get("difficulty") == difficulty]
    return QUESTIONS

@app.post("/api/session")
async def create_session(request: CreateSessionRequest):
    """创建测试会话，返回易记短码"""
    # 生成短码（确保唯一）
    while True:
        short_code = generate_short_code(6)
        if short_code not in sessions:
            break
    
    expires_at = time.time() + (12 * 3600)
    
    with sessions_lock:
        sessions[short_code] = {
            "short_code": short_code,
            "master_name": request.master_name,
            "company": request.company,
            "contact_phone": request.contact_phone,
            "contact_email": request.contact_email,
            "notes": request.notes,
            "created_at": datetime.now().isoformat(),
            "expires_at": expires_at,
            "answers": [],
            "status": "active",
        }
    
    base_url = f"http://{os.getenv('SERVER_HOST', 'localhost:8005')}"
    return {
        "short_code": short_code,
        "test_url": base_url + f"/test/{short_code}",
        "report_url": base_url + f"/report/{short_code}",
        "expires_at": datetime.fromtimestamp(expires_at).strftime("%Y-%m-%d %H:%M"),
        "expires_in_hours": 12,
        "master_info": {
            "name": request.master_name,
            "company": request.company,
            "contact": request.contact_phone or request.contact_email,
        }
    }

@app.get("/api/session/{short_code}")
async def get_session(short_code: str):
    """获取会话信息"""
    with sessions_lock:
        session = sessions.get(short_code)
    
    if not session:
        raise HTTPException(status_code=404, detail="会话不存在或已过期")
    
    if time.time() > session["expires_at"]:
        raise HTTPException(status_code=410, detail="会话已过期")
    
    return {
        "short_code": session["short_code"],
        "master_name": session.get("master_name", ""),
        "company": session.get("company", ""),
        "contact_phone": session.get("contact_phone", ""),
        "notes": session.get("notes", ""),
        "created_at": session["created_at"],
        "expires_at": datetime.fromtimestamp(session["expires_at"]).strftime("%Y-%m-%d %H:%M"),
        "status": session["status"],
        "answer_count": len(session.get("answers", [])),
        "is_complete": session["status"] == "completed",
    }

@app.get("/test/{short_code}")
async def candidate_test_page(short_code: str):
    """保姆答题页面"""
    with sessions_lock:
        session = sessions.get(short_code)
    
    if not session:
        return HTMLResponse("""
            <div style='text-align:center;padding:50px;font-family:sans-serif;'>
                <h2>❌ 会话不存在</h2>
                <p>该二维码已过期或无效，请联系雇主重新生成。</p>
            </div>
        """, status_code=404)
    
    if time.time() > session["expires_at"]:
        return HTMLResponse("""
            <div style='text-align:center;padding:50px;font-family:sans-serif;'>
                <h2>⏰ 二维码已过期</h2>
                <p>该二维码已超过12小时有效期，请联系雇主重新生成。</p>
            </div>
        """, status_code=410)
    
    if session["status"] == "completed":
        return HTMLResponse("""
            <div style='text-align:center;padding:50px;font-family:sans-serif;'>
                <h2>✅ 感谢参与！</h2>
                <p>您已完成所有题目，感谢您的配合！</p>
                <p style='color:#888;margin-top:20px;'>评估结果将由雇主查看。</p>
            </div>
        """)
    
    return await _render_candidate_page(short_code)

@app.post("/api/session/{short_code}/submit")
async def submit_answers(short_code: str, request: SubmitAnswerRequest):
    """提交答案"""
    with sessions_lock:
        session = sessions.get(short_code)
        
        if not session:
            raise HTTPException(status_code=404, detail="会话不存在")
        
        if time.time() > session["expires_at"]:
            raise HTTPException(status_code=410, detail="会话已过期")
        
        if session["status"] == "completed":
            raise HTTPException(status_code=409, detail="该测试已完成")
        
        existing_answers = session.get("answers", [])
        existing_ids = {a["question_id"] for a in existing_answers}
        
        for answer in request.answers:
            if answer.question_id not in existing_ids:
                existing_answers.append({
                    "question_id": answer.question_id,
                    "score": answer.score,
                    "submitted_at": datetime.now().isoformat(),
                })
        
        session["answers"] = existing_answers
        
        if len(existing_answers) >= len(QUESTIONS):
            session["status"] = "completed"
            session["completed_at"] = datetime.now().isoformat()
            session["report"] = generate_report(existing_answers)
    
    return {
        "status": "success",
        "answered_count": len(request.answers),
        "total_questions": len(QUESTIONS),
        "is_complete": len(request.answers) >= len(QUESTIONS),
    }

@app.get("/api/session/{short_code}/report")
async def get_report(short_code: str):
    """获取评估报告"""
    with sessions_lock:
        session = sessions.get(short_code)
    
    if not session:
        raise HTTPException(status_code=404, detail="会话不存在")
    
    if time.time() > session["expires_at"]:
        raise HTTPException(status_code=410, detail="会话已过期")
    
    if session["status"] != "completed":
        raise HTTPException(status_code=409, detail="测试尚未完成")
    
    return session.get("report", {})

@app.get("/report/{short_code}")
async def report_page(short_code: str):
    """直接查看报告页面（无需登录）"""
    with sessions_lock:
        session = sessions.get(short_code)
    
    if not session:
        return HTMLResponse("""
            <div style='text-align:center;padding:50px;font-family:sans-serif;'>
                <h2>❌ 报告不存在</h2>
                <p>该报告链接无效或已过期。</p>
            </div>
        """, status_code=404)
    
    if time.time() > session["expires_at"]:
        return HTMLResponse("""
            <div style='text-align:center;padding:50px;font-family:sans-serif;'>
                <h2>⏰ 报告已过期</h2>
                <p>该测试已过期，无法查看报告。</p>
            </div>
        """, status_code=410)
    
    if session["status"] != "completed":
        return HTMLResponse(f"""
            <div style='text-align:center;padding:50px;font-family:sans-serif;'>
                <h2>⏳ 测试进行中</h2>
                <p>候选人尚未完成测试，请稍后再查看报告。</p>
                <p style='color:#888;'>已答: {len(session.get('answers', []))} / {len(QUESTIONS)} 题</p>
            </div>
        """)
    
    report = session.get("report", {})
    return await _render_report_page(short_code, report, session)

@app.get("/api/sessions")
async def list_sessions(master_name: str = None, status: str = None, limit: int = 50):
    """列出所有会话"""
    with sessions_lock:
        result = []
        for code, session in sessions.items():
            if time.time() > session.get("expires_at", 0):
                continue
            if master_name and session.get("master_name") != master_name:
                continue
            if status and session.get("status") != status:
                continue
            result.append({
                "short_code": code,
                "master_name": session.get("master_name", ""),
                "company": session.get("company", ""),
                "status": session.get("status"),
                "created_at": session.get("created_at"),
                "expires_at": datetime.fromtimestamp(session.get("expires_at", 0)).strftime("%Y-%m-%d %H:%M"),
                "answer_count": len(session.get("answers", [])),
                "has_report": session.get("status") == "completed",
            })
        result.sort(key=lambda x: x["created_at"], reverse=True)
        return result[:limit]

@app.delete("/api/session/{short_code}")
async def delete_session(short_code: str):
    """删除会话"""
    with sessions_lock:
        if short_code in sessions:
            del sessions[short_code]
            return {"status": "deleted"}
    raise HTTPException(status_code=404, detail="会话不存在")

@app.get("/")
async def root():
    """返回主页面"""
    static_path = os.path.join(os.path.dirname(__file__), "..", "static")
    index_path = os.path.join(static_path, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return HTMLResponse(f.read())
    return HTMLResponse("<h1>家政面试题库系统</h1><p>请先部署前端页面</p>")

# ============================================================
# 页面渲染
# ============================================================

async def _render_candidate_page(short_code: str) -> HTMLResponse:
    html_content = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>家政面试评估</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 800px; margin: 0 auto; }
        header { text-align: center; padding: 20px; color: white; }
        header h1 { font-size: 1.8rem; margin-bottom: 5px; }
        header p { font-size: 0.9rem; opacity: 0.9; }

        .card {
            background: white;
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 15px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        }

        .category-badge {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 0.75rem;
            margin-bottom: 10px;
        }
        .difficulty-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 0.7rem;
            font-weight: bold;
            margin-left: 8px;
        }
        .difficulty-badge.easy { background: #4ade80; color: white; }
        .difficulty-badge.medium { background: #fbbf24; color: white; }
        .difficulty-badge.hard { background: #f87171; color: white; }

        .question-number { color: #667eea; font-weight: bold; font-size: 0.85rem; margin-bottom: 5px; }
        .question-text { font-size: 1.1rem; color: #333; margin-bottom: 18px; line-height: 1.6; }

        .options { display: flex; flex-direction: column; gap: 10px; }
        .option-btn {
            padding: 14px 18px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            background: white;
            cursor: pointer;
            transition: all 0.25s ease;
            text-align: left;
            font-size: 0.95rem;
            color: #333;
        }
        .option-btn:hover { border-color: #667eea; background: #f8f9ff; transform: translateX(4px); }
        .option-btn.selected { border-color: #667eea; background: linear-gradient(135deg, #667eea, #764ba2); color: white; }

        .nav-buttons { display: flex; justify-content: flex-start; margin-top: 25px; padding-top: 15px; border-top: 1px solid #eee; }
        .btn { padding: 12px 28px; border: none; border-radius: 25px; font-size: 0.95rem; cursor: pointer; transition: all 0.3s; }
        .btn-prev { background: #f0f0f0; color: #666; }
        .btn-prev:hover { background: #e0e0e0; }
        .btn-prev:disabled { opacity: 0.5; cursor: not-allowed; }

        .progress-bar { height: 6px; background: #e0e0e0; border-radius: 3px; margin-bottom: 20px; overflow: hidden; }
        .progress-fill { height: 100%; background: linear-gradient(90deg, #667eea, #764ba2); transition: width 0.3s ease; }
        .progress-text { text-align: center; color: #666; font-size: 0.85rem; margin-bottom: 8px; }

        .stats-summary { display: flex; justify-content: space-around; padding: 15px 0; border-bottom: 1px solid #eee; margin-bottom: 15px; }
        .stat-item { text-align: center; }
        .stat-item .value { font-size: 1.5rem; font-weight: bold; color: #667eea; }
        .stat-item .label { font-size: 0.8rem; color: #888; }

        .hidden { display: none; }
        
        .thank-you { text-align: center; padding: 40px 20px; }
        .thank-you h2 { color: #667eea; margin-bottom: 15px; }
        .thank-you p { color: #666; line-height: 1.8; }
        .thank-you .icon { font-size: 4rem; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🏠 家政面试评估</h1>
            <p>感谢您的参与，请认真回答以下问题</p>
        </header>

        <div id="quiz-screen">
            <div class="progress-text" id="progress-text">第 1 / 90 题</div>
            <div class="progress-bar"><div class="progress-fill" id="progress-fill" style="width: 1.1%"></div></div>
            <div class="stats-summary">
                <div class="stat-item"><div class="value" id="answered-count">0</div><div class="label">已答</div></div>
                <div class="stat-item"><div class="value" id="remaining-count">90</div><div class="label">剩余</div></div>
                <div class="stat-item"><div class="value" id="current-difficulty">-</div><div class="label">当前难度</div></div>
            </div>
            <div class="card" id="question-card"></div>
            <div class="nav-buttons">
                <button class="btn btn-prev" id="prev-btn" onclick="prevQuestion()">上一题</button>
            </div>
        </div>

        <div id="thankyou-screen" class="hidden">
            <div class="card">
                <div class="thank-you">
                    <div class="icon">🎉</div>
                    <h2>感谢您的参与！</h2>
                    <p>您已完成所有面试题目。</p>
                    <p style="color:#888;margin-top:15px;">雇主将收到您的评估报告。</p>
                    <p style="color:#aaa;font-size:0.85rem;margin-top:20px;">祝您求职顺利！</p>
                </div>
            </div>
        </div>
    </div>

    <script>
        const shortCode = window.location.pathname.split('/test/')[1];
        let allQuestions = [];
        let currentQuestion = 0;
        let answers = [];

        const CATEGORY_MAP = {
            'basic': '基本信息', 'cooking': '烹饪技能', 'childcare': '育儿能力',
            'hygiene': '卫生习惯', 'safety': '安全意识', 'communication': '沟通能力',
            'ethics': '职业道德', 'professionalism': '职业素养', 'elder_care': '老人照护', 'special': '特殊情况'
        };
        const DIFFICULTY_MAP = { 'easy': '基础', 'medium': '中等', 'hard': '进阶' };

        async function init() {
            try {
                const response = await fetch('/api/questions');
                allQuestions = await response.json();
                answers = new Array(allQuestions.length).fill(null);
                renderQuestion();
            } catch (error) {
                document.getElementById('quiz-screen').innerHTML = 
                    '<div class="card"><p style="text-align:center;color:red;">加载题目失败，请刷新重试</p></div>';
            }
        }

        function renderQuestion() {
            const q = allQuestions[currentQuestion];
            const card = document.getElementById('question-card');

            document.getElementById('progress-text').textContent = `第 ${currentQuestion + 1} / ${allQuestions.length} 题`;
            document.getElementById('progress-fill').style.width = `${((currentQuestion + 1) / allQuestions.length) * 100}%`;
            document.getElementById('answered-count').textContent = answers.filter(a => a !== null).length;
            document.getElementById('remaining-count').textContent = allQuestions.length - answers.filter(a => a !== null).length;
            document.getElementById('current-difficulty').textContent = DIFFICULTY_MAP[q.difficulty] || '-';

            const diffClass = q.difficulty || 'medium';
            let html = `
                <span class="category-badge">${CATEGORY_MAP[q.category] || q.category}</span>
                <span class="difficulty-badge ${diffClass}">${DIFFICULTY_MAP[q.difficulty] || '中等'}</span>
                <div class="question-number">问题 ${q.id}</div>
                <div class="question-text">${q.question_zh}</div>
                <div class="options">
            `;

            if (q.options) {
                q.options.forEach((opt, idx) => {
                    const selected = answers[currentQuestion] && answers[currentQuestion].optionIndex === idx ? 'selected' : '';
                    html += `<button class="option-btn ${selected}" onclick="selectOption(${idx}, ${opt.score})">${opt.text_zh}</button>`;
                });
            }
            html += '</div>';
            card.innerHTML = html;

            document.getElementById('prev-btn').disabled = currentQuestion === 0;
        }

        function selectOption(index, score) {
            answers[currentQuestion] = { questionId: allQuestions[currentQuestion].id, score, optionIndex: index };
            if (currentQuestion < allQuestions.length - 1) {
                currentQuestion++;
                renderQuestion();
            } else {
                submitAnswers();
            }
        }

        function prevQuestion() {
            if (currentQuestion > 0) {
                currentQuestion--;
                renderQuestion();
            }
        }

        async function submitAnswers() {
            const answeredCount = answers.filter(a => a !== null).length;
            if (answeredCount < allQuestions.length) {
                if (!confirm(`您还有 ${allQuestions.length - answeredCount} 道题未作答，确定要提交吗？`)) return;
            }

            const apiAnswers = answers.filter(a => a !== null).map(a => ({
                question_id: a.questionId, score: a.score
            }));

            try {
                const response = await fetch(`/api/session/${shortCode}/submit`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ answers: apiAnswers })
                });
                
                const result = await response.json();
                
                if (result.status === 'success') {
                    document.getElementById('quiz-screen').classList.add('hidden');
                    document.getElementById('thankyou-screen').classList.remove('hidden');
                }
            } catch (error) {
                alert('提交失败，请重试');
            }
        }

        init();
    </script>
</body>
</html>'''
    return HTMLResponse(html_content)

async def _render_report_page(short_code: str, report: dict, session: dict) -> HTMLResponse:
    """渲染报告页面"""
    master_name = session.get("master_name", "未知雇主")
    company = session.get("company", "")
    
    html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>评估报告 - {short_code}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif;
            background: #f5f5f5;
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{ max-width: 900px; margin: 0 auto; }}
        header {{
            text-align: center;
            padding: 30px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin-bottom: 20px;
            border-radius: 16px;
        }}
        header h1 {{ font-size: 2rem; margin-bottom: 10px; }}
        header p {{ opacity: 0.9; }}
        .code-badge {{
            display: inline-block;
            background: rgba(255,255,255,0.2);
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 1.2rem;
            font-weight: bold;
            margin-top: 10px;
            letter-spacing: 2px;
        }}

        .card {{
            background: white;
            border-radius: 16px;
            padding: 25px;
            margin-bottom: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}

        .results-header {{ text-align: center; padding: 15px 0; }}
        .score-display {{ font-size: 3.5rem; font-weight: bold; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }}
        .rating-badge {{ font-size: 1.3rem; margin: 10px 0; }}

        .chart-container {{ position: relative; height: 280px; margin: 20px 0; }}
        .dimension-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-top: 15px; }}
        .dimension-item {{ padding: 12px; border-radius: 10px; background: #f8f9ff; }}
        .dimension-item.strong {{ background: linear-gradient(135deg, #d4edda, #c3e6cb); }}
        .dimension-item.weak {{ background: linear-gradient(135deg, #f8d7da, #f5c6cb); }}
        .dimension-name {{ font-weight: bold; color: #333; margin-bottom: 4px; font-size: 0.9rem; }}
        .dimension-score {{ color: #666; font-size: 0.8rem; }}
        .suggestion-box {{ background: linear-gradient(135deg, #667eea10, #764ba210); border-left: 4px solid #667eea; padding: 18px; border-radius: 8px; margin-top: 15px; }}
        .suggestion-box h3 {{ color: #667eea; margin-bottom: 8px; font-size: 1rem; }}
        .suggestion-box p {{ color: #555; font-size: 0.9rem; line-height: 1.6; }}

        .master-info {{ background: #f8f9ff; padding: 15px; border-radius: 12px; margin-bottom: 20px; }}
        .master-info p {{ margin: 5px 0; color: #555; font-size: 0.9rem; }}
        .master-info strong {{ color: #333; }}

        .collapse-btn {{ background: none; border: none; color: #667eea; cursor: pointer; font-size: 0.9rem; padding: 5px 0; }}
        .collapse-btn:hover {{ text-decoration: underline; }}

        .question-detail {{ padding: 15px; margin-bottom: 10px; border-radius: 10px; background: #f9fafb; border-left: 4px solid #e5e7eb; }}
        .question-detail.correct {{ border-left-color: #4ade80; background: #f0fdf4; }}
        .question-detail.incorrect {{ border-left-color: #f87171; background: #fef2f2; }}
        .question-detail .q-header {{ display: flex; justify-content: space-between; margin-bottom: 8px; }}
        .question-detail .q-category {{ font-size: 0.75rem; color: #666; }}
        .question-detail .q-difficulty {{ font-size: 0.7rem; padding: 2px 8px; border-radius: 10px; }}
        .question-detail .q-difficulty.easy {{ background: #4ade80; color: white; }}
        .question-detail .q-difficulty.medium {{ background: #fbbf24; color: white; }}
        .question-detail .q-difficulty.hard {{ background: #f87171; color: white; }}
        .question-detail .q-text {{ font-size: 0.9rem; color: #333; margin-bottom: 8px; }}
        .question-detail .q-answer {{ font-size: 0.85rem; color: #666; }}
        .question-detail .q-feedback {{ font-size: 0.8rem; color: #888; margin-top: 5px; font-style: italic; }}

        .hidden {{ display: none; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 评估报告</h1>
            <p>家政面试评估结果</p>
            <div class="code-badge">{short_code}</div>
        </header>

        <div class="card">
            <div class="master-info">
                <p><strong>雇主:</strong> {master_name}</p>
                <p><strong>公司:</strong> {company or '未填写'}</p>
                <p><strong>创建时间:</strong> {session.get('created_at', '')[:19].replace('T', ' ')}</p>
                <p><strong>完成时间:</strong> {session.get('completed_at', '')[:19].replace('T', ' ') if session.get('completed_at') else '待完成'}</p>
            </div>
            
            <div class="results-header">
                <div class="score-display" id="total-score">{report['total_score']}</div>
                <div class="rating-badge" id="rating-badge">{report['rating']}</div>
                <div style="color:#888;font-size:0.85rem;margin-top:5px;">
                    共 {report['total_questions']} 道题，已答 {report['answered_count']} 道
                </div>
            </div>
            <div class="chart-container"><canvas id="radar-chart"></canvas></div>
            <div class="suggestion-box">
                <h3>📋 评估建议</h3>
                <p>{report['suggestion']}</p>
            </div>
        </div>

        <div class="card">
            <h3 style="margin-bottom:12px;font-size:1rem;">📊 维度详情</h3>
            <div class="dimension-grid" id="dimension-grid"></div>
        </div>

        <div class="card">
            <h3 style="margin-bottom:12px;font-size:1rem;">✅ 优势领域</h3>
            <div class="dimension-grid" id="strong-points"></div>
            <h3 style="margin:18px 0 12px;font-size:1rem;">⚠️ 需改进领域</h3>
            <div class="dimension-grid" id="weak-points"></div>
        </div>

        <div class="card">
            <h3 style="margin-bottom:12px;font-size:1rem;">📝 逐题分析</h3>
            <button class="collapse-btn" onclick="toggleQuestionDetails()">展开/收起题目详情</button>
            <div id="question-details-container" class="hidden" style="margin-top:15px;"></div>
        </div>
    </div>

    <script>
        const report = {json.dumps(report, ensure_ascii=False)};
        
        const CATEGORY_MAP = {{
            'basic': '基本信息', 'cooking': '烹饪技能', 'childcare': '育儿能力',
            'hygiene': '卫生习惯', 'safety': '安全意识', 'communication': '沟通能力',
            'ethics': '职业道德', 'professionalism': '职业素养', 'elder_care': '老人照护', 'special': '特殊情况'
        }};
        const DIFFICULTY_MAP = {{ 'easy': '基础', 'medium': '中等', 'hard': '进阶' }};
        const SCORE_LABELS = {{ 5: '最佳', 4: '更好', 3: '正确', 1: '错误' }};

        // 渲染雷达图
        const topDims = report.dimension_details.sort((a, b) => b.avg_score - a.avg_score).slice(0, 8);
        new Chart(document.getElementById('radar-chart'), {{
            type: 'radar',
            data: {{
                labels: topDims.map(d => d.dimension),
                datasets: [{{
                    label: '得分',
                    data: topDims.map(d => d.avg_score),
                    backgroundColor: 'rgba(102, 126, 234, 0.2)',
                    borderColor: 'rgba(102, 126, 234, 1)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgba(102, 126, 234, 1)',
                    pointRadius: 4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{ r: {{ min: 0, max: 5, ticks: {{ stepSize: 1 }} }} }},
                plugins: {{ legend: {{ display: false }} }}
            }}
        }});

        // 渲染维度详情
        document.getElementById('dimension-grid').innerHTML = report.dimension_details.map(d => `
            <div class="dimension-item">
                <div class="dimension-name">${{d.category}}: {{d.dimension}}</div>
                <div class="dimension-score">{{d.avg_score}} / 5.0 ({{d.weight}}%权重)</div>
            </div>
        `).join('');

        // 渲染强项弱项
        document.getElementById('strong-points').innerHTML = report.strong_points.map(p => `
            <div class="dimension-item strong">
                <div class="dimension-name">{{p.dimension}}</div>
                <div class="dimension-score">{{p.score}} / 5.0</div>
            </div>
        `).join('');

        document.getElementById('weak-points').innerHTML = report.weak_points.map(p => `
            <div class="dimension-item weak">
                <div class="dimension-name">{{p.dimension}}</div>
                <div class="dimension-score">{{p.score}} / 5.0</div>
            </div>
        `).join('');

        // 渲染题目详情
        function renderQuestionDetails() {{
            const container = document.getElementById('question-details-container');
            container.innerHTML = report.question_details.map(qd => `
                <div class="question-detail ${{qd.is_best ? 'correct' : 'incorrect'}}">
                    <div class="q-header">
                        <span class="q-category">${{qd.category}} · 问题 ${{qd.id}}</span>
                        <span class="q-difficulty ${{qd.difficulty}}">${{DIFFICULTY_MAP[qd.difficulty]}}</span>
                    </div>
                    <div class="q-text">${{qd.question}}</div>
                    <div class="q-answer">
                        候选人回答: <strong>${{qd.selected_answer || '未回答'}}</strong>
                        <span style="margin-left:10px;padding:2px 6px;border-radius:4px;font-size:0.75rem;background:${{qd.is_best ? '#d1fae5' : '#fee2e2'}};color:${{qd.is_best ? '#065f46' : '#991b1b'}};">
                            ${{SCORE_LABELS[qd.score] || '未知'}}
                        </span>
                    </div>
                    ${{qd.selected_feedback ? `<div class="q-feedback">💡 ${{qd.selected_feedback}}</div>` : ''}}
                </div>
            `).join('');
        }}
        renderQuestionDetails();

        function toggleQuestionDetails() {{
            document.getElementById('question-details-container').classList.toggle('hidden');
        }}
    </script>
</body>
</html>'''
    return HTMLResponse(html_content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
