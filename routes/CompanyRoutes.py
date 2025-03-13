from fastapi import APIRouter
from controllers.CompanyController import addCompany,getAllCompanies,deleteCompany
from models.CompanyModel import AddCompany

router = APIRouter()

@router.post("/company/")
async def post_company(company:AddCompany):
    return await addCompany(company)

@router.get("/companies/")
async def get_companies():
    return await getAllCompanies()

@router.delete("/company/{id}")
async def delete_company(id:int):
    return await deleteCompany(id)

