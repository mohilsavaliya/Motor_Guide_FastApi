from models.UserModel import User, UserOut, UserLogin
from bson import ObjectId
from config.database import user_collection, role_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt
from config.database import db


# async def addUser(user: User):
#     user_dict = user.dict()
#     user_dict["_id"] = ObjectId()  # Automatically generate user ID
#     user_dict["role_id"] = ObjectId(user.role_id)  # Convert role_id to ObjectId

#     # Encrypt password before storing
#     user_dict["password"] = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode()

#     # Insert into MongoDB
#     result = await user_collection.insert_one(user_dict)

#     return {"message": "User added successfully", "user_id": str(result.inserted_id)}

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
