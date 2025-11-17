from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id, "message": "User details would be here."}

@router.post("/")
async def create_user(user: dict):
    return {"message": "User created", "user": user}