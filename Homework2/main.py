from config import dp
from aiogram.utils import executor
import logging
from handlers import extra, callback, client, admin, FSM

callback.register_callbacks(dp)
admin.register_pin(dp)
client.register_handler(dp)
FSM.reg_load(dp)
extra.register_all(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
