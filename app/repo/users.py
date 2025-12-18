from sqlalchemy import select
from app.db import SessionLocal
from app.models import User

async def get_user(telegram_id: str):
    async with SessionLocal() as session:
        res = await session.execute(
            select(User).where(User.telegram_id == telegram_id)
        )
        return res.scalar_one_or_none()

async def upsert_user(telegram_id: str, timezone: str):
    async with SessionLocal() as session:
        user = await session.get(User, telegram_id)
        if user:
            user.timezone = timezone
        else:
            user = User(telegram_id=telegram_id, timezone=timezone)
            session.add(user)
        await session.commit()
