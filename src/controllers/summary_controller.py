from src.services.summary_service import create_job_id, summary_job
from src.storage.job_storage import job_result
async def start_summary_job(file_path: str, background_tasks):
    job_id = create_job_id(file_path)
    background_tasks.add_task(summary_job, file_path, job_id)
    return {"job_id":job_id, "status":f"{job_id} running..."}

def get_job_result(job_id: str):
    result = job_result.get(job_id)
    if not result:
        return{"error": "mising result"}
    return result
            
            
