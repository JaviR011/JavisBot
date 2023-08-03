#pip install pyTelegramBotAPI   

import telebot
import random
bot = telebot.TeleBot("6413251424:AAHGMsUOf76-vSiiSWe0sgbqtd7gezPY9GM")
    
@bot.message_handler(commands=["start"])
def enviar(message):
    bot.reply_to(message, "Hola, Dominare el mundo")

@bot.message_handler(commands=["neko"])
def neko(message):
    img = ["nekos/n1.jpg","nekos/n2.jpg","nekos/n3.jpg","nekos/n4.jpg","nekos/n5.jpg"]
    imagen = img[random.randint(0, 2)]
    with open(imagen, 'rb') as image:
        bot.send_photo(message.chat.id, image)

bot.polling()