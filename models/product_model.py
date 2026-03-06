from sqlalchemy import Column, String, Float, Integer
from .databaseconnection import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)