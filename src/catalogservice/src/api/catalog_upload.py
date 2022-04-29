from fastapi import APIRouter, UploadFile, File
import os
from tempfile import NamedTemporaryFile
from csv import DictReader
from src.crud.crud_categories import crud_categories
router = APIRouter()


@router.post("/upload_catalog")
async def uploadCatalog(csv_file: UploadFile = File(...)):
    contents = await csv_file.read()
    file_copy = NamedTemporaryFile(delete=False)
    f = None
    try:
        with file_copy as f:
            f.write(contents)  # type: ignore
            f = open(file_copy.name)
            reader = DictReader(f)
            allCategories = list(set([row["Google Shopping / Google Product Category"]
                                 for row in reader if row["Google Shopping / Google Product Category"] != '']))
            crud_categories.add_all_categories(allCategories)

    finally:
        if f is not None:
            f.close()
        os.unlink(file_copy.name)

    return {"filename": csv_file.filename}


@router.get("/get_catalog")
async def getCatalog():
    return {"categories": crud_categories.get_all_categories()}
