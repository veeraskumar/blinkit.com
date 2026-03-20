from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from app.core.conf import settings
from app.models.product_model import Product
from app.repos.sub_categories_repo import get_categories_id
from app.repos import products_repo
from app.schemas.products_schema import ProductsType, ProductsRequest
from app.utils.image_handler import save_img_files, delete_image
from app.utils.title import clean_title

LOCATION = "products"
SIZE = settings.max_size


def create_products_services(
    title: str,
    quantity: int,
    price: int,
    discount: int,
    product_type: ProductsType,
    sub_category_id: int,
    recommended: bool,
    images: list[UploadFile],
    db: Session,
):
    product = ProductsRequest(
        title=clean_title(title),
        quantity=quantity,
        price=price,
        discount=discount,  # ✅ Fixed: store percentage as-is (e.g. 10 for 10%)
        product_type=product_type,
        sub_category_id=sub_category_id,
        recommended=recommended,
    )

    filenames: list[str] = [
        save_img_files(img, location=LOCATION, size=SIZE) for img in images
    ]

    data = Product(**product.model_dump(), images=filenames)
    return products_repo.create_products(db=db, data=data)


def get_all_products_service(db: Session):
    return products_repo.get_products(db=db)


def get_products_by_category_service(db: Session, sub_categories_id: int):
    data = get_categories_id(sub_categories_id=sub_categories_id, db=db)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="SubCategory not found"
        )
    return products_repo.get_products_by_category_id(
        sub_categories_id=sub_categories_id, db=db
    )


def get_prd_by_id(db: Session, id: int):
    data = products_repo.get_product_full(db=db, product_id=id)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return data


def search_products_service(db: Session, q: str):
    return products_repo.search_products(db=db, query=q.strip())


def patch_products_service(
    db: Session,
    products_id: int,
    title: str | None = None,
    quantity: int | None = None,
    price: int | None = None,
    discount: int | None = None,
    product_type: ProductsType | None = None,
    sub_category_id: int | None = None,
    recommended: bool | None = None,
    images: list[UploadFile] | None = None,
):
    data = products_repo.get_product_id(db=db, products_id=products_id)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    if title is not None:
        data.title = clean_title(title)  # type: ignore
    if quantity is not None:
        data.quantity = quantity  # type: ignore
    if price is not None:
        data.price = price  # type: ignore
    if discount is not None:
        data.discount = discount  # type: ignore  ✅ Fixed: just the percentage
    if product_type is not None:
        data.product_type = product_type  # type: ignore
    if sub_category_id is not None:
        data.sub_category_id = sub_category_id  # type: ignore
    if recommended is not None:
        data.recommended = recommended  # type: ignore

    if images:
        if data.images:  # type: ignore
            for img in data.images:  # type: ignore
                delete_image(image_url=img)  # type: ignore
        data.images = [  # type: ignore
            save_img_files(file=img, location=LOCATION, size=SIZE) for img in images
        ]

    return products_repo.update_product(db=db, data=data)


def delete_products_services(db: Session, id: int):
    data = products_repo.get_product_id(db=db, products_id=id)
    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    if data.images:  # type: ignore
        for img in data.images:  # type: ignore
            delete_image(image_url=img)  # type: ignore
    products_repo.delete_product(db=db, data=data)
