from fastapi import APIRouter

from database import SessionLocal
from models import Brand

router = APIRouter(
    prefix="/brand",
    tags=["brand"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/list")
async def read_brands():
    db = SessionLocal()
    brands = db.query(Brand).all()
    return brands


@router.get("/{brand_id}")
async def read_brand(brand_id: str):
    db = SessionLocal()
    brand = db.query(Brand).filter(Brand.brand_id == brand_id).first()
    return brand
