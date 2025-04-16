from fastapi import APIRouter, HTTPException
from controllers.UserController import addUser, getAllUsers, getUserById, loginUser, deleteUser, forgotPassword, resetPassword

from models.UserModel import User, UserLogin ,ResetPasswordReq

router = APIRouter()

@router.post("/user/")
async def create_user(user: User):
    new_user = await addUser(user)  
    if not new_user:
        raise HTTPException(status_code=400, detail="Failed to create user")
    return {"message": "User created successfully", "user": new_user}

@router.get("/users/")
async def get_users():
    return await getAllUsers()

@router.get("/user/{userId}")
async def get_user_by_id(userId: str):
    return await getUserById(userId)

@router.delete("/user/{userId}")
async def delete_user(userId: str):
    return await deleteUser(userId)

@router.post("/login/")
async def login_user(user: UserLogin):
    return await loginUser(user)

@router.post("/forgotpassword")
async def forgot_password(email:str):
    return await forgotPassword(email)

@router.post("/resetpassword")
async def reset_password(data:ResetPasswordReq):
    return await resetPassword(data)