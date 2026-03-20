from pydantic import BaseModel, Field

from app.schemas.sub_categories_schema import SubCategoriesResponse


class CategoriesBase(BaseModel):
    title: str = Field(min_length=3, pattern=r'^[a-zA-Z0-9@&()+=*"?\.~\'!#% ]+$')
    recommended: bool


class CategoriesRequest(CategoriesBase):
    pass


class CategoriesResponse(CategoriesBase):
    categories_id: int
    image: str
    subcategorys: list[SubCategoriesResponse] = []

    class Config:
        from_attributes = True
