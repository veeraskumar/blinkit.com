from pydantic import BaseModel, Field
from enum import Enum

from app.schemas.products_schema import ProductsResponse


class SubCategoriesBase(BaseModel):
    sub_categories_title: str = Field(
        min_length=3, pattern=r'^[a-zA-Z0-9@&()+=*"?\.~\'!#% ]+$'
    )
    categories_id: int
    sub_categories_recommended: bool


class SubCategoriesRequest(SubCategoriesBase):
    pass


class SubCategoriesResponse(SubCategoriesBase):
    sub_categories_id: int
    sub_categories_image: str
    products: list[ProductsResponse] = []

    class Config:
        from_attributes = True
