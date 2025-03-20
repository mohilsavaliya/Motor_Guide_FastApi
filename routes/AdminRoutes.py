# from fastapi import APIRouter
# from models.AdminModel import Admin,AdminOut,AdminLogin
# from controllers.AdminController import addAdmin,getAllAdmins,loginAdmin,deleteAdmin

# router = APIRouter()

# @router.post("/admin/")
# async def post_admin(admin:Admin):
#     return await addAdmin(admin)

# @router.get("/admins/")
# async def get_admins():
#     return await getAllAdmins()

# @router.post("/admin/login/")
# async def login_admin(admin:AdminLogin):
#     return await loginAdmin(admin)

# @router.delete("/admin/{id}")
# async def delete_admin(id:int):
#     return await deleteAdmin(id)

from fastapi import APIRouter
from controllers.AdminController import addAdmin, getAllAdmins, getAdminById, loginAdmin, deleteAdmin
from models.AdminModel import Admin, AdminLogin

router = APIRouter()

@router.post("/admin/")
async def post_admin(admin: Admin):
    return await addAdmin(admin)

@router.get("/admins/")
async def get_admins():
    return await getAllAdmins()

@router.get("/admin/{adminId}")
async def get_admin_by_id(adminId: str):
    return await getAdminById(adminId)

@router.delete("/admin/{adminId}")
async def delete_admin(adminId: str):
    return await deleteAdmin(adminId)

@router.post("/admin/login/")
async def login_admin(admin: AdminLogin):
    return await loginAdmin(admin)




