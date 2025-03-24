# from fastapi import APIRouter
# from controllers.UserController import addUser, getAllUsers, getUserById, loginUser, deleteUser
# from models.UserModel import User, UserLogin

# router = APIRouter()

# @router.post("/user/")
# async def post_user(user: User):
#     return await addUser(user)

# @router.get("/users/")
# async def get_users():
#     return await getAllUsers()

# @router.get("/user/{userId}")
# async def get_user_by_id(userId: str):
#     return await getUserById(userId)

# @router.delete("/user/{userId}")
# async def delete_user(userId: str):
#     return await deleteUser(userId)

# @router.post("/user/login/")
# async def login_user(user: UserLogin):
#     return await loginUser(user)

from fastapi import APIRouter
from controllers.UserController import addUser, getAllUsers, getUserById, loginUser, deleteUser
from models.UserModel import User, UserLogin
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from config.database import db

router = APIRouter()

# @router.post("/api/user/")
# async def post_user():
#     response = JSONResponse(content={"message": "User created successfully"})
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     return await addUser()

@router.post("/user/", status_code=201)
async def create_user(user: User):
    user_dict = user.dict()
    user_dict["role_id"] = "67da63d8ffba085efbfb11d8"  # Set default role

    new_user = db["users"].insert_one(user_dict)
    if not new_user.inserted_id:
        raise HTTPException(status_code=500, detail="User could not be created")

    return {"message": "User created successfully", "user_id": str(new_user.inserted_id)}

@router.get("/api/users/")
async def get_users():
    return await getAllUsers()

@router.get("/api/user/{userId}")
async def get_user_by_id(userId: str):
    return await getUserById(userId)

@router.delete("/api/user/{userId}")
async def delete_user(userId: str):
    return await deleteUser(userId)

@router.post("/api/login/")
async def login_user(user: UserLogin):
    return await loginUser(user)
