import models
import uvicorn
from database import engine
from fastapi import FastAPI
from routers import brand, company, generic

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(generic.router)
app.include_router(brand.router)
app.include_router(company.router)


if __name__ == "__main__":
    uvicorn.run(app)
