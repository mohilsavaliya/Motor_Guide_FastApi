from fastapi import APIRouter
from controllers.CarComparisonContoller import add_comparison, get_comparisons, get_comparison, delete_comparison
from models.CarComparisonModel import CarComparison

router = APIRouter(prefix="/car-comparisons", tags=["Car Comparisons"])

@router.post("/comparison")
def create_comparison(comparison: CarComparison):
    return add_comparison(comparison)

@router.get("/comparisons")
def list_comparisons():
    return get_comparisons()

@router.get("/comparison/{car_1}/{car_2}")
def fetch_comparison(car_1: str, car_2: str):
    return get_comparison(car_1, car_2)

@router.delete("/comparison/{car_1}/{car_2}")
def remove_comparison(car_1: str, car_2: str):
    return delete_comparison(car_1, car_2)