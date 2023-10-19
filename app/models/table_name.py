from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import SQLModel


class TableNameModel(SQLModel):
    __tablename__ = "table_name"
    __table_args__ = {"schema": "myapi"}

    column_name_1: Mapped[int] = mapped_column("column_name_1", primary_key=True)
    column_name_2: Mapped[str] = mapped_column("column_name_2")
    column_name_3: Mapped[float] = mapped_column("column_name_3")
