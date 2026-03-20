from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.db import get_db
from app.schemas.sub_categories_schema import SubCategoriesResponse
from app.services import sub_categories_service

sub_categories_route = APIRouter(prefix="/subcategories", tags=["subcategories"])


@sub_categories_route.get(
    "", response_model=list[SubCategoriesResponse], status_code=status.HTTP_200_OK
)
def get_categories(db: Session = Depends(get_db)):
    return sub_categories_service.get_categories_service(db=db)


@sub_categories_route.get(
    "/{sub_categories_id}",
    response_model=SubCategoriesResponse,
    status_code=status.HTTP_200_OK,
)
def get_subcategory_by_id(sub_categories_id: int, db: Session = Depends(get_db)):
    return sub_categories_service.get_subcategory_by_id_service(
        db=db, sub_categories_id=sub_categories_id
    )


@sub_categories_route.post(
    "/create", response_model=SubCategoriesResponse, status_code=status.HTTP_201_CREATED
)
def create_categories(
    sub_categories_title: str = Form(...),
    categories_id: int = Form(...),
    sub_categories_recommended: bool = Form(...),
    sub_categories_image: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):

    return sub_categories_service.create_categories_service(
        sub_categories_title=sub_categories_title,
        categories_id=categories_id,
        sub_categories_image=sub_categories_image,
        sub_categories_recommended=sub_categories_recommended,
        db=db,
    )


@sub_categories_route.patch(
    "/patch/{sub_categories_id}",
    response_model=SubCategoriesResponse,
    status_code=status.HTTP_200_OK,
)
def patch_category(
    sub_categories_id: int,
    sub_categories_title: str | None = Form(None),
    categories_id: int | None = Form(None),
    sub_categories_recommended: bool | None = Form(None),
    sub_categories_image: UploadFile | None = File(None),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):

    return sub_categories_service.patch_categories_service(
        db=db,
        sub_categories_id=sub_categories_id,
        sub_categories_title=sub_categories_title,
        categories_id=categories_id,
        sub_categories_recommended=sub_categories_recommended,
        sub_categories_image=sub_categories_image,
    )


@sub_categories_route.delete(
    "/delete/{sub_categories_id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_category(
    sub_categories_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return sub_categories_service.delete_categories_service(
        db=db, sub_categories_id=sub_categories_id
    )
