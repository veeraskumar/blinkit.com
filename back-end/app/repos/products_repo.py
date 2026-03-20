from sqlalchemy import or_
from sqlalchemy.orm import Session, joinedload

from app.models.product_model import Product
from app.models.subcategory_model import SubCategory


def create_products(db: Session, data: Product):
    db.add(data)
    db.commit()
    db.refresh(data)

    return data


def get_products(db: Session):
    return db.query(Product).order_by(Product.sub_category_id).all()


def get_products_by_category_id(db: Session, sub_categories_id: int):
    return db.query(Product).filter(Product.sub_category_id == sub_categories_id).all()


def get_product_id(db: Session, products_id: int):
    return db.query(Product).filter(Product.products_id == products_id).first()


def get_product_full(db: Session, product_id: int):
    return (
        db.query(Product)
        .options(joinedload(Product.subcategory).joinedload(SubCategory.category))
        .filter(Product.products_id == product_id)
        .first()
    )


def search_products(db: Session, query: str):
    return (
        db.query(Product)
        .join(SubCategory)
        .filter(
            or_(
                Product.title.ilike(f"%{query}%"),
                SubCategory.sub_categories_title.ilike(f"%{query}%"),
            )
        )
        .all()
    )


def update_product(db: Session, data: Product):
    db.commit()
    db.refresh(data)
    return data


def delete_product(db: Session, data: Product):
    db.delete(data)
    db.commit()
