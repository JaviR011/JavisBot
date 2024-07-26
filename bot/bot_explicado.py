# pip install pyTelegramBotAPI  # Comando para instalar la biblioteca pyTelegramBotAPI si aún no está instalada
# https://t.me/nya_cats  # Enlace al canal de Telegram de donde se pueden obtener imágenes de gatos

import telebot  # Importa la biblioteca telebot para interactuar con la API de Telegram
import random  # Importa la biblioteca random para seleccionar elementos aleatorios
from Funciones import sumar  # Importa la función sumar del módulo Funciones

# Crea una instancia del bot con tu clave de API
bot = telebot.TeleBot("7135962405:AAEk7TiYPBR4XqQ3o3XrZLWDF6iGT4BBVZ8")

@bot.message_handler(commands=["help"])  # Maneja el comando /help
def enviar(message):
    bot.reply_to(message,"/start - Inicia la interacción \n" +
                          "/neko - Manda imágenes de gatitos \n" +
                          "/Hola - Manda un divertido saludo \n" +
                          "/suma n n - Realiza una suma (reemplaza las n por números)")

@bot.message_handler(commands=["start"])  # Maneja el comando /start
def enviar(message):
    bot.reply_to(message, "Hola, ¡Dominaré el mundo.... USANDO GATITOS!")

@bot.message_handler(commands=["neko"])  # Maneja el comando /neko
def neko(message):
    # img = ["nekos/n1.jpg", "nekos/n2.jpg", "nekos/n3.jpg", "nekos/n4.jpg", "nekos/n5.jpg"]
    # Selecciona una imagen aleatoria de 5 posibles opciones
    imagen = "nekos/n" + str(random.randint(1, 5)) + ".jpg"
    # imagen = img[random.randint(0, 2)]
    
    # Abre la imagen seleccionada y la envía al chat
    with open(imagen, 'rb') as image:
        bot.send_photo(message.chat.id, image)

@bot.message_handler(commands=['sumar'])  # Maneja el comando /sumar
def handle_sumar(message):
    try:
        # Extraemos los argumentos del mensaje
        command_args = message.text.split()[1:]  # Ignoramos el comando "/sumar"

        if len(command_args) != 2:
            raise ValueError("El comando debe tener dos números para sumar.")

        # Convertimos los argumentos a números flotantes
        a = float(command_args[0])
        b = float(command_args[1])

        # Llamamos a la función sumar y obtenemos el resultado
        resultado = sumar(a, b)

        # Respondemos con el resultado de la suma
        bot.reply_to(message, f"La suma de {a} y {b} es: {resultado}")
    except ValueError as e:
        # Si hay un error en los valores proporcionados, enviamos el mensaje de error
        bot.reply_to(message, str(e))
    except Exception as e:
        # Si ocurre cualquier otro error, enviamos un mensaje de error genérico
        bot.reply_to(message, "Error al procesar la suma. Inténtalo nuevamente.")

@bot.message_handler(commands=['Hola'])  # Maneja el comando /Hola
def handle_enviar_imagen(message):
    try:
        # Ruta de la imagen almacenada localmente
        gif_path = 'nekos/hola-gatito.gif'  # Reemplaza con la ruta adecuada de tu imagen

        # Texto que acompañará la imagen
        caption_text = "¡Que Gusto Saludarte! 🌟"

        # Enviamos la imagen con el texto como leyenda
        with open(gif_path, 'rb') as gif_file:
            bot.send_document(message.chat.id, gif_file, caption=caption_text)
    except Exception as e:
        # Si ocurre algún error, enviamos un mensaje de error
        bot.reply_to(message, "¡Error al saludar!")

# Inicia la escucha de nuevos mensajes
bot.polling()
