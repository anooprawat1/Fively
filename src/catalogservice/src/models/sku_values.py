from .options import Options
import sqlalchemy as sa
from .product_sku import ProductSKU
from .options_value import OptionValue
from .product import Product
from src.database.database import Base
from sqlalchemy.dialects import postgresql
from uuid import uuid4


class SKUValues(Base):
    __tablename__ = "sku_values"

    product_id = sa.Column(postgresql.UUID(as_uuid=True),
                           sa.ForeignKey("product.id"), primary_key=True)
    option_id = sa.Column(postgresql.UUID(as_uuid=True),
                          sa.ForeignKey("options.id"), primary_key=True)
    option_value_id = sa.Column(postgresql.UUID(as_uuid=True),
                                sa.ForeignKey("option_value.id"), primary_key=True)
    sku_id = sa.Column(postgresql.UUID(as_uuid=True),
                       sa.ForeignKey("product_SKU.id"), primary_key=True)
