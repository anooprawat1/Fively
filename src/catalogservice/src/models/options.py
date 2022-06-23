from enum import unique
import sqlalchemy as sa
from .product import Product
from src.database.database import Base
from sqlalchemy.dialects import postgresql
from uuid import uuid4


class Options(Base):
    __tablename__ = "options"

    id = sa.Column(postgresql.UUID(as_uuid=True),
                   primary_key=True, unique=True, default=uuid4(), doc="Option id of the option")
    name = sa.Column(sa.VARCHAR, nullable=False, unique=True,
                     doc="Name of the option like size, color")
    product_id = sa.Column(postgresql.UUID(as_uuid=True),
                           sa.ForeignKey("product.id"), primary_key=True)
