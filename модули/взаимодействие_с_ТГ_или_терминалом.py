import os
import time
from datetime import datetime
from pytz import UTC

# pip install python-dotenv
from dotenv import load_dotenv
# pip install python-telegram-bot==13.7
from telegram import Bot

load_dotenv()
ТОКЕН = os.getenv('TOKEN')
if not ТОКЕН:
    raise KeyError('Не найден файл .env')
БОТ = Bot(ТОКЕН)
этот_файл = __file__
this_folder = os.path.dirname(этот_файл)

def отправить_сообщение(сообщение, айди, кнопки = None):
    if type(айди) is int:
        БОТ.send_message(chat_id=айди, text=сообщение, reply_markup=кнопки)
    else:
        print(сообщение)

def проверить_входящие(айди=None):
    def создать_last_msg(update_id):
        with open(f'{this_folder}\\last_msg', 'w', encoding='utf-8') as file:
            file.write(str(update_id))

    def считать_last_msg():
        with open(f'{this_folder}\\last_msg', 'r', encoding='utf-8') as file:
            return int(file.read())
        
    now = datetime.now(UTC)
    if not os.path.exists(f'{this_folder}\\last_msg'):
        while True:
            try:
                обновления = БОТ.get_updates()
                if not обновления:
                    time.sleep(0.5)
                    continue
                break
            except:
                continue
        last_msg = обновления[-1]
        if last_msg.message.date < now:
            создать_last_msg(last_msg.update_id)
        else:
            создать_last_msg(last_msg.update_id - 1)

    while True:
        try:
            обновления = БОТ.get_updates(offset=считать_last_msg() + 1)
        except:
            time.sleep(1)
            continue
        if not обновления:
            continue

        обновления.reverse()
        print(len(обновления))
        for msg in обновления:
            if айди is None or msg.effective_user.id == айди:
                создать_last_msg(msg.update_id)
                print(msg.effective_message.text)
                return msg
        time.sleep(0.5)
