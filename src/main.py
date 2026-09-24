from fastapi import FastAPI
from src.routers import upload_router, schema_router, query_router, summary_router
from src.utils.logger import logger_setup
from src.database.database import create_tables

app = FastAPI(docs_url="/docs")

@app.on_event("startup")
async def startup():
    await create_tables()


logger_setup()

app.include_router(upload_router.router, tags=["Upload File"])
app.include_router(schema_router.router, tags=["Inspect schema"])
app.include_router(query_router.router, tags=["Query columns"])
app.include_router(summary_router.router, tags=["Descriptive statistics summary"])
