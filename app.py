from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config.settings import config
import handlers.client
import handlers.admin
import asyncio
import logging

# Настройка логгирования
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(handlers.admin.router)
    dp.include_router(handlers.client.router)

    # Базовая команда для проверки
    @dp.message(Command("start"))
    async def start(message: types.Message):
        await message.answer("Бот запущен и работает!")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())