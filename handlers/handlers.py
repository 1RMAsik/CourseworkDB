from aiogram import types
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F
from aiogram.filters import Command
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

load_dotenv()
db = os.getenv("DB")

from keyboards.menu_bar import get_menu_buttons
from models.models import Departments

router = Router()

engine = create_engine(db)
Session = sessionmaker(bind=engine)
session = Session()

@router.message(Command("start"))
async def cmd_start(message: Message):
    photo_url = "https://th.bing.com/th/id/OIG.Y8RoHD3mrWx1swKpoNnf?pid=ImgGn"
    await message.answer_photo(
        photo=photo_url,
        caption=f"👋 Приветствую, <b>{message.from_user.full_name}</b>! "
                f"И добро пожаловать в онлайн-универмаг <b>GreatStore</b>.\n"
                f"Здесь вы можете найти необходимы товары по оптимальным ценам!\n"
                f"Спешите опробовать наш магазин и не забудьте оставить отзыв.\n"
                f"Спасибо за внимание. 😊", reply_markup=get_menu_buttons(), parse_mode=ParseMode.HTML
    )

@router.message(Command("server"))
async def process_start_command(message: Message):
    await message.reply("Я подключен к Базе данных.\nВсё хорошо:)")

@router.message(Command("get_data"))
async def process_get_data_command(message: Message):
    try:

        departments = session.query(Departments).all()

        response_message = "Содержимое таблицы 'Отделы':\n"
        for department in departments:
            response_message += f"ID: {department.departmentid}\n" \
                               f"Отдел: {department.departmentname}\n" \
                               f"URL: {department.photourl}\n "

        await message.answer(response_message)
    except Exception as e:
        print(f"Error retrieving and sending data: {e}")

@router.message(F.text.lower() == "🏪 каталог")
async def cmd_catalog(message: Message):
    await message.reply("Здесь будет каталог")

@router.message(F.text.lower() == "🛠 настройки")
async def cmd_setting(message: Message):
    await message.reply("Здесь будут настройки")

@router.message(F.text.lower() == "🎧 поддержка")
async def cmd_support(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Github", url="https://github.com/1RMAsik")
    )
    builder.row(types.InlineKeyboardButton(
        text="Телеграм разработчика", url="https://t.me/ZachemNy")
    )

    await message.answer(
        'Чтобы связаться со мной выберите ссылку на Тг.',
        reply_markup=builder.as_markup()
    )
