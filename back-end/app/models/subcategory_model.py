from sqlalchemy import String, Integer, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database.db import Base


class SubCategory(Base):
    __tablename__ = "subcategories"

    sub_categories_id = Column(Integer, primary_key=True, autoincrement=True)
    sub_categories_title = Column(String, nullable=False, index=True)
    sub_categories_image = Column(String, nullable=False)
    sub_categories_recommended = Column(Boolean, nullable=False)

    categories_id = Column(
        Integer, ForeignKey("categories.categories_id"), nullable=False, index=True
    )

    category = relationship("Category", back_populates="subcategorys", lazy="joined")
    products = relationship("Product", back_populates="subcategory", lazy="selectin")
