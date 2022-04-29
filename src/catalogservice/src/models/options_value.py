from enum import unique
import sqlalchemy as sa
from .options import Options
from src.database.database import Base
from sqlalchemy.dialects import postgresql
from uuid import uuid4


class OptionValue(Base):
    __tablename__ = "option_value"

    id = sa.Column(postgresql.UUID(as_uuid=True),
                   primary_key=True, unique=True, default=uuid4(), doc="Value id of the option value")
    name = sa.Column(sa.VARCHAR, nullable=False,
                     doc="Name of the value for option like for size -- S, M")
    product_id = sa.Column(postgresql.UUID(as_uuid=True),
                           sa.ForeignKey("product.id"), primary_key=True)
    option_id = sa.Column(postgresql.UUID(as_uuid=True),
                          sa.ForeignKey("options.id"), primary_key=True)
