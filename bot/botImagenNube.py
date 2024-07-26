import telebot  # Importamos la librería telebot para interactuar con la API de Telegram
import random  # Importamos la librería random para generar números aleatorios
import requests  # Importamos la librería requests para hacer solicitudes HTTP
from io import BytesIO  # Importamos BytesIO para manejar datos en memoria como archivos

# Creamos una instancia del bot usando el token proporcionado por Telegram
bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_API_KEY")

# La API key de Pexels, necesaria para autenticar las solicitudes a su API
PEXELS_API_KEY = "YOUR_PEXELS_API_KEY"

# Definimos un manejador para el comando "/neko"
@bot.message_handler(commands=["neko"])
def neko(message):
    url = "https://api.pexels.com/v1/search"  # URL de la API de búsqueda de Pexels
    headers = {
        "Authorization": PEXELS_API_KEY  # Encabezado de autenticación con la API key de Pexels
    }
    params = {
        "query": "cat",  # Parámetro de búsqueda, en este caso buscamos imágenes de "cat" (gato)
        "per_page": 1,  # Número de resultados por página, en este caso solo necesitamos uno
        "page": random.randint(1, 100)  # Número de página aleatorio para obtener una imagen aleatoria
    }
    response = requests.get(url, headers=headers, params=params)  # Realizamos la solicitud GET a la API de Pexels
    data = response.json()  # Convertimos la respuesta en formato JSON a un diccionario de Python
    image_url = data['photos'][0]['src']['large']  # Extraemos la URL de la imagen de alta calidad del primer resultado

    response = requests.get(image_url)  # Realizamos una solicitud GET a la URL de la imagen para descargarla
    image = BytesIO(response.content)  # Convertimos el contenido de la imagen en un objeto BytesIO (archivo en memoria)

    # Enviamos la imagen al chat desde donde se recibió el comando "/neko"
    bot.send_photo(message.chat.id, image)

# Iniciamos el bot para que empiece a recibir y manejar mensajes
bot.polling()
