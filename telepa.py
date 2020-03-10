import telebot
  
bot = telebot.TeleBot()

@bot.message_handler(command=['start'])
def get_start(message):
        bot.send_message(message.chat.id)


def get_quest(message):
        bot.send_message(message.chat.id, "Доброго времени суток.")
        bot.send_message(message.chat.id, "Как настроение?")

        with open('slovar.txt') as file:
                counter = 0
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_first(message):
        bot.set_update_listener(id)
        bot.send_message(message.chat.id, "Хорошо ли провели день?(если ночь, то что собираетесь сегодня делать?")
        counter = get_quest(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter


def get_second(message):
        bot.set_update_listener(id)
        bot.send_message(message.chat.id, "Хорошо, я тебя понял. Следующий вопрос: Довольны ли вы тем, как Вы проводите время?")
        counter = get_first(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter


def get_more(message):
        bot.set_update_listener(id)
        bot.send_message(message.chat.id, "Хорошо, я вас понял. Следующий вопрос: Как Вы себя чувствуете сегодня?")
        counter = get_second(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter


def get_third(message):
        bot.send_message(message.chat.id, "Хорошо ли провели день?(если ночь, то что собираетесь сегодня делать?")
        counter = get_more(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter


def get_four(message):
        bot.send_message(message.chat.id, "Сделали ли Вы то, что планировали?")
        counter = get_third(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_five(message):
        bot.send_message(message.chat.id, "С кем Вы сегодня общались? Не было ли дискуссий?")
        counter = get_four(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_six(message):
        bot.send_message(message.chat.id, "Занимались ли Вы тем, что Вам нравится? ")
        counter = get_five(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_seven(message):
        bot.send_message(message.chat.id, "Что самое хорошее с Вами сегодня произошло?")
        counter = get_six(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_sev(message):
        bot.send_message(message.chat.id, "Что самое плохое произошло с Вами за день?")
        counter = get_seven(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_habe(message):
        bot.send_message(message.chat.id, "Считаете ли Вы свой день продуктивным?")
        counter = get_sev(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter


def get_nope(message):
        bot.send_message(message.chat.id, "Перечислите все полезные вещи, что Вы сделали за день(не забывайте о мелочах)")
        counter = get_habe(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_dope(message):
        bot.send_message(message.chat.id, "Что бы могло улучшить Ваше настроение?")
        counter = get_nope(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter


def get_pov(message):
        bot.send_message(message.chat.id, "Встречали ли Вы сегодня неприятных людей?")
        counter = get_dope(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_forum(message):
        bot.send_message(message.chat.id, " Как Вы почувствовали себя сегодня с утра?")
        counter = get_pov(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_skoro(message):
        bot.send_message(message.chat.id, "Делали ли Вы то, что вам не нравится?")
        counter = get_forum(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_dadada(message):
        bot.send_message(message.chat.id, "Кто-нибудь давит на Вас?(опишите подробности)")
        counter = get_skoro(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter


def get_konec(message):
        bot.send_message(message.chat.id, "Присутствует ли у Вас напряжение?(опишите из-за чего)")
        counter = get_dadada(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_finish(message):
        bot.send_message(message.chat.id, "Нравится ли Вам погода сегодня?")
        counter = get_konec(message)
        with open('slovar.txt') as file:
                if message.text in file.read(): 
                        counter += 1
                else: 
                        counter += 0
        return counter

def get_finally(message):
        counter = get_more(message)
        bot.send_message(message.chat.id, "Подсчитав результаты я советую тебе....")
        if counter > 12:
                bot.send_message(message.chat.id, "Привет, дорогой,советую тебе как можно скорее обратиться к специалисту. Это уже серьезно.")
        elif 9 < counter < 11:
                bot.send_message(message.chat.id, "Привет дорогой, смотрю ты в отчаяние ТАК НЕ ПОЙДЕТ, пора ҝто менять отбрось то что тебе мешает. ЭТО ТВОЯ ЖИЗНЬ! ТОЛЬКО ТЫ РЕШАЕШЬ КАК ТЕБЕ ЖИТЬ И ТОЛЬКО ОТ ТЕБЯ ЗАВИСИТ ЧЕМ ТЫ НАПОЛНИШЬ СВОЕ СВОБОДНОЕ ВРЕМЯ. Найди себе свое хоуми.")
        elif 7 < counter < 9:
                bot.send_message(message.chat.id, "Привет дорогой, пора бросить себе вызов. Надот выходить из зоны комфорта, пора проверить свое тело на прочность. Хотя я думаю что у тебя ничего не получиться. Я ошибаюсь ? Докажи мне обратное. Пойди в зал, запишись на плавание, почитай две недели Войну и мир.")
        elif 5 < counter < 7:
                bot.send_message(message.chat.id, "Привет дорогой, устал от бытовухи ? Попробуй то чего ты раньше боялся. Стань независимым от других. Разве тебе кто-то нужен, чтобы сходить в кино?")
        elif 3 < counter < 5:
                bot.send_message(message.chat.id, "Привет, дорогой, ты наверное устал ? Выйди на улицу, сьешь шоколадку, посмотри вокруг. Жизнь прекрасна.")
        elif counter < 3:
                bot.send_message(message.chat.id, "Привет, дорогой, да ты отлично себя чувствуешь, тебе улыбается весь мир, а ты улыбаешься ему в ответ.")

if __name__ == '__main__':
    bot.polling(none_stop=True)