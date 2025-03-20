from fastapi import APIRouter
from controllers.CarComparisonController import add_comparison, get_comparisons, delete_comparison
from models.CarComparisonModel import CarComparison

router = APIRouter(prefix="/car-comparisons", tags=["Car Comparisons"])

@router.post("/")
async def create_comparison(comparison: CarComparison):
    return await add_comparison(comparison)

@router.get("/")
async def list_comparisons():
    return await get_comparisons()

@router.get("/{comparison_id}")
async def get_comparison(comparison_id: str):
    return await get_comparisons(comparison_id)

@router.delete("/{comparison_id}")
async def remove_comparison(comparison_id: str):
    return await delete_comparison(comparison_id)
