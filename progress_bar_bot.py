import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse

load_dotenv()
token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')

bot = ptbot.Bot(token)
bot.send_message(chat_id, "Бот запущен")
print('Бот запущен')
bot.send_message(chat_id, 'На сколько запустить таймер?')
print('На сколько запустить таймер?')


def bot_reply(user_time_message):
    seconds = parse(user_time_message)
    bot_message_to_chat = 'Таймер запущен на {} секунд'.format(seconds)
    print(bot_message_to_chat)
    bot.send_message(chat_id, bot_message_to_chat)
    bot.create_countdown(seconds, notify_progress)
#    bot.create_timer(seconds, time_out_message)


#def time_out_message():
#    print('Время вышло')
#    bot.send_message(chat_id, "Время вышло")


def notify_progress(secs_left):
    if secs_left >= 1:
        secs_left_to_chat = 'Осталось секунд: {}'.format(secs_left)
    else:
        secs_left_to_chat = 'Время вышло'
#    print(secs_left_to_chat)
#    bot.send_message(chat_id, secs_left_to_chat)
    message_id = bot.send_message(chat_id, secs_left_to_chat)
    print(secs_left_to_chat)
    bot.update_message(chat_id, message_id, secs_left_to_chat)
    print(secs_left_to_chat)


bot.reply_on_message(bot_reply)

bot.run_bot()
