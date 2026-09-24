from fastapi import APIRouter, HTTPException
import polars as pl
import os
import logging

router = APIRouter()

@router.get("/schema")
async def get_schema(file_name: str):
    if not os.path.exists(file_name):
        logging.warning(f"file not found")
        raise HTTPException(status_code=404, detail="file not found")
    
    df = pl.read_csv(file_name, has_header = True)
    columns = df.columns
    row_count, column_count = df.shape
    datatype = {col: str(dtype) for col, dtype in zip(df.columns, df.dtypes)}
    logging.info(f"schema is loading...")
    return {
        "column_names":columns,
        "column_counts":column_count,
        "row_counts":row_count,
        "schema":datatype

    }
    

