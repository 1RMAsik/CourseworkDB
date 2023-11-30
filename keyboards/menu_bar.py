from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_menu_buttons() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🏪 Каталог")
    kb.button(text="🛒 Корзина")
    kb.button(text="🛠 Настройки")
    kb.button(text="🎧 Поддержка")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)
