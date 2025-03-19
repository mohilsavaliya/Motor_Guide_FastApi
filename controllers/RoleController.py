from config.database import role_collection
from models.RoleModel import Role, RoleOut
from bson import ObjectId
from fastapi import HTTPException

async def getAllRoles():
    roles = await role_collection.find().to_list(length=None)
    return [RoleOut(**role) for role in roles if 'role_name' in role]

async def addRole(role: Role):
    role_dict = role.dict()
    role_dict["_id"] = ObjectId()  # Assign a unique ObjectId to the role
    await role_collection.insert_one(role_dict)
    return {"message": "Role Created Successfully", "role_id": str(role_dict["_id"])}

async def deleteRoleById(roleId: str):
    try:
        obj_id = ObjectId(roleId)
    except:
        raise HTTPException(status_code=400, detail="Invalid role ID format")
    
    role = await role_collection.find_one({"_id": obj_id})
    if role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    
    await role_collection.delete_one({"_id": obj_id})
    return {"message": "Role Deleted Successfully"}

async def getRoleById(roleId: str):
    try:
        obj_id = ObjectId(roleId)
    except:
        raise HTTPException(status_code=400, detail="Invalid role ID format")
    
    role = await role_collection.find_one({"_id": obj_id})
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    role["_id"] = str(role["_id"])
    return RoleOut(**role)