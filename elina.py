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
    item6 = types.KeyboardButton("Для поднятия настроения")
    item7 = types.KeyboardButton("Мотивация")
    

    markup.add(item1,item2,item3,item4,item5,item6,item7)
    
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
        elif message.text == 'Для поднятия настроения':
            mood_list = ['Видео с котятяами', 'Сходить в кино', 'Сходить в театр', 'Сходить в кафе', 'Купить безделушку', 'Посмотреть фильм', 'Нарисовать картину', 'Полепить', 'Поспать', 'Сходить в котокафе', 'Помедитировать', 'Сходить погулять', 'Сходить в веревочный парк', 'Проанализировать ситуацию и выявить плюсы', 'Сделать пенную ванну', 'Массаж', 'Посмотреть мотивирующее видео', 'Написать мысли на бумагу', 'Написать рассказ', 'Написать стихотворение']
            print(random.choice(mood_list))
            bot.send_message(message.chat.id, random.choice(mood_list))      

        elif message.text == "Котенок":
            cat_list= ['https://hvost.news/upload/resize_cache/iblock/8b8/750_400_1/pochemu_kotenok_lizhet_volosy_i_zaryvaetsja_v_nih.jpg', 'https://petstime.ru/sites/default/files/styles/article-500/public/field/image/5week.jpg?itok=f4zhCXrL','https://i.pinimg.com/originals/52/83/61/528361ccabb359c715ebfc5f01038764.jpg','https://vplate.ru/images/article/orig/2019/04/kotenok-v-1-2-mesyaca-osobennosti-razvitiya-i-uhoda-25.jpg','https://www.acana.ru/media/article/kotyonok-ne-est-suhoy-korm-kak-priuchit.jpg','https://avatars.mds.yandex.net/get-zen_doc/1704908/pub_5cfa3f3bbabd4000b092ba9d_5cfa45edbbfeea00af312197/scale_1200']
            bot.send_photo(message.chat.id, random.choice(cat_list))

        elif message.text == 'Мотивация':
            motivation_list = ['«Возможности не приходят сами — вы создаете их». Крис Гроссер (Chris Grosser)', '«Успех обычно приходит к тем, кто слишком занят, чтобы его просто ждать». Генри Девид Торо (Henry David Thoreau)', '«Возьмите идею. Сделайте ее своей жизнью — думайте о ней, мечтайте о ней, живите ею. Пусть ваш разум, мышцы, нервы, каждая часть тела будет наполнена этой одной идеей. Вот он — путь к успеху». Свами Вивекананда (Swami Vivekananda)', '«Чтобы достичь успеха, перестаньте гнаться за деньгами, гонитесь за мечтой». Тони Шей (Tony Hsieh)', '«Даже если вы проходите через ад, продолжайте идти». Уинстон Черчилль (Winston Churchill)', '«Не бойтесь пожертвовать хорошим ради еще лучшего». Джон Рокфеллер (John D. Rockfeller)', '«Есть два вида людей, которые будут вам говорить, что вы не сможете чего-то добиться: те, кто сами боятся пробовать, и те, кто боятся, что у вас получится». Рей Гофорт (Ray Goforth)', '«Успешные люди делают то, что неуспешные не хотят делать. Не стремитесь, чтобы было легче, стремитесь, чтобы было лучше». Джим Рон (Jim Rohn)', '«Многие люди терпят неудачу только потому, что сдаются в двух шагах от успеха». Саймон Хартли (Simon Hartley)', '«Поднимите планку. Делайте то, на что вы вроде бы не способны. Не задумывайтесь о пределе ваших возможностей. Делайте то, чего сделать не можете». Пол Арден (Paul Arden)', '«Бездействие порождает беспокойство и страх. Действие — уверенность и смелость. Если ты хочешь победить страх, не сиди дома и не думай об этом. Встань и действуй». Мэг Джей (Meg Jay)', '«Инвестирование — это бизнес, где вы можете выглядеть очень глупо в течение длительного периода времени, прежде чем вы докажете, что правы». Билл Акман (William Albert Ackman)', '«Мир полон изобилия и возможностей, но слишком многие люди приходят к фонтану жизни с решетом вместо цистерн или с чайной ложкой вместо экскаватора. Они ожидают малого и в результате получают мало». Бен Свитленд (Ben Sweetland)', '«Деньги – это одно из воплощений силы. Но еще большей силой обладает финансовое образование. Деньги приходят и уходят, но если вам известно как они работают, то вы можете управлять ими и становиться богаче». Роберт Кийосаки (Robert Toru Kiyosaki)', '«Одна победа не ведет к успеху, в отличие от постоянного желания побеждать». Винс Ломбарди (Vince Lombardi)', '«Осуществляйте свои мечты, или кто-то наймет вас для осуществления своих». Фарра Грей (Farrah Gray)', '«Успех – это лестница, на нее не взобраться, держа руки в карманах». Пауль Баует (Paul Friedrich Peter Bauer)','«Всегда помните о том, что ваша решимость преуспеть важнее всего остального». Авраам Линкольн (Abraham Lincoln)', '«Я твердо верю в удачу, и я заметил: чем больше я работаю, тем я удачливее». Томас Джефферсон (Thomas Jefferson)', '«Пока у тебя есть попытка – ты не проиграл». Сергей Бубка']
            bot.send_message(message.chat.id, random.choice(motivation_list)) 

        else:
            bot.send_message(message.chat.id, 'Я - Элиноид-3000, прогрессивный бот.')

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
