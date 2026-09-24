import polars as pl 
from uuid import uuid4
from src.storage.job_storage import job_result

async def summary_job(file_path: str, job_id: str):
    df = pl.read_csv(file_path)

    basic_stats = df.describe().to_dicts()
    count_row = {"row_count":df.height}
    count_column = {"column_count":df.width}
    missing_values  = df.null_count().to_dicts()

    final_result = {
       "job_id": job_id,
       "status": "completed",
       "This is your basic summary ":{
          "stats":basic_stats,
          "columns_number":count_column,
          "rows_number":count_row,
          "missing_values":missing_values
        
       }
    }

    job_result[job_id] = final_result

def create_job_id(file_path: str) -> str:
   job_id = str(uuid4())
   return job_id