from pydantic import BaseModel, Field
from typing import Optional, List

class DatasetUploadMetadata(BaseModel):
    filename: str
    file_size_bytes:int
    detected_columns: List[str] = Field(default_factory=list)
    total_rows: Optional[int] = None