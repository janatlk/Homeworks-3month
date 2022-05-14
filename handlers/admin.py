from aiogram import types, Dispatcher
from config import bot, ADMIN


async def pin(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.reply("Вы не являетесь админоm в данной группе!")
    elif message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, 'Нужно ответить на сообщение чтобы его закрепить!')


async def unpin(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.reply("Для использования этой команды вы олжны быть Админом!")
    else:
        await bot.unpin_all_chat_messages(message.chat.id)


async def countmembers(message: types.Message):
    await bot.send_message(message.chat.id, bot.get_chat_member_count(message.chat.id))


def register_pin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix="!/")
    dp.register_message_handler(unpin, commands=['unpin'], commands_prefix="!/")
    dp.register_message_handler(countmembers, commands=['members'], commands_prefix="!/")
