import asyncio
from aiogram import Bot, Dispatcher
from app.config import BOT_TOKEN
from app.middleware import RequireTimezoneMiddleware
from app.handlers import start, analytics

async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.message.middleware(RequireTimezoneMiddleware())

    dp.include_router(start.router)
    dp.include_router(analytics.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
