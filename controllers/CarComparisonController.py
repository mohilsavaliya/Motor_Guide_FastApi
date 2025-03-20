from models.CarComparisonModel import CarComparison
from config.database import car_collection, car_comparison_collection
from fastapi import HTTPException
from bson import ObjectId
from typing import List, Dict

async def fetch_car_details(car_ids: List[str]) -> List[Dict]:
    car_objects = []
    for car_id in car_ids:
        car = await car_collection.find_one({"_id": ObjectId(car_id)})
        if not car:
            raise HTTPException(status_code=404, detail=f"Car with ID {car_id} not found")
        car["_id"] = str(car["_id"])  # Convert ObjectId to string
        car_objects.append(car)
    return car_objects

async def add_comparison(comparison: CarComparison):
    car_details = await fetch_car_details(comparison.car_ids)
    comparison_dict = comparison.dict(by_alias=True)
    comparison_dict["cars"] = car_details  # Store full car details in the response
    result = await car_comparison_collection.insert_one(comparison_dict)
    return {"message": "Comparison added successfully", "comparison_id": str(result.inserted_id)}

async def get_comparisons(comparison_id: str = None):
    if comparison_id:
        comparison = await car_comparison_collection.find_one({"_id": ObjectId(comparison_id)})
        if not comparison:
            raise HTTPException(status_code=404, detail="Comparison not found")
        comparison["_id"] = str(comparison["_id"])
        return comparison
    else:
        comparisons = await car_comparison_collection.find().to_list(None)
        for comparison in comparisons:
            comparison["_id"] = str(comparison["_id"])
        return comparisons

async def delete_comparison(comparison_id: str):
    result = await car_comparison_collection.delete_one({"_id": ObjectId(comparison_id)})
    if result.deleted_count == 1:
        return {"message": "Comparison deleted successfully"}
    raise HTTPException(status_code=404, detail="Comparison not found")
