"""生成支付二维码接口"""
import qrcode
import base64
from io import BytesIO
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

router = APIRouter()

# 支付链接模板（实际应使用真实支付平台）
PAYMENT_LINK_TEMPLATE = "https://pay.example.com/order/{order_id}"


@router.get("/payment/qr/{order_id}")
async def get_payment_qr(order_id: str):
    """生成支付二维码"""
    from src.api.payment import _payment_sessions
    
    # 检查订单是否存在
    session = _payment_sessions.get(order_id)
    if not session:
        raise HTTPException(status_code=404, detail="订单不存在")
    
    # 生成二维码
    payment_url = PAYMENT_LINK_TEMPLATE.format(order_id=order_id)
    img = qrcode.make(payment_url)
    
    # 转换为base64
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return {
        "order_id": order_id,
        "qr_code": f"data:image/png;base64,{img_str}",
        "amount": session["amount"],
        "expire_at": session["expire_at"]
    }


@router.get("/payment/mock_qr/{user_id}")
async def get_mock_payment_qr(user_id: str):
    """获取模拟支付二维码（测试用）"""
    from src.api.payment import _payment_sessions, create_payment, PaymentRequest
    
    # 创建订单
    resp = await create_payment(PaymentRequest(user_id=user_id))
    order_id = resp.order_id
    
    # 生成二维码
    return await get_payment_qr(order_id)
