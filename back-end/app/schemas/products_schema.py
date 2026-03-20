from pydantic import BaseModel, Field
from enum import Enum


class ProductsType(str, Enum):
    LIQUID = "liquid"
    SOLID = "solid"
    PIECE = "piece"


class ProductsBase(BaseModel):
    title: str = Field(min_length=3, pattern=r'^[a-zA-Z0-9@&()+=*"?\.~\'!#% ]+$')
    quantity: int = Field(ge=1)
    price: int = Field(ge=0)
    discount: int = Field(
        default=0, ge=0, le=100, description="this will convert into percentage of sub"
    )
    product_type: ProductsType
    sub_category_id: int
    recommended: bool = Field(default=False)


class ProductsRequest(ProductsBase):
    pass


class ProductsResponse(ProductsBase):
    products_id: int
    images: list[str]

    class Config:
        from_attributes = True
