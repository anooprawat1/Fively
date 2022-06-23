from tkinter import S
from src.models.sku_values import SKUValues
from src.database.database import get_db
from sqlalchemy.orm import Session


class CrudSkuValues:

    def session(self) -> Session:
        return get_db()

    def add_sku_values(self, product_id, option_id, option_value_id, sku_id):
        if not self.is_sku_value_exist(product_id, option_id, option_value_id, sku_id):
            sku_values = SKUValues(
                product_id, option_id, option_value_id, sku_id)
            self.session().add(sku_values)
            self.session().commit()

    def is_sku_value_exist(self, product_id, option_id, option_value_id, sku_id) -> bool:
        return self.session().query(SKUValues).filter(SKUValues.sku_id == sku_id, SKUValues.product_id == product_id, SKUValues.option_id == option_id, SKUValues.option_value_id == option_value_id).first() is not None


crud_sku_values = CrudSkuValues()
