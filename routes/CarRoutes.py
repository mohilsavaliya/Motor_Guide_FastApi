# from fastapi import APIRouter
# from models.CarModel import AddCar
# from controllers.CarController import addCar, getAllCars, getCarById, deleteCar

# router = APIRouter()

# @router.post("/add_car/")
# async def post_car(car: AddCar):
#     return await addCar(car)

# @router.get("/cars/")
# async def get_cars():
#     return await getAllCars()

# @router.get("/car/{carId}")
# async def get_car_byId(carId: str):
#     return await getCarById(carId)

# @router.delete("/car/{carId}")
# async def delete_car(carId: str):
#     return await deleteCar(carId)



from fastapi import APIRouter, Form, UploadFile, File
from controllers.CarController import addCarWithFile, getAllCars, getCarById, deleteCar

router = APIRouter()

@router.post("/add_car_with_file/")
async def post_car_with_file(
    car_name: str = Form(...),
    car_model: str = Form(...),
    car_company: str = Form(...),
    car_price: float = Form(...),
    car_color: str = Form(...),
    car_type: str = Form(...),
    car_engine: str = Form(...),
    car_mileage: str = Form(...),
    car_image: UploadFile = File(...)
):
    return await addCarWithFile(
        car_name, car_model, car_company, car_price, car_color, car_type, car_engine, car_mileage, car_image
    )

@router.get("/cars/")
async def get_cars():
    return await getAllCars()

@router.get("/car/{carId}")
async def get_car_byId(carId: str):
    return await getCarById(carId)

@router.delete("/car/{carId}")
async def delete_car(carId: str):
    return await deleteCar(carId)
