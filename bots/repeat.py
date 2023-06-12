"""
Бот повторяет за пользователем.
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


@dsp.message_handler(content_types=[types.ContentType.ANY])
async def repeat(msg: types.Message):
    await msg.answer(f'{msg.text}')


if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=True)
