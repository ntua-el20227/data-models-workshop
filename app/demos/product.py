import logging

from app.backend.session import create_session
from app.services.product import ProductService


def run():
    with create_session() as session:
        product_service = ProductService(session)
        fetched_product = product_service.get_product(1)  # let's assume product_id 1 exists
        logging.info(f"Retrieved product: {fetched_product}")
