from pydantic import BaseModel,Field,validator
from bson import ObjectId
from typing import Optional, Dict, Any
import bcrypt   #pip install bcrypt

        
class AddCar(BaseModel):
    car_name:Optional[str] = None
    car_model:Optional[str] = None
    car_company:Optional[str] = None
    car_price:Optional[float] = None
    car_image:Optional[str] = None
    car_color:Optional[str] = None
    car_type:Optional[str] = None
    car_engine:Optional[str] = None
    car_mileage:Optional[str] = None

class CarOut(AddCar):
    id:str = Field(alias="_id")    
    car_name:Optional[str] = None
    car_model:Optional[str] = None
    car_company:Optional[str] = None
    car_price:Optional[float] = None
    car_image:Optional[str] = None
    car_color:Optional[str] = None
    car_type:Optional[str] = None
    car_engine:Optional[str] = None
    car_mileage:Optional[str] = None
    
    @validator("id",pre=True,always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v
    

    