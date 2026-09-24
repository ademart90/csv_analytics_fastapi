from fastapi import APIRouter, BackgroundTasks, HTTPException
from src.models.summary_model import SummaryRequest
from src.controllers.summary_controller import start_summary_job, get_job_result
import os
import logging

router = APIRouter()

@router.post("/summary")
async def request_summary(request: SummaryRequest, background_tasks: BackgroundTasks):
    if not os.path.exists(request.file_path):
        logging.warning(f"file not found")
        raise HTTPException(status_code=404, detail="file not found")
    logging.info(f"background task for {request.file_path} running..")
    return await start_summary_job(request.file_path, background_tasks)

@router.get("/summary/{job_id}")
async def get_summary(job_id: str):
    logging.info(f"basic summary for {job_id}")
    return get_job_result(job_id)

    
