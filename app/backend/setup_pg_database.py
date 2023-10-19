import logging

from config import config
from sqlalchemy import create_engine

engine = create_engine(url=config.database.dsn)


sql_script_path = "app/backend/sql_scripts/setup_pg_db.sql"

with open(f"{sql_script_path}") as f:
    setup_database_query: str = "".join(f.readlines())
    engine.execute(setup_database_query)

logging.info("PG database created successfully")
