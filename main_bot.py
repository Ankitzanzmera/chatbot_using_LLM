import os,sys 
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher,executor,types 
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TOKEN = os.getenv("TOKEN")

class Refrence:
    ''' Class that store previously response from the chatgpt api'''
    def __init__(self) -> None:
        self.response = ""

reference = Refrence()

## Model Name
MODEL_NAME = "gpt-3.5-turbo"
bot  = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    ''' Clear the past Context of the bot'''
    reference.response = ""

@dispatcher.message_handler(commands=["start"])
async def welcome(message:types.message) -> None:
    await message.reply(f"Hi,\nI am Tele bot \nCreated by Ankit Zanzmera. \nCan i assist you?")

@dispatcher.message_handler(commands=['clear'])
async def clear(message:types.message):
    ''' A handler for clearing pass Conversation and context'''
    clear_past()
    await message.reply("I've Cleared the past Conversation and context")

@dispatcher.message_handler(commands=['help'])
async def help_menu(message:types.message):
    ''' A handler for Help menu'''

    help_command = """ Hi There, I'm  Chatgpt Telegram bot created by Ankit Zanzmera! Please Follow the Commands- 
    /start - To start the conversation
    /clear - To clear the conversation
    /help - To Get the help menu
    I Hope this helps you. :)
    """
    await message.reply(help_command)


@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    print(f">>> USER: \n\t{message.text}")
    response = openai.chat.completions.create(
        model = MODEL_NAME,
        messages = [
            {"role": "assistant", "content": reference.response}, # role assistant
            {"role": "user", "content": message.text} #our query 
        ]   
    )
    # print(response)
    reference.response = response.choices[0].message.content
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id, text = reference.response)


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=False)