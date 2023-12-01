from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def message_text(message: Message):
    await message.answer(text=message.text)

@router.message(F.sticker)
async def message_sticker(message: Message):
    await message.reply_sticker(sticker=message.sticker.file_id)
    await message.answer("Я так тоже умею. 😎")

@router.message(F.animation)
async def message_gif(message: Message):
    await message.answer("О! Это же GIF😊")
    await message.answer_animation(animation=message.animation.file_id)