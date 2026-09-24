import aiofiles
import os
from sqlalchemy.ext.asyncio import AsyncSession


FILE_DIR = "uploaded_csv"
os.makedirs(FILE_DIR, exist_ok=True)

async def csv_upload(file):
    file_path = os.path.join(FILE_DIR, file.filename)

    async with aiofiles.open(file_path, 'wb') as f:
        while chunk := await file.read(1024):
            await f.write(chunk)


    return str(file_path)

 
        