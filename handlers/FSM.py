from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

import config
from config import bot,dp
cancel_button = KeyboardButton("CANCEL")
cancel_marcup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

cancel_marcup.add(cancel_button)

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.photo.set()
        await bot.send_message(
            message.chat.id,
            f"Привет {message.from_user.full_name}, скинь фотку блюда!",
            reply_markup=cancel_marcup
        )
    else:
        await message.answer("Пиши в личку!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Название блюда?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Опишите блюдо?")


async def load_description(message: types.Message, state: FSMContext):
    a = message.text.split()
    if len(a) > 4:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.answer("Какая цена блюда?")
    else:
        await bot.send_message(message.chat.id,'Минимум 5 слов')


async def load_price(message:types.Message,state: FSMContext):
    try:
        async with state.proxy() as data:
            data['price'] = int(message.text)

        await FSMAdmin.next()
        await message.answer("Регистрация блюда завершена!")
    except:
        await bot.send_message(message.chat.id,'Только численные значения')

async def cancel_registration(message:types.Message,state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("Регистрация отменена!")

async def show_reg(message: types.Message,state: FSMContext):
    # await bot.send_photo(message.chat.id)
    # await bot.send_message()
    # a = {}
    async with state.proxy() as data:
        try:
            await bot.send_photo(message.chat.id, data['photo'])
            await bot.send_message(message.chat.id, f"""
Название    : {data['name']}
Описание    : {data['description']}
Цена           : {data['price']}
                """)
        except:
            await bot.send_message(message.chat.id, "Для начала зарегестрируйтесь!")

def reg_load(message:types.Message):
    dp.register_message_handler(cancel_registration,state="*",commands='cancel')
    dp.register_message_handler(cancel_registration,Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(load_photo,state=FSMAdmin.photo,content_types=["photo"])
    dp.register_message_handler(load_name,state=FSMAdmin.name)
    dp.register_message_handler(load_description,state=FSMAdmin.description)
    dp.register_message_handler(load_price,state=FSMAdmin.price)
    dp.register_message_handler(fsm_start,commands=['reg'])
    dp.register_message_handler(show_reg,commands=['ch'])