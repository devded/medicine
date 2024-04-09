import uvicorn
from fastapi import FastAPI
from routers import generic, brand, company
import models
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(generic.router)
app.include_router(brand.router)
app.include_router(company.router)


# CRUD operations
# Create (Create)


# # Read (GET)
# @app.get("/generic/{generic_id}")
# async def read_generic(generic_id: str):
# 	db = SessionLocal()
# 	generic = db.query(models.Generic).filter(models.Generic.generic_id == generic_id).first()
# 	return generic


# @app.get("/brands")
# async def read_brands():
# 	db = SessionLocal()
# 	brands = db.query(Brand).all()
# 	return brands

# @app.get("/brand/{brand_id}")
# async def read_brand(brand_id: str):
# 	db = SessionLocal()
# 	brand = db.query(Brand).filter(Brand.brand_id == brand_id).first()
# 	return brand

# @app.get("/companies")
# async def read_companies():
# 	db = SessionLocal()
# 	companies = db.query(CompanyName).all()
# 	return companies

# @app.get("/company/{company_id}")
# async def read_company(company_id: str):
# 	db = SessionLocal()
# 	company = db.query(CompanyName).filter(CompanyName.brand_id == company_id).first()
# 	return company



if __name__ == "__main__":
	uvicorn.run(app)
