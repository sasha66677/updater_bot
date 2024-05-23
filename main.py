import os
from os.path import join, dirname
from dotenv import load_dotenv

import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from aiogram import html

logging.basicConfig(level=logging.INFO)


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


bot = Bot(token=os.environ.get("TG_API_TOKEN"))
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}"
    )

@dp.message(Command("pull"))
async def cmd_test1(message: types.Message):
    await message.answer("Ok")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())