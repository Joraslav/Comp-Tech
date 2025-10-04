import os
import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.city import CreateCity, UpdateCity, select
from app.database.models.city import City


async def get_cities(session: AsyncSession) -> list[City]:
    statement = select(City)
    return (await session.exec(statement)).all()


async def get_city(session: AsyncSession, city_id: uuid.UUID) -> City | None:
    return await session.get(City, city_id)


async def add_city(session: AsyncSession, city: CreateCity) -> City:
    new_city = City.model_validate(city.model_dump())
    session.add(new_city)
    await session.commit()
    return new_city


async def update_city(
    session: AsyncSession, city_id: uuid.UUID, city: UpdateCity
) -> City | None:
    db_city = await get_city(session, city_id)
    if db_city is None:
        return None
    db_city.name = city.name
    await session.commit()
    return db_city
