from sqlalchemy.orm import Session
from typing import List
from ..repositories.category_repository import CategoryRepository
from ..schemas.category import CategoryCreate, CategoryResponce
from fastapi import HTTPException, status

class CategoryService:
    def __init__(self, db: Session):
        self.repository = CategoryRepository(db)

    def get_all_categories(self) -> List[CategoryResponce]:
        categories = self.repository.get_all()
        return [CategoryResponce.model_validate(cat) for cat in categories]
    
    def get_category_by_id(self, category_id: int) -> CategoryResponce:
        category = self.repository.get_by_id(category_id)
        if not category:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Category with id {category_id} not found"
            )
        return CategoryResponce.model_validate(category)
    
    def create_category(self, category_data: CategoryCreate) -> CategoryResponce:
        category = self.repository.create(category_data)
        return CategoryResponce.model_validate(category)
    