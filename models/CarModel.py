from pydantic import BaseModel, Field, validator
from bson import ObjectId
from typing import Optional

class AddCar(BaseModel):
    car_name: Optional[str] = None
    car_model: Optional[str] = None
    car_company: Optional[str] = None  # This will store company_id as a foreign key
    car_price: Optional[float] = None
    car_image: Optional[str] = None
    car_color: Optional[str] = None
    car_type: Optional[str] = None
    car_engine: Optional[str] = None
    car_mileage: Optional[str] = None

class CarOut(AddCar):
    id: str = Field(alias="_id")
    
    @validator("id", pre=True, always=True)
    def convert_objectId(cls, v):
        return str(v) if isinstance(v, ObjectId) else v
