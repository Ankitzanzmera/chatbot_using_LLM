import os
import logging
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher,executor,types

load_dotenv()

api_token = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO)

## Initialize and dipatcher

bot = Bot(token=api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def command_start_handler(message:types.message) -> None:
    await message.reply(f"Hi,\nI am Echobot \nPowered by Ankit Zanzmera")

@dp.message_handler(commands=["help"])
async def command_start_handler(message:types.message) -> None:
    await message.reply(f"Please Mail your query to 22msrds052@jainuniversity.ac.in ")

@dp.message_handler()
async def echo(message:types.message) -> None:
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)