from models.CompanyModel import Company,CompanyOut
from bson import ObjectId
from config.database import company_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt

async def addCompany(company:Company):
    result = await company_collection.insert_one(company.dict())
    return JSONResponse(status_code=201,content={"message":"Company created successfully"})

async def getAllCompanies():
    companies = await company_collection.find().to_list(length=None)
    return [Company(**company) for company in companies]

async def deleteCompany(id:int):
    company = await company_collection.find_one({"_id":ObjectId(id)})
    if company is None:
        raise HTTPException(status_code=404,detail="Company not found")
    await company_collection.delete_one({"_id":ObjectId(id)})
    return JSONResponse(status_code=200,content={"message":"Company deleted successfully"})

