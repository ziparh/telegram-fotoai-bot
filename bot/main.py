import telebot
import os

from options import BOT_TOKEN
from logik import api

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello! Write /img <your pormt>")


@bot.message_handler(commands=['img'])
def send_image(message):
    promt = message.text.replace("/img", "").strip()

    if not promt:
        bot.send_message(message.chat.id, "Write /img <your pormt> (for example: /img cat)")
        return

    bot.send_chat_action(message.chat.id, "typing")
    msg_load = bot.send_message(message.chat.id, "Wait a few seconds for the photo to be generated...")

    model_id = api.get_model()
    uuid = api.generate(promt, model_id)

    api.save_image(uuid=uuid, file_path='output.jpg')

    with open("output.jpg", "rb") as photo:
        bot.send_chat_action(message.chat.id, "upload_photo")
        bot.send_photo(message.chat.id, photo, caption=f"{promt}:")

    bot.delete_message(message.chat.id, msg_load.message_id)
    os.remove("output.jpg")


bot.polling()
