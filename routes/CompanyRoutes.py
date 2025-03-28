from fastapi import APIRouter
from controllers.CompanyController import addCompany, getAllCompanies, getCompanyById, deleteCompany
from models.CompanyModel import AddCompany

router = APIRouter()

@router.post("/company/")
async def post_company(company: AddCompany):
    return await addCompany(company)

@router.get("/companies/")
async def get_companies():
    return await getAllCompanies()

@router.get("/company/{id}")
async def get_company(id: str):
    return await getCompanyById(id)

@router.delete("/company/{id}")
async def delete_company(id: str):
    return await deleteCompany(id)
