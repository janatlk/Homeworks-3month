from aiogram import Bot,Dispatcher
from decouple import config

Token = config("CODE")
bot = Bot(Token)
dp = Dispatcher(bot=bot)
ADMIN = 520632727