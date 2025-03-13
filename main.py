from fastapi import FastAPI
from routes.RoleRoutes import router as role_router
from routes.UserRoutes import router as user_router
from routes.AdminRoutes import router as admin_router
from routes.CarRoutes import router as addcar_router
from routes.CompanyRoutes import router as company_router
from routes.CarComparisonRoutes import router as car_comparison_router


# import cors middleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(role_router)
app.include_router(user_router)
app.include_router(admin_router)
app.include_router(addcar_router)
app.include_router(company_router)
app.include_router(car_comparison_router)


#routes