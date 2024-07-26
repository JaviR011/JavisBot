import telebot  # Importa la biblioteca telebot para interactuar con la API de Telegram
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para generar gráficos
import numpy as np  # Importa la biblioteca numpy para manejar arreglos numéricos
from io import BytesIO  # Importa BytesIO para manejar datos binarios en memoria

# Crea una instancia del bot con tu clave de API
bot = telebot.TeleBot("7135962405:AAEk7TiYPBR4XqQ3o3XrZLWDF6iGT4BBVZ8")

@bot.message_handler(commands=["graficar"])  # Maneja el comando /graficar
def graficar(message):
    try:
        # Extraemos los datos enviados por el usuario
        datos = message.text.split()[1:]  # Ignoramos el comando "/graficar"

        if not datos:  # Si no hay datos, lanzamos un error
            raise ValueError("Debes proporcionar una lista de números separados por comas.")

        # Convertimos los datos a una lista de números
        datos = [float(i) for i in datos[0].split(',')]  # Convertimos los datos a flotantes

        # Generamos la gráfica
        plt.figure()  # Creamos una nueva figura para el gráfico
        plt.plot(datos, marker='o')  # Graficamos los datos con marcadores en los puntos
        plt.title('Gráfica de Datos')  # Añadimos el título de la gráfica
        plt.xlabel('Índice')  # Etiqueta para el eje X
        plt.ylabel('Valor')  # Etiqueta para el eje Y

        # Guardamos la gráfica en un objeto BytesIO
        buf = BytesIO()  # Creamos un objeto BytesIO para almacenar la imagen
        plt.savefig(buf, format='png')  # Guardamos la gráfica en el objeto BytesIO en formato PNG
        buf.seek(0)  # Movemos el puntero del objeto BytesIO al principio
        plt.close()  # Cerramos la figura para liberar memoria

        # Enviamos la gráfica al usuario
        bot.send_photo(message.chat.id, buf)  # Enviamos la imagen al chat

    except Exception as e:
        # Si ocurre algún error, enviamos un mensaje de error
        bot.reply_to(message, f"Error: {str(e)}\nPor favor, asegúrate de enviar los datos en el formato correcto. Ejemplo: /graficar 1,2,3,4,5")

# Inicia la escucha de nuevos mensajes
bot.polling()
