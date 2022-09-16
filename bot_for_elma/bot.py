import os
from urllib import response
from aiogram import Bot, Dispatcher, types, executor
from cachetools import cached, TTLCache
import requests
import json
#import bs4



BOT_TOKEN = ''
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hello, I'm the demo merchant bot.")



    # 3 hours cache time
cache = TTLCache(maxsize=100, ttl=10800)

@cached(cache)
def get_information(self):
    url = 'https://elmt.niivs.ru/pub/v1/app/test_notes/test_notes/list'
    geo_result = requests.request('POST', url, '')

    print(json.dump(geo_result))
    return geo_result()

@dp.message_handler(commands=['help'])
async def help_menu(message: types.Message, geo_result):
    await message.reply(message.chat.id, geo_result)



if __name__ == '__main__':
    executor.start_polling(dp)
