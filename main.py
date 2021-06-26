import os 
import telebot
from dotenv import load_dotenv
from response_generate import *

load_dotenv()

API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def greet(message):
    name = message.from_user.first_name 
    bot.send_message(message.chat.id, 
    f'Hy, {name}!\nSelamat datang di bot Aksara Bugis Writer \nSilahkan Masukkan Kata atau kalimat bahasa bugis yang ingin anda tulis dengan lontara (aksara bugis) dengan command seperti dibawah contoh ini\n 1. /w manu\n 2. /w kaluku\ndst..\n\n*Catatan Untuk Membedakan e dan E :v\n- enErgi\n- Empat\n- ember\n\nSelamat Mencoba :)\nJika Menemukan Error atau Bug\nContact : t.me/ToKu404', disable_web_page_preview=True)

@bot.message_handler(commands=['w'])
def hello(message):
    text = message.text[3:]
    text = generete_text(text)
    draw_text(text)
    bot.send_photo(message.chat.id, photo=open('pil_text.png', 'rb'))

# Memeriksa pesan
bot.polling()

