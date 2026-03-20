from sqlalchemy.orm import Session, joinedload

from app.models.category_model import Category
from app.models.subcategory_model import SubCategory


def get_categories(db: Session):
    return db.query(Category).order_by(Category.categories_id).all()


def get_categories_id(id: int, db: Session):
    return db.query(Category).filter(Category.categories_id == id).first()


def create_categories(data: Category, db: Session):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def get_category_full(category_id: int, db: Session):
    return (
        db.query(Category)
        .options(joinedload(Category.subcategorys).joinedload(SubCategory.products))
        .filter(Category.categories_id == category_id)
        .first()
    )


def patch_categories(data: Category, db: Session):
    db.commit()
    db.refresh(data)
    return data


def delete_categories(data: Category, db: Session):
    db.delete(data)
    db.commit()
