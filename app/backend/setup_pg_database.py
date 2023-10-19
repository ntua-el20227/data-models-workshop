import logging

from config import config
from sqlalchemy import create_engine, text

engine = create_engine(url=config.database.dsn)


sql_script_path = "app/backend/sql_scripts/setup_pg_db.sql"

# Read SQL statements from the file
with open(sql_script_path, "r") as sql_file:
    sql_statements = sql_file.read()

# Split the SQL statements into individual statements
statements = sql_statements.split(";")

# Execute each SQL statement
with engine.connect() as connection:
    for statement in statements:
        if statement.strip():  # Skip empty statements
            connection.execute(text(statement))

logging.info("PG database created successfully")
