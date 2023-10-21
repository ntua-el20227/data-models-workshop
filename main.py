# Entry point for the application.
# Initializes logging and starts the [entity]demo, e.g. product, customer, etc.

import logging
from app.demos import product, users

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting application")

    logging.info("Starting users demo")
    users.run()