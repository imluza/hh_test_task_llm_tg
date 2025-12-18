from aiogram import BaseMiddleware
from aiogram.types import Message
from app.repo.users import get_user

class RequireTimezoneMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        if not isinstance(event, Message):
            return await handler(event, data)

        if event.text == "/start":
            return await handler(event, data)

        user = await get_user(str(event.from_user.id))
        if not user:
            await event.answer("Сначала выберите таймзону")
            return

        data["user_timezone"] = user.timezone
        return await handler(event, data)
