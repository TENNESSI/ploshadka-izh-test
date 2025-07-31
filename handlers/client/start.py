from aiogram import Router, types
from aiogram.filters import Command
from keyboards.client import main_kb

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать в барбершоп!",
        reply_markup=main_kb()
    )

@router.message(lambda message: message.text == "📌 Записаться")
async def book_service(message: types.Message):
    await message.answer("Выберите мастера:")