import sqlalchemy as sa
from src.database.database import Base


class ProductCategories(Base):
    __tablename__ = "product_categories"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String,
                     doc="Name of the Product category")
    parent_category_id = sa.Column(sa.Integer, doc="Parent id of the categroy")
