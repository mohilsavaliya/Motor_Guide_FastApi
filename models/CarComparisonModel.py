from pydantic import BaseModel, Field, validator
from typing import List
import uuid

class CarComparison(BaseModel):
    car_ids: List[str]  # List of car IDs to compare (Minimum 2, Maximum 4)
    better_option: str = None  # Stores which car is better based on comparison

    @validator("car_ids")
    def validate_car_ids(cls, value):
        if not (2 <= len(value) <= 4):
            raise ValueError("You must provide between 2 and 4 car IDs for comparison.")
        return value

class CarComparisonInDB(CarComparison):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="_id")
