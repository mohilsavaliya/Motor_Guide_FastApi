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
