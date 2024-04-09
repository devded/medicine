from fastapi import APIRouter

from database import SessionLocal
from models import CompanyName

router = APIRouter(
    prefix="/company",
    tags=["company"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)


@router.get("/list")
async def read_companies():
    db = SessionLocal()
    companies = db.query(CompanyName).all()
    return companies


@router.get("/{company_id}")
async def read_company(company_id: str):
    db = SessionLocal()
    company = db.query(CompanyName).filter(CompanyName.brand_id == company_id).first()
    return company
