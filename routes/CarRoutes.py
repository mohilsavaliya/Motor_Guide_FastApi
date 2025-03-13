from fastapi import APIRouter,HTTPException
from models.CarModel import AddCar
from controllers.CarController import addCar,getAllCars,getCarById,deleteCar

router = APIRouter()

@router.post("/add_car/")
async def post_car(car:AddCar):
    return await addCar(car)

@router.get("/cars/")
async def get_cars():
    return await getAllCars()

@router.get("/car/{carId}")
async def get_car_byId(carId:str):
    return await getCarById(carId)

@router.delete("/car/{carId}")
async def delete_car(carId:str):
    return await deleteCar(carId)




