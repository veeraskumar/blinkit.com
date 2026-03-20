from sqlalchemy.orm import Session, joinedload

from app.models.subcategory_model import SubCategory


def create_categories(data: SubCategory, db: Session):
    db.add(data)
    db.commit()
    db.refresh(data)
    return data


def get_categories(db: Session):
    return db.query(SubCategory).order_by(SubCategory.categories_id).all()


def get_categories_id(sub_categories_id: int, db: Session):
    return (
        db.query(SubCategory)
        .filter(SubCategory.sub_categories_id == sub_categories_id)
        .first()
    )


def get_subcategory_full(db: Session, sub_id: int):
    return (
        db.query(SubCategory)
        .options(joinedload(SubCategory.category), joinedload(SubCategory.products))
        .filter(SubCategory.sub_categories_id == sub_id)
        .first()
    )


def update_categories(db: Session, data: SubCategory):
    db.commit()
    db.refresh(data)
    return data


def delete_categories(db: Session, data: SubCategory):
    db.delete(data)
    db.commit()
