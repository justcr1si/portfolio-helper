from typing import Optional

from sqlalchemy import select

from database.connector import async_session
from database.models import User


async def get_user(telegram_id: int) -> Optional[User]:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_id))
        return result.scalar_one_or_none()


async def create_user(telegram_id: int, first_name: str, username: Optional[str] = None,
                      last_name: Optional[str] = None) -> User:
    async with async_session() as session:
        user = User(
            telegram_id=telegram_id,
            first_name=first_name,
            username=username,
            last_name=last_name
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
