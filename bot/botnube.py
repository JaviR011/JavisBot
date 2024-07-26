import telebot
import random
import requests
from io import BytesIO

bot = telebot.TeleBot("7135962405:AAEk7TiYPBR4XqQ3o3XrZLWDF6iGT4BBVZ8")

PEXELS_API_KEY = "UMCoJ1XP76BeWat3JD9zBiGll2uUaTDfpdJwam0tcFTLWi1MiOyuAt42"

@bot.message_handler(commands=["neko"])
def neko(message):
    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": "cat",
        "per_page": 1,
        "page": random.randint(1, 100)
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    image_url = data['photos'][0]['src']['large']
    response = requests.get(image_url)
    image = BytesIO(response.content)
    bot.send_photo(message.chat.id, image)

bot.polling()
