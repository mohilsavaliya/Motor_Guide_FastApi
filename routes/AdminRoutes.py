from fastapi import APIRouter
from models.AdminModel import Admin,AdminOut,AdminLogin
from controllers.AdminController import addAdmin,getAllAdmins,loginAdmin,deleteAdmin

router = APIRouter()

@router.post("/admin/")
async def post_admin(admin:Admin):
    return await addAdmin(admin)

@router.get("/admins/")
async def get_admins():
    return await getAllAdmins()

@router.post("/admin/login/")
async def login_admin(admin:AdminLogin):
    return await loginAdmin(admin)

@router.delete("/admin/{id}")
async def delete_admin(id:int):
    return await deleteAdmin(id)


