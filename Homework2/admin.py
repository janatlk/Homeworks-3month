from aiogram import types,Dispatcher
from config import bot,ADMIN



async def pin(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.reply("Вы не являетесь админоm в данной группе!")
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id,message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id,'Нужно ответить на сообщение чтобы его закрепить!')

def register_pin(dp: Dispatcher):
    dp.register_message_handler(pin,commands=['pin'], commands_prefix="!/")