import logging
from app.demos import product

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting application")
    product.run()
