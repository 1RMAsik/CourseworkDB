import asyncio

from aiogram import Bot, Dispatcher
from handlers import different_types, handlers
from dotenv import load_dotenv
import os

load_dotenv()

Token = os.getenv("TOKEN")
async def main():
    bot = Bot(token=Token)
    dp = Dispatcher()

    dp.include_routers(handlers.router, different_types.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
