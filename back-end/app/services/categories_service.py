from fastapi import HTTPException, status, UploadFile
from sqlalchemy.orm import Session

from app.core.conf import settings
from app.models.category_model import Category
from app.repos import categories_repo
from app.schemas.categories_schema import CategoriesRequest
from app.utils.image_handler import save_img_files, delete_image
from app.utils.title import clean_title

CATEGORY = "categories"


def get_categories_services(db: Session):
    return categories_repo.get_categories(db=db)


def get_categories_id_services(category_id: int, db: Session):
    data = categories_repo.get_category_full(category_id=category_id, db=db)

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="categories not found"
        )

    return data


def create_categories_services(
    title: str, recommended: bool, image: UploadFile, db: Session
):
    data = CategoriesRequest(title=clean_title(title), recommended=recommended)
    img = save_img_files(file=image, location=CATEGORY, size=settings.max_size)
    category = Category(**data.model_dump(), image=img)
    return categories_repo.create_categories(data=category, db=db)


def patch_categories_services(
    categories_id: int,
    title: str | None,
    recommended: bool | None,
    image: UploadFile | None,
    db: Session,
):

    data = categories_repo.get_categories_id(id=categories_id, db=db)

    if data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="categories not found"
        )

    if title is not None:
        data.title = clean_title(title)  # pyright: ignore[reportAttributeAccessIssue]

    if recommended is not None:
        data.recommended = recommended  # pyright: ignore[reportAttributeAccessIssue]

    if image is not None:
        delete_image(image_url=data.image)  # pyright: ignore[reportArgumentType]
        img = save_img_files(file=image, location=CATEGORY, size=settings.max_size)
        data.image = img  # pyright: ignore[reportAttributeAccessIssue]

    return categories_repo.patch_categories(data=data, db=db)


def delete_categories_services(categories_id: int, db: Session):
    data = categories_repo.get_categories_id(id=categories_id, db=db)

    if data is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="")

    delete_image(image_url=data.image)  # type: ignore
    categories_repo.delete_categories(data=data, db=db)
