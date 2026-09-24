from sqlalchemy import select 
from sqlalchemy.ext.asyncio import AsyncSession

from .models import DatasetDB

class DatasetRepository:

    def __init__(self, db: AsyncSession):
          self.db = db

    async def create_dataset(
            self,
            filename: str,
            file_path: str,
            rows: int | None = None,
            columns: int | None = None
    ):
        dataset = DatasetDB(
            filename = filename,
            file_path = file_path,
            rows = rows,
            columns = columns
        )

        self.db.add(dataset)
        await self.db.commit()
        await self.db.refresh(dataset)

        return dataset

    async def  get_dataset(
            self,
            dataset_id: int
        ):
           result = await self.db.execute(
                select(DatasetDB).where(
                     DatasetDB.dataset_id==dataset_id
                )
           )

           return result.scalar_one_or_none()

    async def get_all_datasets(
              self,
              
        ):
            result = await self.db.execute(
                  select(DatasetDB)
            )

            return result.scalars().all()

    async def delete_dataset(
                self,
                dataset_id: int
    ):
          dataset = await self.get_dataset(self.db, dataset_id)

          if dataset is None:
                return False 

          await self.db.delete(dataset)
          await self.db.commit()

          return True
    