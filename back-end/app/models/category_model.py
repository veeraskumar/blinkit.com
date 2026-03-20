from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from app.database.db import Base


class Category(Base):
    __tablename__ = "categories"

    categories_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    image = Column(String, nullable=True)
    recommended = Column(Boolean, nullable=True)

    subcategorys = relationship(
        "SubCategory", back_populates="category", lazy="selectin"
    )
