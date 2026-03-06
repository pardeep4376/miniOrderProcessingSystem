from models.user_model import User
from models.databaseconnection import SessionLocal
from utils.id_generator import generate_id

def create_user(name, email):
    db = SessionLocal()
    user = User(
        id=generate_id(),
        name=name,
        email=email
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users