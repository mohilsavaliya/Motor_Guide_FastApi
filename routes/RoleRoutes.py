from fastapi import APIRouter
from models.RoleModel import Role
from controllers.RoleController import addRole, getAllRoles, getRoleById, deleteRoleById

router = APIRouter()



@router.post("/role/")
async def post_role(role: Role):
    return await addRole(role)

@router.get("/roles/")
async def get_roles():
    return await getAllRoles()

@router.get("/role/{roleId}")
async def get_role_byId(roleId: str):
    return await getRoleById(roleId)

@router.delete("/role/{roleId}")
async def delete_role_byId(roleId: str):
    return await deleteRoleById(roleId)