from fastapi import APIRouter, Depends, status, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.database.db import get_db
from app.schemas.products_schema import ProductsResponse, ProductsType
from app.services import products_service

products_route = APIRouter(prefix="/products", tags=["Products"])


@products_route.get(
    "", response_model=list[ProductsResponse], status_code=status.HTTP_200_OK
)
def get_products(db: Session = Depends(get_db)):
    return products_service.get_all_products_service(db=db)


@products_route.get(
    "/search", response_model=list[ProductsResponse], status_code=status.HTTP_200_OK
)
def search_products(q: str, db: Session = Depends(get_db)):
    return products_service.search_products_service(db=db, q=q)


# Products by subcategory
@products_route.get(
    "/category/{sub_categories_id}",
    response_model=list[ProductsResponse],
    status_code=status.HTTP_200_OK,
)
def get_products_by_category(sub_categories_id: int, db: Session = Depends(get_db)):
    return products_service.get_products_by_category_service(
        db=db, sub_categories_id=sub_categories_id
    )


@products_route.get(
    "/{products_id}",
    response_model=ProductsResponse,
    status_code=status.HTTP_200_OK,
)
def get_product_by_id(products_id: int, db: Session = Depends(get_db)):
    return products_service.get_prd_by_id(db=db, id=products_id)


@products_route.post(
    "/create", response_model=ProductsResponse, status_code=status.HTTP_201_CREATED
)
def create_products(
    title: str = Form(...),
    quantity: int = Form(...),
    price: int = Form(...),
    discount: int = Form(0),
    product_type: ProductsType = Form(...),
    sub_category_id: int = Form(...),
    recommended: bool = Form(...),
    images: list[UploadFile] = File(...),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):

    return products_service.create_products_services(
        title=title,
        quantity=quantity,
        price=price,
        discount=discount,
        product_type=product_type,
        recommended=recommended,
        sub_category_id=sub_category_id,
        images=images,
        db=db,
    )


@products_route.patch(
    "/patch/{products_id}",
    response_model=ProductsResponse,
    status_code=status.HTTP_200_OK,
)
def patch_products(
    products_id: int,
    title: str | None = Form(None),
    quantity: int | None = Form(None),
    price: int | None = Form(None),
    discount: int | None = Form(None),
    product_type: ProductsType | None = Form(None),
    sub_category_id: int | None = Form(None),
    recommended: bool | None = Form(None),
    images: list[UploadFile] | None = File(None),
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return products_service.patch_products_service(
        db=db,
        products_id=products_id,
        title=title,
        quantity=quantity,
        price=price,
        discount=discount,
        product_type=product_type,
        sub_category_id=sub_category_id,
        recommended=recommended,
        images=images,
    )


@products_route.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_products(
    id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    return products_service.delete_products_services(db=db, id=id)
