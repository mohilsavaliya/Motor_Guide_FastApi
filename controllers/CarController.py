from models.CarModel import AddCar
from bson import ObjectId
from config.database import car_collection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import bcrypt

async def addCar(car:AddCar):
    result = await car_collection.insert_one(car.dict())
    return JSONResponse(status_code=201,content={"message":"Car created successfully"})
    #raise HTTPException(status_code=500,detail="Car not created")

async def getAllCars():
    cars = await car_collection.find().to_list(length=None)
    return [AddCar(**car) for car in cars]

async def getCarById(carId:str):
    car = await car_collection.find_one({"_id":ObjectId(carId)})
    if car is None:
        raise HTTPException(status_code=404,detail="Car not found")
    return AddCar(**car)

async def deleteCar(carId:str):
    car = await car_collection.find_one({"_id":ObjectId(carId)})
    if car is None:
        raise HTTPException(status_code=404,detail="Car not found")
    await car_collection.delete_one({"_id":ObjectId(carId)})
    return JSONResponse(status_code=200,content={"message":"Car deleted successfully"})
