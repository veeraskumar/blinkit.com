from fastapi import UploadFile, HTTPException, status
from sqlalchemy.orm import Session

from app.core.conf import settings
from app.models.subcategory_model import SubCategory
from app.repos import sub_categories_repo
from app.schemas.sub_categories_schema import SubCategoriesRequest
from app.utils.image_handler import save_img_files, delete_image
from app.utils.title import clean_title

LOCATION = "subcategories"
SIZE = settings.max_size


def create_categories_service(
    sub_categories_title: str,
    categories_id: int,
    sub_categories_recommended: bool,
    sub_categories_image: UploadFile,
    db: Session,
):

    category = SubCategoriesRequest(
        sub_categories_title=clean_title(sub_categories_title),
        categories_id=categories_id,
        sub_categories_recommended=sub_categories_recommended,
    )

    filenames = save_img_files(file=sub_categories_image, location=LOCATION, size=SIZE)
    data = SubCategory(**category.model_dump(), sub_categories_image=filenames)
    return sub_categories_repo.create_categories(data=data, db=db)


def get_categories_service(db: Session):
    return sub_categories_repo.get_categories(db=db)


def get_subcategory_by_id_service(db: Session, sub_categories_id: int):
    data = sub_categories_repo.get_subcategory_full(db=db, sub_id=sub_categories_id)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="SubCategory not found"
        )
    return data


def patch_categories_service(
    db: Session,
    sub_categories_id: int,
    sub_categories_title: str | None,
    categories_id: int | None,
    sub_categories_recommended: bool | None,
    sub_categories_image: UploadFile | None,
):
    data = sub_categories_repo.get_categories_id(
        db=db, sub_categories_id=sub_categories_id
    )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="category is not Found"
        )

    if sub_categories_title is not None:
        data.sub_categories_title = clean_title(sub_categories_title)  # type: ignore

    if categories_id is not None:
        data.categories_id = categories_id  # type: ignore

    if sub_categories_recommended is not None:
        data.sub_categories_recommended = sub_categories_recommended  # type: ignore

    if sub_categories_image is not None:
        new_filename = save_img_files(
            file=sub_categories_image, location=LOCATION, size=SIZE
        )
        delete_image(image_url=data.sub_categories_image)  # type: ignore
        data.sub_categories_image = new_filename  # type: ignore

    return sub_categories_repo.update_categories(db=db, data=data)


def delete_categories_service(db: Session, sub_categories_id: int):

    data = sub_categories_repo.get_categories_id(
        sub_categories_id=sub_categories_id, db=db
    )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Category not found"
        )

    delete_image(image_url=data.sub_categories_image)  # type: ignore
    sub_categories_repo.delete_categories(db=db, data=data)
