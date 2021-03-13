import telebot
import requests
from CONFIG import *

bot = telebot.TeleBot(TOKEN)

requests.get('https://api.telegram.org/bot'+TOKEN+'/sendMessage'.format(bot), params=dict(
   chat_id='@areuherenow',
   text='Я здесь и сейчас!'
))