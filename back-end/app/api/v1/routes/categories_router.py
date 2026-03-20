from fastapi import APIRouter, status, Depends, Form, File, UploadFile
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.db import get_db
from app.schemas.categories_schema import CategoriesResponse
from app.services import categories_service

categories_route = APIRouter(prefix="/categories", tags=["Categories"])


@categories_route.get(
    "", response_model=list[CategoriesResponse], status_code=status.HTTP_200_OK
)
def get_categories(db: Session = Depends(get_db)):
    return categories_service.get_categories_services(db=db)


@categories_route.get(
    "/{category_id}", response_model=CategoriesResponse, status_code=status.HTTP_200_OK
)
def get_categories_id(category_id: int, db: Session = Depends(get_db)):
    return categories_service.get_categories_id_services(db=db, category_id=category_id)


@categories_route.post(
    "/create", response_model=CategoriesResponse, status_code=status.HTTP_201_CREATED
)
def create_categories(
    title: str = Form(...),
    recommended: bool = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return categories_service.create_categories_services(
        title=title,
        image=image,
        recommended=recommended,
        db=db,
    )


@categories_route.patch(
    "/update/{categories_id}",
    response_model=CategoriesResponse,
    status_code=status.HTTP_200_OK,
)
def patch_categories(
    categories_id: int,
    title: str | None = Form(None),
    recommended: bool | None = Form(None),
    image: UploadFile | None = File(None),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return categories_service.patch_categories_services(
        categories_id=categories_id,
        title=title,
        recommended=recommended,
        image=image,
        db=db,
    )


@categories_route.delete(
    "/delete/{categories_id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_categories(
    categories_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return categories_service.delete_categories_services(
        categories_id=categories_id, db=db
    )
