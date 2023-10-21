from datetime import date

from sqlalchemy import select

from app.models.users import Users
from app.schemas.users import UserCreateSchema, UsersSchema
from app.services.base import BaseDataManager, BaseService


class UsersService(BaseService):
    def get_all_users(self) -> list[UsersSchema]:
        """Retrieve all users from the database."""
        return UsersDataManager(self.session).get_all_users()

    def add_user(self, user_data: UserCreateSchema) -> UsersSchema:
        """Add a new user to the database."""
        user = Users(**user_data.dict(), registration_date=date.today())
        added_user = UsersDataManager(self.session).add_one(user)
        return UsersSchema.from_orm(added_user)


class UsersDataManager(BaseDataManager):
    def get_all_users(self) -> list[UsersSchema]:
        stmt = select(Users)
        models = self.get_all(stmt)
        return [UsersSchema.from_orm(model) for model in models]
