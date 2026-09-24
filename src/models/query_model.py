from pydantic import BaseModel
from typing import Any, Optional
from src.services.query_services import Operator

class Filter(BaseModel):
    column: str
    operator: Operator
    value: Any

class QueryRequest(BaseModel):
    file_path: str
    filters: list[Filter] = []
    
    