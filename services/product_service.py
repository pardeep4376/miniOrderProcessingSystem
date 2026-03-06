from models.product_model import Product
from models.databaseconnection import SessionLocal
from utils.id_generator import generate_id

def create_product(name, price, stock_quantity):
    db = SessionLocal()
    product = Product(
        id=generate_id(),
        name=name,
        price=price,
        stock_quantity=stock_quantity
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    db.close()
    return product

def get_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products