from fastapi import APIRouter, HTTPException
from src.models.query_model import QueryRequest
import os
import polars as pl
import logging
from src.controllers.query_controller import OPERATORS

router = APIRouter()

@router.post("/query")
async def query(request: QueryRequest):
    if not os.path.exists(request.file_path):
        logging.warning(f"file not found")
        raise HTTPException(status_code=404, detail="file not found")
    
    df = pl.read_csv(request.file_path, has_header= True)

    
    

    for f in request.filters:
        filtered = df.filter(
            OPERATORS[f.operator.value](f.column, f.value)
        ).to_dicts()
        

    logging.info(f"query loading...")
    
    return{
        "filtered_count":f"there are {len(filtered)} rows",
        "filtered": filtered
    }