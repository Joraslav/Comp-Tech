from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from app.settings import DATABASE_URL, DEBUG

engine = create_async_engine(DATABASE_URL, echo=bool(DEBUG), future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_db():
    # with engine.begin() as conn:
    #     conn.run_sync(SQLModel.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_async(SQLModel.metadata.create_all)


# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
