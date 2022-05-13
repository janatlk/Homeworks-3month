from config import dp
from aiogram.utils import executor
import logging
import extra,callback,client,admin

callback.register_callbacks(dp)
admin.register_pin(dp)
client.register_handler(dp)
extra.register_all(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)


