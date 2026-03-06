from fastapi import APIRouter
from services.order_service import create_order, cancel_order, get_all_orders,get_orders_by_status
from schemas.order_schema import OrderCreate

router = APIRouter()


@router.post("/orders")
def create_order_route(order: OrderCreate):
    return create_order(
        order.user_id,
        [item.dict() for item in order.items]
    )

@router.get("/orders")
def get_orders_route():
    return get_all_orders()


@router.get("/orders/status/{status}")
def get_orders_by_status_route(status: str):
    return get_orders_by_status(status)


@router.put("/orders/{order_id}/cancel")
def cancel_order_route(order_id: str):
    return cancel_order(order_id)


