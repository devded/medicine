from fastapi import APIRouter, Depends, HTTPException

import models
from database import SessionLocal


router = APIRouter(
    prefix="/generic",
    tags=["generic"],
    # dependencies=[Depends(get_token_header)],
    # responses={404: {"description": "Not found"}},
)

@router.get("/{generic_id}")
async def read_generic(generic_id: str):
	db = SessionLocal()
	generic = db.query(models.Generic).filter(models.Generic.generic_id == generic_id).first()
	return generic
