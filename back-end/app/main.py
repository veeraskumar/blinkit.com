from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.database.db import Base, engine
from app.api.v1.routes import (
    auth_router,
    categories_router,
    products_router,
    sub_categories_router,
)


app: FastAPI = FastAPI(title="Blinkit")

origins = [
    "http://localhost:3000",  # for local dev
    "https://blinkit-frontend.com",  # production domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=auth_router.auth_router)
app.include_router(router=categories_router.categories_route)
app.include_router(router=products_router.products_route)
app.include_router(router=sub_categories_router.sub_categories_route)


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}
