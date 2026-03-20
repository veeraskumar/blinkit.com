from sqlalchemy import Column, String, Boolean, Integer, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base


class Product(Base):
    __tablename__ = "products"

    products_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    discount = Column(Integer, default=0)
    product_type = Column(String, nullable=False)
    images = Column(JSON, nullable=False, default=list)
    recommended = Column(Boolean, default=False)

    sub_category_id = Column(
        Integer,
        ForeignKey("subcategories.sub_categories_id"),
        nullable=False,
        index=True,
    )

    subcategory = relationship("SubCategory", back_populates="products", lazy="joined")
