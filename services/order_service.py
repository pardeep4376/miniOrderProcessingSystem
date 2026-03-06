import json
from models.order_model import Order
from models.product_model import Product
from models.user_model import User
from models.databaseconnection import SessionLocal
from utils.id_generator import generate_id


def create_order(user_id, items):
    db = SessionLocal()

    try:
        
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            return {"error": "User not found"}

        total_amount = 0
        processed_items = []

        for item in items:
            product = db.query(Product).filter(Product.id == item["product_id"]).first()
            if not product:
                return {"error": "Product not found"}

            if product.stock_quantity < item["quantity"]:
                return {"error": f"Insufficient stock for {product.name}"}

            # Reduce stock
            product.stock_quantity -= item["quantity"]
            total_amount += product.price * item["quantity"]

            processed_items.append(item)

        # Create Order
        order = Order(
            id=generate_id(),
            user_id=user_id,
            products=json.dumps(processed_items),
            total_amount=total_amount,
            status="created"
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        # Return clean JSON response
        return {
            "id": order.id,
            "user_id": order.user_id,
            "items": processed_items,
            "total_amount": order.total_amount,
            "status": order.status
        }

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()


# ✅ CANCEL ORDER
def cancel_order(order_id):
    db = SessionLocal()

    try:
        order = db.query(Order).filter(Order.id == order_id).first()

        if not order:
            return {"error": "Order not found"}

        if order.status == "cancelled":
            return {"error": "Order already cancelled"}

        items = json.loads(order.products)

        # Restore stock
        for item in items:
            product = db.query(Product).filter(Product.id == item["product_id"]).first()
            if product:
                product.stock_quantity += item["quantity"]

        order.status = "cancelled"
        db.commit()

        return {"message": "Order cancelled successfully"}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()


# ✅ GET ALL ORDERS
def get_all_orders():
    db = SessionLocal()

    try:
        orders = db.query(Order).all()

        result = []

        for order in orders:
            result.append({
                "id": order.id,
                "user_id": order.user_id,
                "items": json.loads(order.products),
                "total_amount": order.total_amount,
                "status": order.status
            })

        return result

    finally:
        db.close()

def get_orders_by_status(status: str):
    db = SessionLocal()
    try:
        orders = db.query(Order).filter(Order.status == status).all()

        result = []
        for order in orders:
            result.append({
                "id": order.id,
                "user_id": order.user_id,
                "items": json.loads(order.products),
                "total_amount": order.total_amount,
                "status": order.status
            })

        return result
    finally:
        db.close()