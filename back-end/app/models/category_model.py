from sqlalchemy import Column, String, Integer, Boolean, Sequence
from sqlalchemy.orm import relationship
from app.database.db import Base

categories_id_seq = Sequence("categories_id_seq", start=1000)


class Category(Base):
    __tablename__ = "categories"

    categories_id = Column(
        Integer,
        categories_id_seq,
        primary_key=True,
        server_default=categories_id_seq.next_value(),
    )
    title = Column(String, nullable=False, index=True)
    image = Column(String, nullable=True)
    recommended = Column(Boolean, nullable=True)

    subcategorys = relationship(
        "SubCategory", back_populates="category", lazy="selectin"
    )
