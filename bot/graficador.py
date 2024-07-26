import telebot
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO

bot = telebot.TeleBot("7135962405:AAEk7TiYPBR4XqQ3o3XrZLWDF6iGT4BBVZ8")

@bot.message_handler(commands=["graficar"])
def graficar(message):
    try:
        # Extraemos los datos enviados por el usuario
        datos = message.text.split()[1:]
        
        if not datos:
            raise ValueError("Debes proporcionar una lista de números separados por comas.")

        # Convertimos los datos a una lista de números
        datos = [float(i) for i in datos[0].split(',')]

        # Generamos la gráfica
        plt.figure()
        plt.plot(datos, marker='o')
        plt.title('Gráfica de Datos')
        plt.xlabel('Índice')
        plt.ylabel('Valor')

        # Guardamos la gráfica en un objeto BytesIO
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()

        # Enviamos la gráfica al usuario
        bot.send_photo(message.chat.id, buf)

    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}\nPor favor, asegúrate de enviar los datos en el formato correcto. Ejemplo: /graficar 1,2,3,4,5")

bot.polling()

