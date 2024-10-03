from pydantic import BaseModel, EmailStr
from fastapi import APIRouter

router = APIRouter(prefix="/user")

class CreateUser(BaseModel):
    email: EmailStr


@router.post("/")
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }