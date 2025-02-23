import telebot

from options import BOT_TOKEN
from logik import api

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Напиши /img и ваш промт")


@bot.message_handler(commands=['img'])
def send_image(message):
    promt = message.text.replace("/img", "").strip()

    if not promt:
        bot.send_message(message.chat.id, "Напишите /img и ваш промт (например: /img кот)")

    model_id = api.get_model()
    uuid = api.generate(promt, model_id)

    api.save_image(uuid=uuid, file_path='../output.jpg')

    with open("../output.jpg", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=f"{promt}:")


bot.polling()
