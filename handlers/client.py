import random

from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram import types, Dispatcher


async def start(message: types.Message):
    await bot.send_message(message.chat.id, """
    Вас приветствует бот!
    Возможности клиента:
    /quiz    -     Отправляет мини викторину из 3х вопросов.
    /mem     -     Отправляет вам мемчик.
    /members -     Указывает количество участников в группе.
    /reg     -     Регистрация
    Возможности Админа:
    !pin     -     Закрепляет сообщение на которое вы ответили данной командой.
    !unpin   -     Открепляет все сообщения.
    Пока это все!
    """)


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton("next", callback_data="button_call")
    markup.add(button_call)

    question = "Владелец какой компании является Марк Цекерберг?"
    answers = ["VK", "FaceBook", "YouTube", "Telegram"]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup)


photo = open(f"photos/ds.jpg", "rb")


async def mem(message: types.Message):
    await bot.send_photo(message.chat.id, photo=photo)
    # await bot.send_message(message.chat.id,'photo')


async def pin(message: types.Message):
    await bot.pin_chat_message(message.reply_to_message.from_user)


def register_handler(dp: Dispatcher):
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'])
    dp.register_message_handler(start, commands=['start', 'intro', 'help', 'instruction'])
