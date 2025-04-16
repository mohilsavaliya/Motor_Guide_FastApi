from models.UserModel import User, UserOut, UserLogin, ResetPasswordReq
from bson import ObjectId
from config.database import user_collection, role_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt
from config.database import db
from models.RoleModel import Role
from utils.SendMail import send_mail
import datetime
import jwt
from typing import Optional, Dict, Any

async def addUser(user: User):
    user_data = user.dict()
    
    # Assign a hardcoded role ID
    user_data["role_id"] = "67da63d8ffba085efbfb11d8" #user
    # user_data["role_id"] = "67da4df256e772c9467c5da6" #admin

    # Ensure MongoDB insertion is awaited correctly
    result = await db["users"].insert_one(user_data)

    if result.inserted_id:  # Check if insertion was successful
        created_user = await db["users"].find_one({"_id": result.inserted_id})
        created_user["_id"] = str(created_user["_id"])  # Convert ObjectId to string
        return created_user

    raise HTTPException(status_code=500, detail="User creation failed")


async def getAllUsers():
    users = await user_collection.find().to_list(length=None)

    for user in users:
        if "role_id" in user and isinstance(user["role_id"], ObjectId):
            user["role_id"] = str(user["role_id"])

        # Fetch role details
        role = await role_collection.find_one({"_id": ObjectId(user["role_id"])})
        if role:
            role["_id"] = str(role["_id"])
            user["role"] = role

    return [UserOut(**user) for user in users]


async def getUserById(userId: str):
    user = await user_collection.find_one({"_id": ObjectId(userId)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user["_id"] = str(user["_id"])
    user["role_id"] = str(user["role_id"])

    # Fetch role details
    role = await role_collection.find_one({"_id": ObjectId(user["role_id"])})
    if role:
        role["_id"] = str(role["_id"])
        user["role"] = role

    return UserOut(**user)


async def loginUser(request: UserLogin):
    foundUser = await user_collection.find_one({"email": request.email})
    
    if not foundUser:
        raise HTTPException(status_code=404, detail="User not found")
    
    foundUser["_id"] = str(foundUser["_id"])
    foundUser["role_id"] = str(foundUser["role_id"])

    # Validate password
    if bcrypt.checkpw(request.password.encode(), foundUser["password"].encode()):
        role = await role_collection.find_one({"_id": ObjectId(foundUser["role_id"])})
        foundUser["role"] = role
        return {"message": "User login success", "user": UserOut(**foundUser)}
    else:
        raise HTTPException(status_code=400, detail="Invalid password")


async def deleteUser(userId: str):
    result = await user_collection.delete_one({"_id": ObjectId(userId)})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

SECRET_KEY ="motorguide"
def generate_token(email:str):
    expiration =datetime.datetime.utcnow()+datetime.timedelta(hours=1)
    payload = {"sub":email,"exp":expiration}
    token = jwt.encode(payload,SECRET_KEY,algorithm="HS256")
    return token


async def forgotPassword(email:str):
    foundUser = await user_collection.find_one({"email":email})
    if not foundUser:
        raise HTTPException(status_code=404,detail="email not found")
    
    token = generate_token(email)
    resetLink = f"http://localhost:5173/resetpassword/{token}"
    body = f"""
    <html>
        <h1>HELLO THIS IS RESET PASSWORD LINK EXPIRES IN 1 hour</h1>
        <a href= "{resetLink}">RESET PASSWORD</a>
    </html>
    """
    subject = "RESET PASSWORD"
    send_mail(email,subject,body)
    return {"message":"reset link sent successfully"}
    

async def resetPassword(data: ResetPasswordReq):
    try:
        payload = jwt.decode(data.token, SECRET_KEY, algorithms="HS256")
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=421, detail="Token is not valid...")

        # Hash the new password and decode the result to store it as a string
        hashed_password = bcrypt.hashpw(data.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        await user_collection.update_one({"email": email}, {"$set": {"password": hashed_password}})

        return {"message": "Password updated successfully"}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=500, detail="JWT is expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=500, detail="JWT is invalid")