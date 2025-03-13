from pydantic import BaseModel,Field,validator
from typing import List, Optional
from bson import ObjectId

class CarComparison(BaseModel):
    car_1: str
    car_2: str
    comparison_criteria: List[str]  # Example: ["mileage", "price", "safety"]
    better_option: Optional[str] = None  # Stores which car is better based on comparison

    class Config:
        orm_mode = True

class CarComparisonOut(CarComparison):
    id: str = Field(alias="_id")
    car_1: Optional[str] = None
    car_2: Optional[str] = None

@validator("id", pre=True, always=True)
def convert_objectId(cls, v):
    if isinstance(v, ObjectId):
        return str(v)
    return v


    

# class CarComparisonInDB(CarComparison):
#     id: str = Field(alias="_id")
#     car_1: str
#     car_2: str



