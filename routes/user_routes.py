from fastapi import APIRouter
from services.user_service import create_user, get_users

router = APIRouter()

@router.post("/users")
def create_user_route(name: str, email: str):
    return create_user(name, email)

@router.get("/users")
def get_users_route():
    return get_users()