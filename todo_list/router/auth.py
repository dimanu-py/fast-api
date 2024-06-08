from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/")
async def authenticate_user():
    return {"message": "User authenticated successfully"}
