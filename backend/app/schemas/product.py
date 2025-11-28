from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from .category import CategoryResponce


class ProductBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=200,
                    description="Product name")
    description: Optional[str] = Field(None,
                    description="Product description")
    price: float = Field(..., gt=0,
                    description="Product price(must be greater than 0)")
    category_id: int = Field(...,
                    description="Category ID")
    image_url: Optional[str] = Field(None,
                    description="Product image URL")
    
class ProductCreate(ProductBase):
    pass

class ProductResponce(BaseModel):
    id: int = Field(..., description="Unique product ID")
    name: str
    description: Optional[str]
    price: float
    category_id: int
    image_url: Optional[str]
    created_at: datetime
    category: CategoryResponce = Field(..., description="Product category details")

    class Config:
        form_attributes = True

class ProductListResponce(BaseModel):
    products: list[ProductResponce]
    total: int = Field(..., description="Total number of products")