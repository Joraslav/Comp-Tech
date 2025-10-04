import uuid
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, HTTPException

from app.database.db import get_session
from app.schemas.city import CreateCity, City, UpdateCity
from app.database.repository.city import get_cities as db_get_cities
from app.database.repository.city import get_city as db_get_city
from app.database.repository.city import add_city as db_add_city
from app.database.repository.city import update_city as db_update_city

api_router = APIRouter(prefix="/admin", tags=["AdminAPI"])


@api_router.post("/city")
async def add_city(
    city: CreateCity, session: AsyncSession = Depends(get_session)
) -> City:
    return City.from_orm(await db_add_city(session=session, city=city))


@api_router.get("/city")
async def get_cities(session: AsyncSession = Depends(get_session)) -> list[City]:
    return [City.from_orm(city=city) for city in await db_get_cities(session=session)]


@api_router.get("/city/{city_id}")
async def get_city(
    city_id: uuid.UUID, session: AsyncSession = Depends(get_session)
) -> City:
    city = await db_get_city(city_id=city_id, session=session)
    if not city:
        raise HTTPException(status_code=404, detail="City not found")
    return City.from_orm(city=city)


@api_router.put("/city/{city_id}")
async def update_city(
    city_id: uuid.UUID, city: UpdateCity, session: AsyncSession = Depends(get_session)
) -> City:
    update_city = await db_update_city(city_id=city_id, city=city, session=session)
    if not update_city:
        raise HTTPException(status_code=404, detail="City not found")
    return City.from_orm(city=update_city)
