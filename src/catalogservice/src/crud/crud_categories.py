
from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.product_categories import ProductCategories
from src.database.database import get_db


class CrudCategories:

    def session(self) -> Session:
        return get_db()

    def add_categories(self, category: str) -> Optional[int]:
        data = category.split(">")
        self.__create_categories_from_data(data)
        return self.__get_category_id(data[len(data)-1].strip())

    def __create_categories_from_data(self, data: List[str]):
        for index, categor in enumerate(data):
            category = data[index].strip()
            if not self.__is_category_already_exists(category):
                if index == 0:
                    self.__add_categories(category)
                else:
                    parent_category_id = self.__get_category_id(
                        data[index-1].strip())
                    self.__add_categories(category, parent_category_id)

    def __add_categories(self, category: str, parent_category_id: Optional[int] = None):
        category_obj = ProductCategories(
            name=category, parent_category_id=parent_category_id)

        self.session().add(category_obj)
        self.session().commit()
        print("CATEGORIES Added to database --------",
              category, parent_category_id)

    def __is_category_already_exists(self, category: str) -> bool:
        return self.session().query(ProductCategories).filter(ProductCategories.name == category).first() is not None

    def __get_category_id(self, category: str) -> Optional[int]:
        selected_category = self.session().query(ProductCategories).filter(
            ProductCategories.name == category).first()
        if selected_category is not None:
            return selected_category.id
        else:
            return None

    def get_all_categories(self):
        return [u.__dict__ for u in self.session().query(ProductCategories).all()]


crud_categories = CrudCategories()
