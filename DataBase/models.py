# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
# from sqlalchemy import BigInteger, String, Text, ForeignKey
#
# engine = create_async_engine(url='sqlite+aiosqlite:///conventer.sqlite3')
# async_session = async_sessionmaker(engine)
#
#
# class Base(AsyncAttrs, DeclarativeBase):
#     pass
#
# class User(Base):
#     __tablename__ = 'users'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     tg_id: Mapped[int] = mapped_column(BigInteger, unique=False)
#     name: Mapped[str] = mapped_column(String(50))
#     # favorites: Mapped[str | None]
#
# async def create_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#
# async def drop_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)