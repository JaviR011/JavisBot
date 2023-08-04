#pip install pyTelegramBotAPI   
#https://t.me/nya_cats
import telebot
import random
from Funciones import sumar
bot = telebot.TeleBot("6413251424:AAHGMsUOf76-vSiiSWe0sgbqtd7gezPY9GM")

@bot.message_handler(commands=["start"])
def enviar(message):
    bot.reply_to(message, "Hola, Dominare el mundo.... ¡USANDO GATITOS!")

@bot.message_handler(commands=["neko"])
def neko(message):
    #img = ["nekos/n1.jpg","nekos/n2.jpg","nekos/n3.jpg","nekos/n4.jpg","nekos/n5.jpg"]
    imagen = "nekos/n"+str(random.randint(1,5))+".jpg"
    #imagen = img[random.randint(0, 2)]
    with open(imagen, 'rb') as image:
        bot.send_photo(message.chat.id, image)

@bot.message_handler(commands=['sumar'])
def handle_sumar(message):
    try:    
        # Extraemos los argumentos del mensaje
        command_args = message.text.split()[1:]  # Ignoramos el comando "/sumar"

        if len(command_args) != 2:
            raise ValueError("El comando debe tener dos números para sumar.")

        a = float(command_args[0])
        b = float(command_args[1])

        resultado = sumar(a,b)

        bot.reply_to(message, f"La suma de {a} y {b} es: {resultado}")
    except ValueError as e:
        bot.reply_to(message, str(e))
    except Exception as e:
        bot.reply_to(message, "Error al procesar la suma. Inténtalo nuevamente.")

@bot.message_handler(commands=['Hola'])
def handle_enviar_imagen(message):
    try: 
        # Ruta de la imagen almacenada localmente
        gif_path = 'nekos/hola-gatito.gif'  # Reemplaza con la ruta adecuada de tu imagen

        # Texto que acompañará la imagen
        caption_text = "¡Que Gusto Saludarte! 🌟"

        # Enviamos la imagen con el texto como leyenda
        with open(gif_path, 'rb') as gif_file:
                bot.send_document(message.chat.id, gif_file , caption=caption_text)
    except Exception as e:
        bot.reply_to(message,"¡Error al saludar!")

bot.polling()
