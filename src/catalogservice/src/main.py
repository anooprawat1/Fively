from .models.product import Product
from .models.product_categories import ProductCategories
from .models.options import Options
from .models.options_value import OptionValue
from .models.product_sku import ProductSKU
from .models.sku_values import SKUValues
from fastapi import FastAPI
from .api.catalog_upload import router
from .database.database import engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router, prefix='/v1')
