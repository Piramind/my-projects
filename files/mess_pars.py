import requests
import telebot
from bs4 import BeautifulSoup
import datetime
import time


daynames = []

@bot.message_handler(content_type=['text'])
def message_parse(message):
    message = message.split(' ')
    message[0].upper()
    if message[0] in daynames:
        pass
    elif message[0] == 'tomorrow':
        pass
    elif message[0] == 'near':
        pass
    elif message[0] == 'дата хз хз':
        pass
    else:
        return 'ошибка ввода лох'
    return *args