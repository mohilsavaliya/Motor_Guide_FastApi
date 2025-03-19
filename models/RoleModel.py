from pydantic import BaseModel, Field, validator
from bson import ObjectId
from typing import Optional

class Role(BaseModel):
    role_name: str
    description: str
    
    @validator("role_name", pre=True, always=True)
    def validate_role_name(cls, v):
        if v.lower() not in ["admin", "user"]:
            raise ValueError("Role must be either 'admin' or 'user'")
        return v
    
class RoleOut(Role):
    id: str = Field(alias="_id")
    
    @validator("id", pre=True, always=True)
    def convert_objectId(cls, v):
        return str(v) if isinstance(v, ObjectId) else v
