from sqlmodel import SQLModel, Field

from app.database.enums.booking_status import BookingStatus


class Booking(SQLModel, table=True):
    booking_id: int = Field(primary_key=True)
    user_id: int = Field(foreign_key="user.user_id", nullable=False, index=True)
    advert_id: int = Field(foreign_key="advert.advert_id", nullable=False, index=True)
    status: BookingStatus = Field(
        default_factory=lambda: BookingStatus.PENDING, index=True
    )
    created_at: int
    updated_at: int
    not_before: int
    not_after: int
