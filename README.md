A csv-analytics application that accepts and processes csv files through fast-api endpoints

## Features
1. Fast asynchronous csv uploads using fastapi's 'UploadFile'
2. Automated data profiling, instantly returning summaries(row counts, missing values, column data types and descriptive statistics)
3. Filtering and aggregation - Query parametersallow filtering, grouping, and sorting data through API.
4. JSON responses - Outputs ready-to-use JSON structures.
5. Interactive docs

## Tech Stack
-- Framework: FastAPI
-- Data Processing: Polars
-- ASGI Server: Uvicorn

## Prerequisites and installation

Install the required dependencies:
''' bash
pip install fastapi uvicorn polars
'''

## Running the API
start the local development server using uvicorn:
'''bash
uvicorn src.main:app --reload
'''
The API will be live at "http://127.0.0.1:8000"

## Core Endpoints
Examples: 
Method -- Endpoint -- Description
'POST' -- '/upload' -- 'upload a .csv file'
'GET'  -- '/schema' -- 'Returns column names, column types, datatypes'

### Sample Response ('POST /upload')
'''json
{
     "message":"csv uploaded succesfully",
     "dataset_id":metadata.dataset_id,
     "filename":metadata.filename
}
'''

## Contribution 
You are free to fork this project, open issues, or submit pull requests to expand the capabilities of the analytics
