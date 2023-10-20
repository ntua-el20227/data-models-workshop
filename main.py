# app/main.py
import logging
from app.backend.session import create_session
from app.services.product import ProductService

def product_service_demo():
    with create_session() as session:
        product_service = ProductService(session)
        fetched_product = product_service.get_product(1)  # let's assume product_id 1 exists
        logging.info(f"Retrieved product: {fetched_product}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting application")
    product_service_demo()
