# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# from bson import ObjectId
# from models.CarModel import AddCar, CarOut
# from config.database import car_collection, company_collection

# async def addCar(car: AddCar):
#     # Validate if the company exists
#     company = await company_collection.find_one({"_id": ObjectId(car.car_company)})
#     if not company:
#         raise HTTPException(status_code=404, detail="Company not found")
    
#     car_dict = car.dict()
#     car_dict["_id"] = ObjectId()  # Assign a unique ObjectId to the car
    
#     await car_collection.insert_one(car_dict)
#     return JSONResponse(status_code=201, content={"message": "Car created successfully", "car_id": str(car_dict["_id"])})


# async def getAllCars():
#     cars = await car_collection.find().to_list(length=None)
    
#     for car in cars:
#         car["_id"] = str(car["_id"])
    
#     return [CarOut(**car) for car in cars]

# async def getCarById(carId: str):
#     try:
#         obj_id = ObjectId(carId)
#     except:
#         raise HTTPException(status_code=400, detail="Invalid car ID format")

#     car = await car_collection.find_one({"_id": obj_id})
#     if not car:
#         raise HTTPException(status_code=404, detail="Car not found")
    
#     car["_id"] = str(car["_id"])
#     return CarOut(**car)

# async def deleteCar(carId: str):
#     try:
#         obj_id = ObjectId(carId)
#     except:
#         raise HTTPException(status_code=400, detail="Invalid car ID format")
    
#     car = await car_collection.find_one({"_id": obj_id})
#     if car is None:
#         raise HTTPException(status_code=404, detail="Car not found")
    
#     await car_collection.delete_one({"_id": obj_id})
#     return JSONResponse(status_code=200, content={"message": "Car deleted successfully"})

import os
import shutil
from fastapi import HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from bson import ObjectId
from models.CarModel import AddCar, CarOut
from config.database import car_collection, company_collection
from utils.CloudinaryUtil import upload_image  # Cloudinary for image hosting

# Local directory for image storage (if needed)
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def addCarWithFile(
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
    # Validate company existence
    company = await company_collection.find_one({"_id": ObjectId(car_company)})
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    try:
        # Save image locally
        file_ext = car_image.filename.split(".")[-1]
        file_path = os.path.join(UPLOAD_DIR, f"{ObjectId()}.{file_ext}")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(car_image.file, buffer)

        # Upload image to Cloudinary and get the URL
        image_url = await upload_image(file_path)

        # Prepare car data
        car_dict = {
            "car_name": car_name,
            "car_model": car_model,
            "car_company": ObjectId(car_company),
            "car_price": car_price,
            "car_color": car_color,
            "car_type": car_type,
            "car_engine": car_engine,
            "car_mileage": car_mileage,
            "car_image": image_url  # Store image URL
        }

        # Insert into database
        savedCar = await car_collection.insert_one(car_dict)
        return JSONResponse(status_code=201, content={"message": "Car created successfully", "car_id": str(savedCar.inserted_id)})

    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Error adding car")

async def getAllCars():
    cars = await car_collection.find().to_list(length=None)

    for car in cars:
        car["_id"] = str(car["_id"])
        car["car_company"] = str(car["car_company"])  # Convert ObjectId to string

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
    car["car_company"] = str(car["car_company"])  # Convert ObjectId to string
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
