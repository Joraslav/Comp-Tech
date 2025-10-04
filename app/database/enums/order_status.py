from enum import StrEnum


class OrderStatus(StrEnum):
    DRAFT = "draft"
    NEED_PAYMENT = "need_payment"
    PAYMENT_CONFIRMED = "payment_confirmed"
    CANCELED = "canceled"
    COMPLETED = "completed"
