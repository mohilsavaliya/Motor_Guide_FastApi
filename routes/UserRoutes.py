from fastapi import APIRouter
from controllers.UserController import addUser,getAllUsers,loginUser,deleteUser
from models.UserModel import User,UserOut,UserLogin

router = APIRouter()

@router.post("/user/")
async def post_user(user:User):
    return await addUser(user)

@router.get("/users/")
async def get_users():
    return await getAllUsers()

@router.delete("/user/{id}")
async def delete_user(id:int):
    return await deleteUser(id)

@router.post("/user/login/")
async def login_user(user:UserLogin):
    return await loginUser(user)