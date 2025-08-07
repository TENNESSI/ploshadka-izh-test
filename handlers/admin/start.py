from aiogram import Router, types
from aiogram.filters import Command
from keyboards.admin import main_kb as start_admin_kb

router = Router()

@router.message(Command("start"))
async def start(message: types.Message, is_admin: bool):
    if is_admin:
        await message.answer(
            "Добро пожаловать в админ-панель",
            reply_markup=start_admin_kb()
        )