import os
from urllib import response
from aiogram import Bot, Dispatcher, types, executor
from cachetools import cached, TTLCache
import requests
import json
import bs4



BOT_TOKEN = ''
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Hello, I'm the demo merchant bot.")



class CountryService:

    # 3 hours cache time
    cache = TTLCache(maxsize=100, ttl=10800)

    @cached(cache)
    def get_information(self):
        url = 'https://niivs.elma365.ru/pub/v1/app/LK/list'
        geo_result = requests.request('GET', url)
        return geo_result.json()

    @dp.message_handler(commands=['help'])
    async def help_menu(message: types.Message, geo_result):
        await message.reply(message.chat.id, geo_result.json)

def get_request_from_elma_list(self):
    pass
    #return response.json


if __name__ == '__main__':
    executor.start_polling(dp)
