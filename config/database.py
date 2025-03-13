from motor.motor_asyncio import AsyncIOMotorClient

#db url
MONGO_URL = "mongodb://localhost:27017"
DATABASE_NAME ="25_internship_fast"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]
role_collection = db["roles"]
user_collection = db["users"]
admin_collection = db["admins"]
car_collection = db["cars"]
company_collection = db["companies"]
car_comparison_collection = db["car_comparison"]