import telebot
from telebot import types
import random
from random import choice


bot = telebot.TeleBot('6931737827:AAHaS7LszjXrZK7eqxqmGWxpL1EMfZhrSrc')
fact1 = "Путеводная звезда. \n"+"Ежегодно в честь новых студентов загорается «звезда первокурсника». Традиция зародилась с первого года существования университета, и День знаний в САФУ без "+\
        "этой процедуры уже немыслим. Десять лет – десять звёзд на аллее у главного корпуса университета возле памятника Михаилу Васильевичу Ломоносову. И сколько таких "+\
        "символических светил ещё появится за долгие годы САФУ! Словно в стихотворном произведении гениального помора: «Открылась бездна, звёзд полна: звёздам числа нет, "+\
        "бездне дна…» За прошедшее десятилетие у выпускников и студентов старших курсов появилась собственная традиция – назначать встречу у своей звезды."

fact2 = "Миссия выполнима. \n"+"Миссия университета – научное и кадровое обеспечение защиты геополитических интересов России в Арктике."+\
        "Стратегическая цель университета – формирование интеллектуального центра освоения Арктики в международном пространстве."

fact3 = "Арктический вектор. \n"+"Миссия, цели и задачи САФУ напрямую связаны с реализацией Стратегии развития Арктической зоны Российской Федерации. Важная часть арктических"+\
        " образовательных программ – возможность прохождения стажировок и практик в Арктике, необходимых для освоения и развития северных территорий."+\
        " Университет ведёт подготовку кадров для 15 отраслей экономики Арктической зоны по 98 программам арктической направленности. "

fact4 = "Политика партнёрства. \n"+"Среди российских партнёров – Московский государственный университет, Санкт-Петербургский государственный университет, РГУ нефти и газа имени Губкина,"+\
        " Дальневосточный федеральный университет, Уральский федеральный университет имени Б. Н. Ельцина и другие знаменитые вузы. "+\
        "Арктический вектор САФУ определяет тесные связи с вузами Норвегии, Финляндии, Швеции, Канады и США. Среди научных и деловых партнёров – университет Буде,"+\
        "колледж Нарвика, университет Лапландии, университет Осло, Школа бизнеса в городе Йончепинге. "+\
        "САФУ сотрудничает с ведущими вузами Великобритании, Германии, Польши, Китая, Кореи и других стран. "

fact5 = "Поверить алгеброй гармонию. \n"+"В настоящее время в САФУ обучаются более 24 тысяч студентов из 54 стран. В структуре университета семь высших школ, 81 кафедра, семь базовых кафедр и"+\
        " три филиала кафедр. Кроме того – два колледжа, три филиала (в Северодвинске, Коряжме, Нарьян-Маре), представительство в Москве, а также научные, "+\
        "технологические, образовательные центры и лаборатории. А так же общая численность научно-преподавательского состава САФУ более 800 человек. "
fact6 = "С опорой на традиции. \n"+"Университет сохраняет традиции научных школ Севера и даёт новый импульс к развитию уникальной системы «школа-завод-втуз»: студенты САФУ работают на заводах "+\
        "Северодвинска параллельно с обучением. Данная система успешно реализуется в образовательном процессе «Севмашвтуза». Это уникальный центр многоуровневого инженерного "+\
        "образования, осуществляющий подготовку по всем уровням высшего образования, связанным с кораблестроением и океанотехникой, машиностроением и технологическим оснащением" +\
        "производства, автоматизацией производственных процессов и систем, информатикой и вычислительной техникой, ядерной и радиационной безопасностью. "

fact7 = "Ориентация на инновации. \n"+"Гордость САФУ – уникальный Центр пользования научным оборудованием «Арктика» для высокоточных анализов исследований веществ, позволяющих с атомной точностью "+\
        "исследовать структуру вещества. Каждая из девяти лабораторий центра оснащена специальным оборудованием, направленным на исследование актуальных вопросов "+\
        "жизнеобеспечения северян, а также на мониторинг, прогнозирование и предупреждение рисков переноса загрязняющих веществ и их распространения в биологических экосистемах."+\
        "Университет создаёт краткосрочные образовательные интенсивы – летние и зимние арктические школы. Успешным примером межвузовского партнёрства является Летняя школа "+\
        "на Соловках САФУ и Высшей школы экономики. "

fact8 = "САФУ объединяет регионы и страны. \n"+"В университете активно ведётся экспедиционная деятельность в Российской Арктике и за её пределами. Уникальный проект «Арктический плавучий университет» стал визитной "+\
        "карточкой не только университета, но и всей страны. За восемь лет (2012–2019 гг.) на борту научно-исследовательского судна «Профессор Молчанов» проведено 12 экспедиций. "+\
        "Совместная научная деятельность укрепляет международные связи. В САФУ функционирует лаборатория, созданная в рамках постановления правительства под руководством ведущего "+\
        "учёного из Норвегии. Ежегодно вуз проводит около 100 международных мероприятий."
fact9 = "Социальная сфера. \n"+"В мае 2011 года на базе САФУ открылся Центр подготовки волонтёров в первую очередь для главного спортивного события мира – Олимпиады. В мае 2013 года САФУ встретил огонь "+\
        "XXVII Всемирной летней Универсиады. Движущая сила университета – бойцы студенческих отрядов. С 2011 года проводится Всероссийская олимпиада студотрядов «Старт», "+\
        "которая объединяет лучших бойцов Северо-Западного региона страны. "

fact10 = "Ориентация – Север. \n"+"За минувшее десятилетие в университете появились современные площадки: геологический музей имени академика Н. Лаверова, технопарк, Центр деревянного зодчества и "+\
        "деревянного домостроения, Центр физики, музей природы Арктики и другие. В 2014 году построен Интеллектуальный центр – научная библиотека САФУ. В 2014 году Северный "+\
        "(Арктический) федеральный университет удостоен региональной общественной награды «Достояние Севера». Престижную награду вуз получил в номинации "+\
        "«Предприятие непроизводственной сферы». Университет завершает реализацию «Программы развития САФУ на 2010-2020 гг.», одобренную Правительством Российской Федерации. "+\
        "Готова новая программа развития САФУ на 2021-2035 годы. В ней арктический вектор университета определён ещё более чётко, отражена и его особая роль как основной "+\
        "научно-образовательной базы."
safufacts = [fact1,fact2,fact3,fact4,fact5,fact6,fact7,fact8,fact9,fact10]


@bot.message_handler(commands=['start']) #стартовая команда
def start(message):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🏫 Университет")#
        btn2 = types.KeyboardButton('🔭 Наука и инновации')
        btn3 = types.KeyboardButton('📚 Обучение')
        btn4 = types.KeyboardButton('🌐 Iternational (Международная деятельность)')
        btn5 = types.KeyboardButton('🎓 Жизнь САФУ')
        btn6 = types.KeyboardButton('🤔 Интересный факт')
        btn7 = types.KeyboardButton('🔎 Поиск')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, "👋 Вас приветствует информационно-справочный бот"+\
                        " Северного Арктического федерального университета имени М.В. Ломоносова", reply_markup=markup)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
#---------------------------------------------Университет
    if message.text == "🏫 Университет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Основные сведения")
        btn2 = types.KeyboardButton("Визитная карточка")
        btn3 = types.KeyboardButton('Структура и контакты')
        btn4 = types.KeyboardButton('Работа в САФУ')
        btn5 = types.KeyboardButton('Сотрудничество САФУ')
        btn6 = types.KeyboardButton('Программа развития')
        btn7 = types.KeyboardButton('🔙 Вернуться в главное меню')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == 'Основные сведения':

        with open("Main_info/Основные_сведения.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строк
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Визитная карточка':
        with open("Main_info/Визитная_карточка.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Структура и контакты':
        with open("Main_info/Структура_и_контакты.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Работа в САФУ':
        with open("Main_info/Работа_в_САФУ.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents )

    elif message.text == 'Сотрудничество САФУ':
        with open("Main_info/Сотрудничество_в_САФУ.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Программа развития':
        with open("Main_info/Программа_развития.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)


    elif message.text == '🔙 Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🏫 Университет")#
        btn2 = types.KeyboardButton('🔭 Наука и инновации')
        btn3 = types.KeyboardButton('📚 Обучение')
        btn4 = types.KeyboardButton('🌐 Iternational (Международная деятельность)')
        btn5 = types.KeyboardButton('🎓 Жизнь САФУ')
        btn6 = types.KeyboardButton('🤔 Интересный факт')
        btn7 = types.KeyboardButton('🔎 Поиск')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

#🔎 Поиск
    elif message.text == '🔎 Поиск':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Вернуться в главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '📲 Если вы хотите найти конкретную информацию на сайте'+\
                        " воспользуйтесь поиском - перейдя по [ссылке](https://narfu.ru/search/)", \
                        reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🤔 Интересный факт':
        bot.send_message(message.from_user.id, random.choice(safufacts))

#-----------------------------------------------------------Наука и инновации
    elif message.text == '🔭 Наука и инновации':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Инфраструктура")#
        btn2 = types.KeyboardButton('Аспирантура, докторантура и диссертационные советы')
        btn3 = types.KeyboardButton('Молодым учёным')
        btn4 = types.KeyboardButton('Экспедиционная деятельность САФУ')
        btn5 = types.KeyboardButton('Публикации')
        btn6 = types.KeyboardButton('Национальный проект «Наука и университеты»')
        btn7 = types.KeyboardButton('🔙 Вернуться в главное меню')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == 'Инфраструктура':

        with open("Science/Инфраструктура.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Аспирантура, докторантура и диссертационные советы':
        with open("Science/Аспирантура.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Молодым учёным':
        with open("Science/Молодым_ученым.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Экспедиционная деятельность САФУ':
        with open("Science/Экспедиции.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents )

    elif message.text == 'Публикации':
        with open("Science/Публикации.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Национальный проект «Наука и университеты»':
        with open("Science/Проект_Наука_и_университеты.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

#-----------------------------------------------Обучение
    elif message.text == '📚 Обучение':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Основные образовательные программы")#
        btn2 = types.KeyboardButton('Дополнительное образование')
        btn3 = types.KeyboardButton('Стипендии/Материальная помощь')
        btn4 = types.KeyboardButton('Электронное обучение')
        btn5 = types.KeyboardButton('Практика и трудоустройство')
        btn6 = types.KeyboardButton('Аккредитация')#
        btn7 = types.KeyboardButton('🔙 Вернуться в главное меню')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == 'Основные образовательные программы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Образовательные программы - Бакалавриат")#
        btn2 = types.KeyboardButton('Образовательные программы - Магистратура')
        btn3 = types.KeyboardButton('Образовательные программы - Специалитет')
        btn4 = types.KeyboardButton('🔙 Вернуться назад')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == '🔙 Вернуться назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Основные образовательные программы")#
        btn2 = types.KeyboardButton('Дополнительное образование')
        btn3 = types.KeyboardButton('Стипендии/Материальная помощь')
        btn4 = types.KeyboardButton('Электронное обучение')
        btn5 = types.KeyboardButton('Практика и трудоустройство')
        btn6 = types.KeyboardButton('Аккредитация')#
        btn7 = types.KeyboardButton('🔙 Вернуться в главное меню')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == 'Образовательные программы - Бакалавриат':
        with open("Study/Бакалавр.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Образовательные программы - Магистратура':
        with open("Study/Магистратура.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Образовательные программы - Специалитет':
        with open("Study/Специалитет.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Дополнительное образование':
        with open("Study/Дополнительное_образование.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents )

    elif message.text == 'Стипендии/Материальная помощь':
        with open("Study/Стипендии.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Электронное обучение':
        with open("Study/Электронное_обучение.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Практика и трудоустройство':
        with open("Study/Практика.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Аккредитация':
        with open("Study/Аккредитация.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

#--------------------------------International
        
    elif message.text == '🌐 Iternational (Международная деятельность)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Структура международного сотрудничества")#
        btn2 = types.KeyboardButton('Международные партнерства')
        btn3 = types.KeyboardButton('Новости и объявления')
        btn4 = types.KeyboardButton('Международная проектная деятельность')
        btn5 = types.KeyboardButton('Учеба за рубежом')
        btn6 = types.KeyboardButton('Для инностранных студентов')
        btn7 = types.KeyboardButton('🔙 Вернуться в главное меню')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == 'Структура международного сотрудничества':

        with open("International/Структура.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Международные партнерства':
        with open("International/Международные_партнерства.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Новости и объявления':
        with open("International/Новости_и_Объявления.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Международная проектная деятельность':
        with open("International/Международная_проектная_деятельность.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents )

    elif message.text == 'Учеба за рубежом':
        with open("International/Учеба_за_рубежом.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Для инностранных студентов':
        with open("International/Для_инностранных_студентов.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

#-----------------------------------------Жизнь САФУ
    elif message.text == '🎓 Жизнь САФУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Спорт")#
        btn2 = types.KeyboardButton('Социально-воспитательная работа')
        btn3 = types.KeyboardButton('Творческий центр')
        btn4 = types.KeyboardButton('Новости САФУ')
        btn5 = types.KeyboardButton('Волонтерский центр')
        btn6 = types.KeyboardButton('Общественные объединения')
        btn7 = types.KeyboardButton('🔙 Вернуться в главное меню')#
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7)
        bot.send_message(message.from_user.id, '⬇️ Выберите интересующий вас раздел', reply_markup=markup)

    elif message.text == 'Спорт':

        with open("Life/Спорт.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Социально-воспитательная работа':
        with open("Life/Социально-воспитательная_работа.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)
    
    elif message.text == 'Творческий центр':
        with open("Life/Творческий_центр.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Новости САФУ':
        with open("Life/Новости_САФУ.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents )

    elif message.text == 'Волонтерский центр':
        with open("Life/Волонтерский_центр.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    elif message.text == 'Общественные объединения':
        with open("Life/Общественные_объединения.txt", "rb") as f: # открываем документ
            contents = f.read().decode("UTF-8") # считываем все строки
        bot.send_message(message.from_user.id, contents)

    #Small talk
    elif message.text == 'Привет!':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'Привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Как дела?':
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю людям!')

    elif message.text == 'что делаешь?':
        bot.send_message(message.from_user.id, 'Помогаю людям!')

    elif message.text == 'как дела':
        bot.send_message(message.from_user.id, 'Хорошо!')
    else:
        bot.send_message(message.from_user.id, 'К сожалению, не понимаю')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть