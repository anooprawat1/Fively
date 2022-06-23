
from sqlalchemy.orm import Session
from src.models.product import Product
from src.database.database import get_db


class CrudProducts:

    def session(self) -> Session:
        return get_db()

    def add_product(self, handle: str, name: str, description: str, gender: str, image_url: str, category_id: int):
        if not self.__is_product_exist(handle):
            product = Product(handle=handle, name=name,
                              description=description, gender=gender, image_url=image_url, category=category_id)
            self.session().add(product)
            self.session().commit()

        return self.get_product_id_from_handle(handle)

    def __is_product_exist(self, handle):
        return self.session().query(Product).filter(Product.handle == handle).first() is not None

    def get_product_id_from_handle(self, handle: str):
        product = self.session().query(Product).filter(
            Product.handle == handle).first()
        if product is not None:
            return product.id
        else:
            return None


crud_products = CrudProducts()
