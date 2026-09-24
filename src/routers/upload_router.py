from fastapi import FastAPI, UploadFile, HTTPException, BackgroundTasks, Query, APIRouter, File, Depends
from src.services.csv_service import csv_upload
from src.database.database import get_db
import logging
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from src.database.repository import DatasetRepository 


router = APIRouter()

"""
This upload endpoint is an async function that:
1. accepts csv file with UploadFile's fastapi.
2. validates file name format with endswith().
3. generates logs for success and failed cases with logging.
4. Raises HTTPException error cases by status_code.
5. Sends the file object to file _upload async function and awaits the file_upload async function to return

    
"""

@router.post("/upload")
async def upload_csv(
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
    ):
    if not file.filename.endswith(".csv"): 
        logging.warning(f"{file.filename} - unsorported file format")
        raise HTTPException(status_code=400, detail ="upload csv file format")

    file_path = await csv_upload(file)

    repository = DatasetRepository(db)
    

    metadata = await repository.create_dataset(
        filename=file.filename,
        file_path=file_path
    )
    logging.info(f"{file.filename} uploaded")
    return {
        "message":"csv uploaded succesfully",
        "dataset_id":metadata.dataset_id,
        "filename":metadata.filename
    }

    