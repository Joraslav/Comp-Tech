import uuid

from pydantic import BaseModel

from app.database.models.city import City as DBCity


class BaseCiry(BaseModel):
    name: str


class CreateCity(BaseCiry):
    pass


class UpdateCity(BaseCiry):
    pass


class City(BaseCiry):
    city_id: uuid.UUID

    @staticmethod
    def from_orm(city: DBCity) -> "City":
        return City.model_validate(city.model_dump())
