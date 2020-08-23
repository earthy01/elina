import random
import telebot

from telebot import types
 
TOKEN = '1030426189:AAHA7HYGTJQvDB-dvUKIsAgF5bGIkt4LSgQ' 
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Орел или решка")
    item2 = types.KeyboardButton("Расскажи о себе")
    item3 = types.KeyboardButton("Котенок")
    item4 = types.KeyboardButton("Основное блюдо")
    item5 = types.KeyboardButton("Десерт")
    

    markup.add(item1,item2,item3,item4,item5)
    
    bot.send_message(message.chat.id, "Привет, {0.first_name} меня зовут Элина. ".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    bot.send_photo(message.chat.id, 'https://sun9-36.userapi.com/c851536/v851536172/13b41a/E9YX-nxcNzw.jpg');    

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Орел или решка':
 
            markup = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton("Тебе повезло!", callback_data='jest')
 
            markup.add(item1)
            item_list = ['Орел', 'Решка']
            bot.send_message(message.chat.id, random.choice(item_list), reply_markup=markup)

        elif message.text == 'Расскажи о себе':

            markup = types.InlineKeyboardMarkup(row_width=4)

            item2 = types.InlineKeyboardButton("Довольно-таки интересная личность", callback_data='about')
            
            markup.add(item2)


            bot.send_message(message.chat.id, 'Ну как видишь я бот. Какой-то черт заточил меня в какой-то телеге и теперь я выполняю всякие команды. А так-то я художница, спортсменка, чайлдф..комсомолка', reply_markup=markup)
        elif message.text == 'Основное блюдо':
            food_list = ['Гречка с капустой', 'Овсянка с бананами', 'Пюре с огурцами и помидорами', 'Пшено c капустой', 'Ячмень с капустой', 'Овсянка с персиками', 'Рис с кукурузой', 'Яичница с салатом', 'Манка', 'Салат', 'Гречка с огурцами и помидорами', 'Овсянка с капустой', 'Рис с капустой']
            bot.send_message(message.chat.id, random.choice(food_list))

        elif message.text == 'Десерт':
            desert_list = ['Блинчики', 'Творог с бананами', 'Тортик', 'Печеньки', 'Кофе с взбитыми сливками', 'Хлопья','Шоколад', 'Элиночка']
            print(random.choice(desert_list))
            bot.send_message(message.chat.id, random.choice(desert_list))    

        elif message.text == "Котенок":
            bot.send_photo(message.chat.id, 'https://opt-1031816.ssl.1c-bitrix-cdn.ru/upload/resize_cache/iblock/8b8/750_400_1/pochemu_kotenok_lizhet_volosy_i_zaryvaetsja_v_nih.jpg?152818987087154')
            

        else:
            bot.send_message(message.chat.id, 'Я - Элиноид-2000, прогрессивный бот.')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'jest':
                bot.send_message(call.message.chat.id, 'Конечно!😊')
            elif call.data == 'about':
                bot.send_message(call.message.chat.id, 'Внатуре.')
    except Exception as e:
        print(repr(e))            

bot.polling(none_stop=True)
