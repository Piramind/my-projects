from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import pyowm

TOKEN = "1886761313:AAF2iOtAtRSMIKgVtYL3pkjcrbdx7dsNvKE"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['lead', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Я вирт. человек. Приятно познакомиться',{msg.from_user})



@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')
"""
@dp.message_handler(commands=['weather'])
async def get_weather():
    wm = pyowm.OWM('', Language = "ru")
    place = input("В каком городе искать ?")
    observation = owm.weather_at_place('London,GB')
    w = observation.get_weather()
    print(w)
"""

if __name__ == '__main__':
   executor.start_polling(dp)