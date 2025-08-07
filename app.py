from aiogram import Bot, Dispatcher, types
from config.settings import config
from handlers import client, admin
from middlewares.admin import AdminMiddleware
import asyncio
import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры
    dp.message.middleware(AdminMiddleware())
    dp.include_routers(admin.router, client.router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())