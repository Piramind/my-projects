from email import message
import telebot
import wikipedia, re
from telebot import *

# Создаем экземпляр бота
bot = telebot.TeleBot("5244078884:AAGByx3ek2pL2bLZC5n_jClVUyhfGmzP194")
# Устанавливаем русский язык в Wikipedia
wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = ny.content[:200]
        # Разделяем по точкам
        wikimas = wikitext.split(".")
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ""
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not ("==" in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if len((x.strip())) > 3:
                    wikitext2 = wikitext2 + x + "."
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub("\([^()]*\)", "", wikitext2)
        wikitext2 = re.sub("\([^()]*\)", "", wikitext2)
        wikitext2 = re.sub("\{[^\{\}]*\}", "", wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return "В энциклопедии нет информации об этом"


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(message, res=False):
    bot.send_message(
        message.chat.id, "Отправьте мне любое слово, и я найду его значение на Wikipedia"
    )


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


# Запускаем бота
bot.polling(none_stop=True, interval=0)
