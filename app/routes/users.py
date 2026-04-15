from fastapi import APIRouter
from app.schemas.UserViewModel import User

router = APIRouter()

@router.get("/usermethod")
async def getUsers():
    return "User Details fetched Successfully"

@router.post("/createUser")
async def createUser(userDetails:User):
    return userDetails.name


