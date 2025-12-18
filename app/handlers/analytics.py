from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def analytics_stub(message: Message, user_timezone: str):
    await message.answer(f"Ваша таймзона: {user_timezone}")
