import uuid
from sqlmodel import Field, SQLModel

from app.database.enums.advert_status import AdvertStatus


class Advert(SQLModel, table=True):
    advert_id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    description: str
    city_id: uuid.UUID = Field(foregin_key="city.city_id", nullable=False, index=True)
    address: str = Field(index=True)
    price: int
    contact: str
    author: uuid.UUID = Field(foregin_key="user.user_id", nullable=False, index=True)
    status: AdvertStatus = Field(default_factory=lambda: AdvertStatus.DRAFT, index=True)
    not_before: int
    not_after: int
