import telebot
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='start')
def help(msg):
    user_id = msg.chat.id
    bot.send_message(user_id, f"Для заказа наберите /order/n")


@bot.message_handler(commands='order')
def size_pizza(msg):
    message = msg.text
    user_id = msg.chat.id
    bot.send_message(user_id, f"Какую пиццу желаете заказать ? Большую или маленькую ?")

@bot.message_handler(content_types='text')
def big_pizza(msg):
    global size
    message = msg.text
    user_id = msg.chat.id
    if message == 'большую':
        size = message
        bot.send_message(user_id, f"Какая у вас будет оплата? Наличными или картой ?")
        
    elif message == "маленькую":
        size = message
        bot.send_message(user_id, f"Какая у вас будет оплата? Наличными или картой ?")
        

@bot.message_handler(content_types='text')
def card_pizza(msg):
    message = msg.text
    user_id = msg.chat.id
    if message == 'картой':
        type_buy = message
        bot.send_message(user_id, f"Хорошо вот что я записал. Вы хотите" + size +"пиццу"+"Оплата - "+ type_buy + "?")
    elif message == "наличными":
        type_buy = message
        bot.send_message(user_id, f"Хорошо вот что я записал. Вы хотите" + size +"пиццу"+"Оплата - "+ type_buy + "?")
        
                




if __name__ == '__main__':
    bot.polling(none_stop=True)
