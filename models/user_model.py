from sqlalchemy import Column, String
from .databaseconnection import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    name = Column(String(60), nullable=False)
    email = Column(String(60), unique=True, nullable=False)