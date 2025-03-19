# from pydantic import BaseModel,Field,validator
# from bson import ObjectId
# from typing import Optional, Dict, Any
# import bcrypt  

# class AddCompany(BaseModel):
#     company_name:str
#     company_description:str


# class CompanyOut(AddCompany):
#     id:str = Field(alias="_id")  
#     # company_id:Optional[str] = None  
#     # company_name:Optional[str] = None
#     # company_description:Optional[str] = None
    
#     @validator("id",pre=True,always=True)
#     def convert_objectId(cls,v):
#         if isinstance(v,ObjectId):
#             return str(v)
        
#         return v
    

from pydantic import BaseModel, Field, validator
from bson import ObjectId
from typing import Optional

class AddCompany(BaseModel):
    company_name: str
    company_description: str

class CompanyOut(AddCompany):
    id: str = Field(alias="_id")
    
    @validator("id", pre=True, always=True)
    def convert_objectId(cls, v):
        return str(v) if isinstance(v, ObjectId) else v
