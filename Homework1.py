from aiogram import Bot,Dispatcher,types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup, ParseMode
import logging
from decouple import config

Token = config("CODE")
bot = Bot(Token)
ds = Dispatcher(bot=bot)
@ds.message_handler(commands=['quiz','start'])
async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton("next",callback_data="button_call")
    markup.add(button_call)

    question = "Владелец какой компании является Марк Цекерберг?"
    answers = ["VK","FaceBook","YouTube","Telegram"]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup)

@ds.callback_query_handler(lambda call: call.data == "button_call")
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call2 = InlineKeyboardButton("next",callback_data="button_call2")
    markup.add(button_call2)
    question = "В каком году распался СССР?"
    answers = ['1990','1993','1991','2001']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        # reply_markup=markup
    )

@ds.message_handler()
async def echo(message: types.Message):
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    # if message == int:
    #     await bot.send_message(message.from_user.id, "its int")
    # else:
    if c == 1:
        await bot.send_message(message.from_user.id, f"{x*x}")
    elif c == 0:
        await bot.send_message(message.from_user.id,x)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(ds,skip_updates=True)