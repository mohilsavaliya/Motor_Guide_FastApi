from fastapi import HTTPException
from fastapi.responses import JSONResponse
from bson import ObjectId
from models.CarModel import AddCar, CarOut
from config.database import car_collection, company_collection

async def addCar(car: AddCar):
    # Validate if the company exists
    company = await company_collection.find_one({"_id": ObjectId(car.car_company)})
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    car_dict = car.dict()
    car_dict["_id"] = ObjectId()  # Assign a unique ObjectId to the car
    
    await car_collection.insert_one(car_dict)
    return JSONResponse(status_code=201, content={"message": "Car created successfully", "car_id": str(car_dict["_id"])})

async def getAllCars():
    cars = await car_collection.find().to_list(length=None)
    
    for car in cars:
        car["_id"] = str(car["_id"])
    
    return [CarOut(**car) for car in cars]

async def getCarById(carId: str):
    try:
        obj_id = ObjectId(carId)
    except:
        raise HTTPException(status_code=400, detail="Invalid car ID format")

    car = await car_collection.find_one({"_id": obj_id})
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    car["_id"] = str(car["_id"])
    return CarOut(**car)

async def deleteCar(carId: str):
    try:
        obj_id = ObjectId(carId)
    except:
        raise HTTPException(status_code=400, detail="Invalid car ID format")
    
    car = await car_collection.find_one({"_id": obj_id})
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    
    await car_collection.delete_one({"_id": obj_id})
    return JSONResponse(status_code=200, content={"message": "Car deleted successfully"})
