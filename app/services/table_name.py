from sqlalchemy import select

from app.models.table_name import TableNameModel
from app.schemas.table_name import TableNameSchema
from app.services.base import BaseDataManager, BaseService


class TableNameService(BaseService):
    def get_table_name(self, column_name_1: int) -> TableNameSchema:
        """Get movie by ID."""

        return TableNameDataManager(self.session).get_table_name(column_name_1)


class TableNameDataManager(BaseDataManager):
    def get_table_name(self, column_name_1: int) -> TableNameSchema:
        stmt = select(TableNameModel).where(TableNameModel.column_name_1 == column_name_1)
        model = self.get_one(stmt)

        return TableNameSchema(**model.to_dict())
