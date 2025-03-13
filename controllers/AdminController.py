from models.AdminModel import Admin,AdminOut,AdminLogin
from bson import ObjectId
from config.database import admin_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt


async def addAdmin(admin:Admin):
    result = await admin_collection.insert_one(admin.dict())
    return JSONResponse(status_code=201,content={"message":"Admin created successfully"})
    #raise HTTPException(status_code=500,detail="Admin not created")    

async def getAllAdmins():
    admins = await admin_collection.find().to_list(length=None) 
    return [AdminOut(**admin) for admin in admins]

async def loginAdmin(request:AdminLogin):
    foundAdmin = await admin_collection.find_one({"email":request.email})   
    foundAdmin["_id"] = str(foundAdmin["_id"])
    if foundAdmin is None:
        raise HTTPException(status_code=404,detail="Admin not found")
    if "password" in foundAdmin and bcrypt.checkpw(request.password.encode(),foundAdmin["password"].encode()):
        return {"message":"admin login success","admin":AdminOut(**foundAdmin)}
    else:
        raise HTTPException(status_code=404,detail="Admin not found")

async def deleteAdmin(id:int):
    admin = await admin_collection.find_one({"_id":ObjectId(id)})
    if admin is None:
        raise HTTPException(status_code=404,detail="Admin not found")
    await admin_collection.delete_one({"_id":ObjectId(id)})
    return JSONResponse(status_code=200,content={"message":"Admin deleted successfully"
    "Admin not found"})   
    




