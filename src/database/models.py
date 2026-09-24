from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

class DatasetDB(Base):
    __tablename__ = "datasets"

    dataset_id: Mapped[int] = Column(Integer, primary_key = True, index=True, autoincrement=True)
    filename: Mapped[str] = mapped_column(String)
    file_path: Mapped[str] = mapped_column(String)
    rows: Mapped[int | None] = mapped_column(Integer, nullable=True)
    columns: Mapped[int | None] = mapped_column(Integer, nullable=True)

