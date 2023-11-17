import os
from dotenv import load_dotenv    # pip install python-dotenv
import requests
# pip install python-telegram-bot==13.7
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

load_dotenv()
ТОКЕН = os.getenv('TOKEN')
БОТ = Bot(ТОКЕН)

def отправить_сообщение(чат, сообщение):
    кнопки = [["Коломна", "Воскренск", "Москва"], ["/help"]]
    рег_кнопки = ReplyKeyboardMarkup(кнопки, resize_keyboard=True)
    БОТ.send_message(chat_id=чат.id, text=сообщение, reply_markup=рег_кнопки)
    имя_пользователя = чат.first_name
    

def запарсить_погоду(город):

    ссылка = "https://www.google.com/search"
    параметры = {"q" : f"погода в городе {город}"}
    ответ_сайта = requests.get(url=ссылка, params=параметры)

    текст = ответ_сайта.text
    старт = текст.find('°C')
    старт = текст.find('>', старт - 10)
    стоп = текст.find('<', старт)
    ответ = текст[старт + 1:стоп]
    if len (ответ) == 0:
        return "Город не распознан"
    return ответ 

def реакция(информация, контекст):
    текст_сообщение = информация.effective_message.text
    ид_чата = информация.effective_message.chat
    погода = запарсить_погоду(текст_сообщение)
    print(f'Запрос - "{текст_сообщение}". Ответ - "{погода}"')
    отправить_сообщение(ид_чата, погода)

def старт(информация, контекст):
    ид_чата = информация.effective_message.chat
    имя_пользователя = информация._effective_message.chat.first_name
    сообщение = f"""Привет, {имя_пользователя}!

Бот поможет тебе узнать погоду в нужном для тебя городе. Введи название интересующего тебя города для получении информации"""
    отправить_сообщение(ид_чата, сообщение)

def help(информация, контекст):
    ид_чата = информация.effective_message.chat
    имя_пользователя = информация._effective_message.chat.first_name
    сообщение = f"""Привет, {имя_пользователя}!

Бот поможет тебе узнать погоду в нужном для тебя городе. Введи название интересующего тебя города для получении информации"""
    отправить_сообщение(ид_чата, сообщение)


def запустить_бота():
    обновление = Updater(ТОКЕН)

    # эта строка позволяет реагировать на стандартные команды, которые пользователь пишет через /, например /start 
    обновление.dispatcher.add_handler(CommandHandler('start', старт))
    обновление.dispatcher.add_handler(CommandHandler('help', help))

    # Эта строка позволяет реагировать на входящие текстовые сообщения
    обновление.dispatcher.add_handler(MessageHandler(Filters.text, реакция))

    # Эта строка заставляет код опрашивать сервер телеграмма с заданным интервалом
    обновление.start_polling(poll_interval=1)
    print('бот запущен')
    
    # запускает процесс опроса сервера (выполняется бесконечно)
    обновление.idle()


# print(запарсить_погоду('казань'))

# отправить_сообщение(923992817, "Персональный бот")
запустить_бота()
