from datetime import date

from pydantic import BaseModel


class PaymentSchema(BaseModel):
    payment_id: int
    order_id: int
    payment_method: str
    payment_date: date
    amount: float

    class Config:
        from_orm = True
        from_attributes = True
