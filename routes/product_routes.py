from fastapi import APIRouter
from services.product_service import create_product, get_products

router = APIRouter()

@router.post("/products")
def create_product_route(name: str, price: float, stock_quantity: int):
    return create_product(name, price, stock_quantity)

@router.get("/products")
def get_products_route():
    return get_products()