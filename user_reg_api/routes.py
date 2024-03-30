from fastapi import APIRouter, HTTPException
from models import UserRegistration
from services import UserService

router = APIRouter()


@router.post("/register/")
async def register_user(user: UserRegistration):
    try:
        registered_user = UserService.register_user(user)
        return registered_user
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
