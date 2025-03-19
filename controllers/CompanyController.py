# from models.CompanyModel import AddCompany,CompanyOut
# from bson import ObjectId
# from config.database import company_collection
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# import bcrypt

# async def addCompany(company:AddCompany):
#     result = await company_collection.insert_one(company.dict())
#     return JSONResponse(status_code=201,content={"message":"Company created successfully"})

# async def getAllCompanies():
#     companies = await company_collection.find().to_list(length=None)
#     return [AddCompany(**company) for company in companies]

# async def deleteCompany(id:int):
#     company = await company_collection.find_one({"_id":ObjectId(id)})
#     if company is None:
#         raise HTTPException(status_code=404,detail="Company not found")
#     await company_collection.delete_one({"_id":ObjectId(id)})
#     return JSONResponse(status_code=200,content={"message":"Company deleted successfully"})



from fastapi import HTTPException
from fastapi.responses import JSONResponse
from bson import ObjectId
from models.CompanyModel import AddCompany, CompanyOut
from config.database import company_collection

async def addCompany(company: AddCompany):
    company_dict = company.dict()
    company_dict["_id"] = ObjectId()  # Assign MongoDB's ObjectId automatically
    
    await company_collection.insert_one(company_dict)
    return JSONResponse(status_code=201, content={"message": "Company created successfully", "company_id": str(company_dict["_id"])})

async def getAllCompanies():
    companies = await company_collection.find().to_list(length=None)
    
    for company in companies:
        company["_id"] = str(company["_id"])
    
    return [CompanyOut(**company) for company in companies]

async def getCompanyById(id: str):
    try:
        obj_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Invalid company ID format")

    company = await company_collection.find_one({"_id": obj_id})
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    company["_id"] = str(company["_id"])
    return CompanyOut(**company)

async def deleteCompany(id: str):
    try:
        obj_id = ObjectId(id)
    except:
        raise HTTPException(status_code=400, detail="Invalid company ID format")
    
    company = await company_collection.find_one({"_id": obj_id})
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    
    await company_collection.delete_one({"_id": obj_id})
    return JSONResponse(status_code=200, content={"message": "Company deleted successfully"})
