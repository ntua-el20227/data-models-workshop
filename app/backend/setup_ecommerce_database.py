import logging
from config import config
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
engine = create_engine(url=config.database.dsn)

sql_script_path = "app/backend/sql_scripts/init_ecommerce_db.sql"

with open(f"{sql_script_path}") as f:
    setup_database_query: str = "".join(f.readlines())
    engine.execute(setup_database_query)

print("--------------------")
logging.info("E-commerce database tables created successfully")
print("--------------------")
