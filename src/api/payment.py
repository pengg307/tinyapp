"""支付相关接口"""

from typing import Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import time
import json
from pathlib import Path
from datetime import datetime, timedelta

router = APIRouter()

# 内存存储支付状态 (实际应使用数据库)
_payment_sessions: dict[str, dict[str, Any]] = {}

# 支付配置
PAYMENT_AMOUNT = 9.9  # 价格
PAYMENT_EXPIRE_HOURS = 24  # 有效期24小时


class PaymentRequest(BaseModel):
    """支付请求"""
    user_id: str = "anonymous"


class PaymentResponse(BaseModel):
    """支付响应"""
    success: bool
    order_id: str | None
    amount: float
    message: str
    expire_at: str | None = None


class PaymentVerifyRequest(BaseModel):
    """支付验证请求"""
    order_id: str
    user_id: str


class PaymentVerifyResponse(BaseModel):
    """支付验证响应"""
    paid: bool
    expire_at: str | None
    remaining_hours: float | None


@router.post("/api/payment", response_model=PaymentResponse)
async def create_payment(req: PaymentRequest):
    """创建支付订单"""
    order_id = f"ORD{int(time.time())}{hash(req.user_id) % 10000:04d}"
    expire_at = datetime.now() + timedelta(hours=PAYMENT_EXPIRE_HOURS)
    
    _payment_sessions[order_id] = {
        "user_id": req.user_id,
        "amount": PAYMENT_AMOUNT,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "expire_at": expire_at.isoformat(),
        "paid_at": None
    }
    
    return PaymentResponse(
        success=True,
        order_id=order_id,
        amount=PAYMENT_AMOUNT,
        message=f"请扫码支付 {PAYMENT_AMOUNT} 元，有效期 {PAYMENT_EXPIRE_HOURS} 小时",
        expire_at=expire_at.isoformat()
    )


@router.post("/api/payment/verify", response_model=PaymentVerifyResponse)
async def verify_payment(req: PaymentVerifyRequest):
    """验证支付状态"""
    session = _payment_sessions.get(req.order_id)
    
    if not session:
        raise HTTPException(status_code=404, detail="订单不存在")
    
    if session["status"] != "paid":
        return PaymentVerifyResponse(paid=False, expire_at=None, remaining_hours=0)
    
    # 检查是否过期
    expire_at = datetime.fromisoformat(session["expire_at"])
    remaining = (expire_at - datetime.now()).total_seconds() / 3600
    
    if remaining <= 0:
        return PaymentVerifyResponse(paid=False, expire_at=None, remaining_hours=0)
    
    return PaymentVerifyResponse(
        paid=True,
        expire_at=session["expire_at"],
        remaining_hours=round(remaining, 1)
    )


@router.post("/api/payment/mock_pay")
async def mock_payment(req: PaymentRequest):
    """模拟支付（仅用于测试）"""
    # 查找该用户的待支付订单
    for order_id, session in _payment_sessions.items():
        if session["user_id"] == req.user_id and session["status"] == "pending":
            session["status"] = "paid"
            session["paid_at"] = datetime.now().isoformat()
            
            return {
                "success": True,
                "message": "支付成功！",
                "expire_at": session["expire_at"],
                "remaining_hours": round(
                    (datetime.fromisoformat(session["expire_at"]) - datetime.now()).total_seconds() / 3600, 1
                )
            }
    
    # 如果没有待支付订单，创建一个新的
    return await create_payment(req)


@router.get("/api/payment/status/{user_id}")
async def get_payment_status(user_id: str):
    """查询用户支付状态"""
    for order_id, session in _payment_sessions.items():
        if session["user_id"] == user_id and session["status"] == "paid":
            expire_at = datetime.fromisoformat(session["expire_at"])
            remaining = (expire_at - datetime.now()).total_seconds() / 3600
            
            if remaining > 0:
                return {
                    "paid": True,
                    "order_id": order_id,
                    "expire_at": session["expire_at"],
                    "remaining_hours": round(remaining, 1)
                }
    
    return {"paid": False, "message": "未支付或已过期"}
