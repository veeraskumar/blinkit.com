from sqlalchemy import String, Integer, Column, Boolean, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from app.database.db import Base

sub_categories_id_seq = Sequence("sub_categories_id_seq", start=1000)


class SubCategory(Base):
    __tablename__ = "subcategories"

    sub_categories_id = Column(
        Integer,
        sub_categories_id_seq,
        primary_key=True,
        server_default=sub_categories_id_seq.next_value(),
    )
    sub_categories_title = Column(String, nullable=False, index=True)
    sub_categories_image = Column(String, nullable=False)
    sub_categories_recommended = Column(Boolean, nullable=False)

    categories_id = Column(
        Integer, ForeignKey("categories.categories_id"), nullable=False, index=True
    )

    category = relationship("Category", back_populates="subcategorys", lazy="joined")
    products = relationship("Product", back_populates="subcategory", lazy="selectin")
