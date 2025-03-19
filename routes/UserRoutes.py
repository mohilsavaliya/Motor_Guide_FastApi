from fastapi import APIRouter
from controllers.UserController import addUser, getAllUsers, getUserById, loginUser, deleteUser
from models.UserModel import User, UserLogin

router = APIRouter()

@router.post("/user/")
async def post_user(user: User):
    return await addUser(user)

@router.get("/users/")
async def get_users():
    return await getAllUsers()

@router.get("/user/{userId}")
async def get_user_by_id(userId: str):
    return await getUserById(userId)

@router.delete("/user/{userId}")
async def delete_user(userId: str):
    return await deleteUser(userId)

@router.post("/user/login/")
async def login_user(user: UserLogin):
    return await loginUser(user)
