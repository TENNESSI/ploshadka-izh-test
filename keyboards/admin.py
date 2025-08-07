from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👨‍💼 Управление мастерами")],
            [KeyboardButton(text="📊 Статистика")]
        ],
        resize_keyboard=True
    )