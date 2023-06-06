"""
Используя команду '/hello', бот здоровается в ответ,
обращаясь к имени пользователя.
"""

import os
from pathlib import Path
from aiogram import Bot, Dispatcher, executor, types

import environ


ENVFILE = '.env'
BASEDIR = Path(os.path.dirname(__file__))

environ.add(BASEDIR / ENVFILE)


bot = Bot(token=os.getenv('TOKEN'))
dsp = Dispatcher(bot)


@dsp.message_handler(commands=['hello'])
async def hello(msg: types.Message):
    await msg.answer(f'Hello, {msg.from_user.first_name}!')


if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=True)
