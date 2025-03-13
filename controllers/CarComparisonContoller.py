from models.CarComparisonModel import CarComparison
from typing import List
from fastapi import HTTPException

# Fake database storage (for demonstration)
car_comparisons_db: List[CarComparison] = []

def add_comparison(comparison: CarComparison):
    car_comparisons_db.append(comparison)
    return {"message": "Comparison added successfully", "data": comparison}

def get_comparisons():
    return car_comparisons_db

def get_comparison(car_1: str, car_2: str):
    for comparison in car_comparisons_db:
        if comparison.car_1 == car_1 and comparison.car_2 == car_2:
            return comparison
    raise HTTPException(status_code=404, detail="Comparison not found")

def delete_comparison(car_1: str, car_2: str):
    global car_comparisons_db
    car_comparisons_db = [comp for comp in car_comparisons_db if not (comp.car_1 == car_1 and comp.car_2 == car_2)]
    return {"message": "Comparison deleted successfully"}
