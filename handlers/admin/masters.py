from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters.command import Command
from database.crud import add_master, get_session
from database.models import Master

router = Router()

@router.message(F.text == "➕ Добавить мастера")
async def add_master_handler(message: Message):
    db = get_session()
    new_master = add_master(db, name="Новый мастер")
    await message.answer(f"Мастер {new_master.name} добавлен!")

@router.message(Command("test"))
async def test_db(message: Message):
    db = get_session()
    new_master = add_master(db, name="Тестовый мастер")
    await message.answer(f"Добавлен мастер: {new_master.name}")