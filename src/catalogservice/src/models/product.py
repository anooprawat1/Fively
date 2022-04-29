from datetime import datetime
import sqlalchemy as sa
from src.database.database import Base
from sqlalchemy.dialects import postgresql
from uuid import uuid4
import enum


class Gender(enum.Enum):
    male = "male"
    female = "female"
    unisex = "unisex"


class Product(Base):
    __tablename__ = "product"

    id = sa.Column(postgresql.UUID(as_uuid=True),
                   primary_key=True, default=uuid4())
    handle = sa.Column(
        sa.VARCHAR, unique=True, doc="Unique handle of the product")
    name = sa.Column(sa.String(256), nullable=False, doc="Name of the product")

    description = sa.Column(sa.VARCHAR, doc="Description of the product")
    gender = sa.Column(sa.Enum(Gender), nullable=False,
                       doc="Product related to which gender", index=True)
    image_url = sa.Column(sa.VARCHAR, doc="Main image of the product")
    date_added = sa.Column(sa.DateTime(timezone=False),
                           doc="Date when the product is added", default=datetime.now, nullable=False)
    date_updated = sa.Column(sa.DateTime(timezone=False),
                             doc="Date when the product is update", default=datetime.now, nullable=False, onupdate=datetime.now)
    category = sa.Column(sa.Integer, sa.ForeignKey(
        "product_categories.id"), nullable=False)
