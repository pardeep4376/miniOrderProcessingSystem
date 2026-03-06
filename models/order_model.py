from sqlalchemy import Column, String, Float, DateTime, Text
from datetime import datetime
from .databaseconnection import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(String(36), primary_key=True)
    user_id = Column(String(36), nullable=False)
    products = Column(Text, nullable=False)  # JSON string
    total_amount = Column(Float, nullable=False)
    status = Column(String(20), default="created")
    created_at = Column(DateTime, default=datetime.utcnow)