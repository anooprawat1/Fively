from fastapi import APIRouter, UploadFile, File
import os
from tempfile import NamedTemporaryFile
from csv import DictReader
from src.crud.crud_categories import crud_categories
from src.crud.crud_products import crud_products
from src.crud.crud_options import crud_options
from src.crud.crud_options_value import crud_options_value
from src.crud.crud_product_sku import crud_product_sku
from src.crud.crud_sku_values import crud_sku_values
router = APIRouter()


@router.post("/upload_catalog")
async def upload_catalog(csv_file: UploadFile = File(...)):
    last_option1_id = None
    last_option2_id = None
    last_option3_id = None
    contents = await csv_file.read()
    file_copy = NamedTemporaryFile(delete=False)
    f = None
    try:
        with file_copy as f:
            f.write(contents)  # type: ignore
            f = open(file_copy.name)
            reader = DictReader(f)
            all_categories = []
            all_handles = []
            all_options = []
            product_sku = []
            for row in reader:
                category = row["Google Shopping / Google Product Category"]
                handle = row["Handle"]
                name = row["Title"]
                description = row["Body (HTML)"]
                gender = row["Google Shopping / Gender"].strip()
                image_url = row["Image Src"]
                sku = row["Variant SKU"]
                price = row["Variant Price"]
                barcode = row["Variant Barcode"]
                inventory_count = row["Variant Inventory Qty"]

                category_id = crud_categories.add_categories(category)
                if category_id is None:
                    return
                product_id = crud_products.add_product(
                    handle, name, description, gender, image_url, category_id)
                optionName1 = row["Option1 Name"]
                optionName2 = row["Option2 Name"]
                optionName3 = row["Option3 Name"]
                optionValue1 = row["Option1 Value"]
                optionValue2 = row["Option2 Value"]
                optionValue3 = row["Option3 Value"]

                if optionName1 != '':
                    last_option1_id = crud_options.add_option(
                        optionName1, product_id)
                if optionName2 != '':
                    last_option2_id = crud_options.add_option(
                        optionName2, product_id)
                if optionName3 != '':
                    last_option3_id = crud_options.add_option(
                        optionName3, product_id)

                if optionValue1 != '':
                    option_id_1 = crud_options_value.add_option_option(
                        optionValue1, product_id, last_option1_id)
                if optionValue2 != '':
                    option_id_2 = crud_options_value.add_option_option(
                        optionValue2, product_id, last_option2_id)
                if optionValue3 != '':
                    option_id_3 = crud_options_value.add_option_option(
                        optionValue3, product_id, last_option3_id)
                product_sku = crud_product_sku.add_product_sku(
                    sku, price, barcode, inventory_count, product_id)
                # crud_sku_values.add_sku_values(product_id)

                print("Product id------------", product_id)
                break
                handle = row["Handle"]
                product_sku_dict = {"handle": handle, "variant_sku": row["Variant SKU"], "variant_price": row["Variant Price"],
                                    "variant_barcode": row["Variant Barcode"], "inventory_count": row["Variant Inventory Qty"]}
                product_sku.append(product_sku_dict)
                if category != '' and not category in all_categories:
                    all_categories.append(category)
                if handle != '':
                    all_handle_dict = {"handle": handle}
                    if not any(d['handle'] == handle for d in all_handles):
                        all_handle_dict["name"] = row["Title"]
                        all_handle_dict["description"] = row["Body (HTML)"]
                        all_handle_dict["gender"] = row["Google Shopping / Gender"]
                        all_handle_dict["image_url"] = row["Image Src"]
                        all_handle_dict["category"] = row["Google Shopping / Google Product Category"]
                        all_handles.append(all_handle_dict)

                        all_option_dict = {}
                        all_option_dict["handle"] = handle
                        options = []
                        option1 = row["Option1 Name"]
                        option2 = row["Option2 Name"]
                        option3 = row["Option3 Name"]
                        if option1 != '':
                            options.append(option1)
                        if option2 != '':
                            options.append(option2)
                        if option3 != '':
                            options.append(option3)
                        all_option_dict["option"] = options
                        all_options.append(all_option_dict)

            print("Handles----")

    finally:
        if f is not None:
            f.close()
        os.unlink(file_copy.name)

    return {"filename": csv_file.filename}


@ router.get("/get_catalog")
async def getCatalog():
    return {"categories": crud_categories.get_all_categories()}
