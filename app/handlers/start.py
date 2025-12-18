from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboards import timezone_kb
from app.repo.users import upsert_user

router = Router()

@router.message(F.text == "/start")
async def start_cmd(message: Message):
    await message.answer(
        "Выберите таймзону для расчётов:",
        reply_markup=timezone_kb(),
    )

@router.callback_query(F.data.startswith("tz:"))
async def set_timezone(cb: CallbackQuery):
    tz = cb.data.split(":", 1)[1]
    await upsert_user(str(cb.from_user.id), tz)
    await cb.message.edit_text(
        f"Таймзона сохранена: {tz}"
    )
    await cb.answer()
