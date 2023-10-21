from typing import Any, List, Sequence

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import Executable


class SessionMixin:
    """Provides instance of database session."""

    def __init__(self, session: Session) -> None:
        self.session = session


class BaseService(SessionMixin):
    """Base class for application services."""


class BaseDataManager(SessionMixin):
    """Base data manager class responsible for operations over database."""

    def add_one(self, model: Any) -> None:
        """Adds one model to the database."""

        self.session.add(model)

    def add_all(self, models: Sequence[Any]) -> None:
        """Adds multiple models to the database."""

        self.session.add_all(models)

    def get_one(self, select_stmt: Executable) -> Any:
        """Returns one model from the database."""

        return self.session.scalar(select_stmt)

    def get_all(self, select_stmt: Executable) -> List[Any]:
        """Returns all models from the database."""

        return list(self.session.scalars(select_stmt).all())
