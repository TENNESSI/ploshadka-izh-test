from aiogram import Router, types
from aiogram.filters import Command
from keyboards.client import main_kb as start_client_kb

router = Router()

@router.message(Command("start"))
async def start(message: types.Message, is_admin: bool):
    if not is_admin:
        await message.answer(
            "Добро пожаловать в барбершоп!",
            reply_markup=start_client_kb()
        )

@router.message(lambda message: message.text == "📌 Записаться")
async def book_service(message: types.Message):
    await message.answer("Выберите мастера:")