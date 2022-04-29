from enum import unique
import sqlalchemy as sa
from .product import Product
from src.database.database import Base
from sqlalchemy.dialects import postgresql
from uuid import uuid4


class ProductSKU(Base):
    __tablename__ = "product_SKU"

    id = sa.Column(postgresql.UUID(as_uuid=True),
                   primary_key=True, unique=True, default=uuid4(), doc="Individual id of the sku")
    sku = sa.Column(sa.VARCHAR, nullable=False,
                    doc="Product sku")
    price = sa.Column(sa.FLOAT, nullable=False, doc="Price of the Product sku")

    variant_barcode = sa.Column(sa.VARCHAR, nullable=False,
                                doc="Barcode of the variant")

    inventory_count = sa.Column(
        sa.Integer, nullable=False, default=0, doc="Total product available for the sku")

    product_id = sa.Column(postgresql.UUID(as_uuid=True),
                           sa.ForeignKey("product.id"), primary_key=True)
