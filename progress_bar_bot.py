import os
import ptbot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')

bot = ptbot.Bot(token)
bot.send_message(chat_id, "Бот запущен")


def bot_reply(user_message):
    print('Привет! Ты написал мне:', user_message)


bot_message_to_chat = bot.reply_on_message(bot_reply)
bot.send_message(chat_id, bot_message_to_chat)

bot.run_bot()