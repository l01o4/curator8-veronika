import telebot

bot = telebot.TeleBot('6500311970:AAGGY7EXYDs5NlssVzSGaKBlfvm7eR7nvIs')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Привет! \nСвободный вечер и не знаешь, чем себя занять? Выбирай жанр фильма в меню, а я подберу несколько для тебя!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['fantasy'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* Звездные Войны (серия фильмов) \n*2.* Аватар \n*3.* Гарри Поттер (серия фильмов) \n*4.* Дом странных детей Мисс Перегрин \n*5.* Сумерки (серия фильмов) \n*6.* Хроники Нарнии (серия фильмов) \n*7.* Пираты Карибского моря (серия фильмов) \n*8.* Властелин колец (серия фильмов) \n*9.* Хоббит (серия фильмов) \n*10.* Малефисента',
                     parse_mode='Markdown')


@bot.message_handler(commands=['science fiction'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* Стражи Галактики (серия фильмов) \n*2.* Веном \n*3.* Человек-паук (серия фильмов) \n*4.* Аквамен \n*5.* Индиана Джонс (серия фильмов) \n*6.* Мстители: Война бесконечности \n*7.* Валериан и город тысячи планет \n*8.* Голодные игры (серия фильмов) \n*9.* Терминатор (серия фильмов) \n*10.* Пятый элемент',
                     parse_mode='Markdown')


@bot.message_handler(commands=['comedy'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* Один дома \n*2.* Кухня (сериал) \n*3.* Батя \n*4.* Мистер и миссис Смит \n*5.* Отпетые мошенницы \n*6.* Астерикс и Обеликс (серия фильмов) \n*7.* Третий лишний \n*8.* Стажер \n*9.* Иван Васильевич меняет профессию \n*10.* Ловушка для родителей',
                     parse_mode='Markdown')


@bot.message_handler(commands=['thriller'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* Молчание ягнят \n*2.* Семь \n*3.* Прошлой ночью в Сохо \n*4.* Отступники \n*5.* Зодиак \n*6.* Чёрный лебедь \n*7.* Бегущий в лабиринте \n*8.* Бессонница \n*9.* Остров проклятых \n*10.* Бойцовский клуб',
                     parse_mode='Markdown')


@bot.message_handler(commands=['detective'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* Достать ножи \n*2.* Тайное окно \n*3.* Подмена \n*4.* Смерть на Ниле \n*5.* Шерлок Холмс \n*6.* Адвокат дьявола \n*7.* Иллюзия обмана \n*8.* Энола Холмс \n*9.* Ветреная река \n*10.* Невидимый гость',
                     parse_mode='Markdown')


@bot.message_handler(commands=['adventure'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* Анчартед: На картах не значится \n*2.* Джуманджи: Зов джунглей \n*3.* Мумия \n*4.* Сокровище нации \n*5.* Интерстеллар \n*6.* Парк Юрского периода \n*7.* Кинг Конг \n*8.* Дюна \n*9.* Ночь в музее \n*10.* Орудия смерти: Город костей',
                     parse_mode='Markdown')


@bot.message_handler(commands=['drama'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* 1+1 \n*2.* Дьявол носит Prada \n*3.* Хорошо быть тихоней \n*4.* Лед \n*5.* Маленькие женщины \n*6.* Тарзан. Легенда \n*7.* Ной \n*8.* Тоня против всех \n*9.* 2+1 \n*10.* Мальчик в полосатой пижаме',
                     parse_mode='Markdown')


@bot.message_handler(commands=['family'])
def main(message):
    bot.send_message(message.chat.id,
                     '*1.* Двое: я и моя тень \n*2.* Собачья жизнь \n*3.* Путешествие к центру земли \n*4.* Перси джексон (серия фильмов) \n*5.* Король Лев \n*6.* Чарли и шоколадная фабрика \n*7.* Бунт ушастых \n*8.* Последний богатырь \n*9.* Алиса в стране чудес \n*10.* H2O: Просто добавь воды (сериал)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['more'])
def main(message):
    bot.send_message(message.chat.id,
                     'Вы можете перейти по этой [ссылке](https://yandex.ru/video/movies/) и найти больше интересных фильмов. Приятного просмотра!!!',
                     parse_mode='Markdown')


bot.infinity_polling()