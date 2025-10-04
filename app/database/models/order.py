import uuid
from sqlmodel import Field, SQLModel

from app.database.enums.order_status import OrderStatus


class Order(SQLModel, table=True):
    order_id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.user_id", nullable=False, index=True)
    advert_id: uuid.UUID = Field(
        foreign_key="advert.advert_id", nullable=False, index=True
    )
    booking_id: uuid.UUID = Field(
        foreign_key="booking.booking_id", nullable=False, index=True
    )
    status: OrderStatus = Field(default_factory=lambda: OrderStatus.DRAFT, index=True)
