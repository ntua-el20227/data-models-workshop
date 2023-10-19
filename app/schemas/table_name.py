from pydantic import BaseModel


class TableNameSchema(BaseModel):
    column_name_1: int
    column_name_2: str
    column_name_3: float
