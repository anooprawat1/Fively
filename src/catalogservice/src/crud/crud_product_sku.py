from src.models.product_sku import ProductSKU
from src.database.database import get_db
from sqlalchemy.orm import Session


class CrudProductSku:

    def session(self) -> Session:
        return get_db()

    def add_product_sku(self, sku: str, price: str, variant_barcode: str, inventory_count: str, product_id):
        if not self.is_sku_exist(sku):
            product_sku = ProductSKU(sku, price, variant_barcode,
                                     inventory_count, product_id)
            self.session().add(product_sku)
            self.session().commit()
        return self.get_product_sku_for_sku(sku)

    def is_sku_exist(self, sku: str) -> bool:
        return self.session().query(ProductSKU).filter(ProductSKU.sku == sku).first() is not None

    def get_product_sku_for_sku(self, sku: str):
        option = self.session().query(ProductSKU).filter(
            ProductSKU.sku == sku).first()
        if option is not None:
            return option.id
        else:
            return None


crud_product_sku = CrudProductSku()
