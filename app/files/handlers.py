import shutil
from pathlib import Path

from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post("/upload-file")
async def create_upload_file(file: UploadFile = File(...)):
    # Create the destination folder if it doesn't exist
    upload_folder = "./uploads"
    Path(upload_folder).mkdir(parents=True, exist_ok=True)

    # Save the file to the destination folder
    file_path = Path(upload_folder) / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "file_path": str(file_path)}
