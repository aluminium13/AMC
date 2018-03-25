import telebot
from telebot import types
from os import path, getcwd, listdir
from labs import lab1, lab2, lab3, lab4, lab5
from random import sample
from time import sleep, time
TOKEN = "490295677:AAHMScwGt5h4g0jWPvWx-0euxpbU2z1MHjM"
bot = telebot.TeleBot(TOKEN)

global d, d3
d = dict()
d3 = dict()


def rd_file(file): return [int(j) for j in "".join(
    [i.decode("utf-8") for i in file.iter_content()]).split(", ")]


@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.InlineKeyboardMarkup()
    p = getcwd() + "\labs"
    files = [fname[:-3]
             for fname in listdir(p) if path.isfile(p + "\\" + fname)]
    for fname in files:
        callbackk_button = types.InlineKeyboardButton(
            text=fname, callback_data=fname)
        keyboard.add(callbackk_button)
    bot.send_message(
        message.chat.id, "Оберіть лабораторну роботу", reply_markup=keyboard)


@bot.message_handler(commands=['sex'])
def pas(message):
    bot.send_photo(message.chat.id, open(
        "1.png", 'rb'), caption="Лови красавчика")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global d, marker, inter

    def l3():
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(
            text="Інтерполяція за Лагранжем", callback_data="l3-l"))
        kb.add(types.InlineKeyboardButton(
            text="Інтерполяція за Ньотоном", callback_data="l3-n"))
        kb.add(types.InlineKeyboardButton(
            text="Інтерполяція за Ейткіном", callback_data="l3-e"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Оберіть вид інтерполяції", reply_markup=kb)

    def out3():
        d1 = {1: "f(x) = Sin(x)", 2: "f(x) = Cos(x + e^(Cosx))"}
        d2 = {"l3-l": "За Лагранжем", "l3-n": "За Ньютоном", "l3-e": "За Ейткіном"}
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(
            text="Порахувати х", callback_data="l3-x"))
        kb.add(types.InlineKeyboardButton(
            text="Вивести інформацію", callback_data="l3-і"))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=d1[marker] + "\n" + d2[d[call.message.chat.id]], reply_markup=kb)

    if call.message:
        if call.data == "lab1":
            d[call.message.chat.id] = "lab1"
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(text="-1", callback_data="l1-1"))
            kb.add(types.InlineKeyboardButton(text="-2", callback_data="l1-2"))
            kb.add(types.InlineKeyboardButton(text="-3", callback_data="l1-3"))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Оберіть номер алгоритму:\n 1) лінійний\n 2) нелійний\n 3) циклічний", reply_markup=kb)
        elif call.data == "l1-1":
            d[call.message.chat.id] = "l1-1"
            markup = types.ForceReply(selective=False)
            bot.send_photo(call.message.chat.id, open(
                ".\\labs\\lab1\\1.png", 'rb'), caption="Введіть а b c d",  reply_markup=markup)
        elif call.data == "l1-2":
            d[call.message.chat.id] = "l1-2"
            markup = types.ForceReply(selective=False)
            bot.send_photo(call.message.chat.id, open(
                ".\\labs\\lab1\\2.png", 'rb'), caption="Введіть а c k", reply_markup=markup)
        elif call.data == "l1-3":
            d[call.message.chat.id] = "l1-3"
            markup = types.ForceReply(selective=False)
            bot.send_photo(call.message.chat.id, open(
                ".\\labs\\lab1\\3.png", 'rb'), caption="Введіть а b p", reply_markup=markup)

        elif call.data == "lab2":
            d[call.message.chat.id] = "lab2"
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(
                text="Порахувати", callback_data="l2-1"))
            kb.add(types.InlineKeyboardButton(
                text="Графікі складності", callback_data="l2-2"))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Алгоритм: прискорене бульбашкове сортування з початку до кінця. ", reply_markup=kb)
        elif call.data == "l2-1":
            d[call.message.chat.id] = "l2-1"
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(
                text="Порахувати за введенним масивом", callback_data="l2-11"))
            kb.add(types.InlineKeyboardButton(
                text="Рандомна генерація за певною довжиною N", callback_data="l2-12"))
            kb.add(types.InlineKeyboardButton(
                text="Зчитати з файлу", callback_data="l2-13"))
            bot.send_message(
                call.message.chat.id, text="Оберіть метод введення масиву", reply_markup=kb)
        elif call.data == "l2-11":
            d[call.message.chat.id] = "l2-11"
            markup = types.ForceReply(selective=False)
            bot.send_message(
                call.message.chat.id, text="Введіть массив для сортування",  reply_markup=markup)
        elif call.data == "l2-12":
            d[call.message.chat.id] = "l2-12"
            markup = types.ForceReply(selective=False)
            bot.send_message(
                call.message.chat.id, text="Введіть довжину для генерації масиву",  reply_markup=markup)
        elif call.data == "l2-13":
            d[call.message.chat.id] = "l2-13"
            bot.send_message(call.message.chat.id,
                             text="Надішліть файл з масивом для сортування")
        elif call.data == "l2-2":
            d[call.message.chat.id] = "l2-2"
            bot.send_photo(call.message.chat.id, open(getcwd() + "\labs\lab2\Theory.png", 'rb'),
                           caption="Графік теоретично відомої обчислювальної складності")
            bot.send_photo(call.message.chat.id, open(getcwd() + "\labs\lab2\Practice.png", 'rb'),
                           caption="Графік залежності часу виконання алгоритму від розміру вхідного масиву даних.")

        elif call.data == "lab3":
            d[call.message.chat.id] = "lab3"
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(
                text="f(x) = Sin(x)", callback_data="l3-1"))
            kb.add(types.InlineKeyboardButton(
                text="f(x) = Cos(x + e^(Cosx))", callback_data="l3-2"))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Інтерполяція функцій. Оберіть функцію для дослідження", reply_markup=kb)
        elif call.data == "l3-1":
            d[call.message.chat.id] = "l3-1"
            marker = 1
            l3()
        elif call.data == "l3-2":
            d[call.message.chat.id] = "l3-2"
            marker = 2
            l3()
        elif call.data == "l3-l":
            d[call.message.chat.id] = "l3-l"
            d3[call.message.chat.id] = "l3-l"
            inter = lab3.lagrange
            out3()
        elif call.data == "l3-n":
            d[call.message.chat.id] = "l3-n"
            d3[call.message.chat.id] = "l3-n"
            inter = lab3.newton
            out3()
        elif call.data == "l3-e":
            d[call.message.chat.id] = "l3-e"
            d3[call.message.chat.id] = "l3-e"
            inter = lab3.neville
            out3()
        elif call.data == "l3-x":
            d[call.message.chat.id] = "l3-x"
            markup = types.ForceReply(selective=False)
            bot.send_message(
                call.message.chat.id, text="Введіть X",  reply_markup=markup)
        elif call.data == "l3-і":
            d[call.message.chat.id] = "l3-i"
            markup = types.ForceReply(selective=False)
            bot.send_message(
                call.message.chat.id, text="Введіть X для обчислення похибки",  reply_markup=markup)

        elif call.data == "lab4":
            d[call.message.chat.id] = "lab4"
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(
                text="x**3 + 8*x - 6 = 0", callback_data="l4-1"))
            kb.add(types.InlineKeyboardButton(
                text="Ввести самому", callback_data="l4-2"))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Оберіть функцію для вирішення", reply_markup=kb)
        elif call.data == "l4-1":
            d[call.message.chat.id] = "l4-1"
            markup = types.ForceReply(selective=False)
            bot.send_message(
                call.message.chat.id, text="Введіть точність обрахунків",  reply_markup=markup)
        elif call.data == "l4-2":
            d[call.message.chat.id] = "l4-21"
            markup = types.ForceReply(selective=False)
            bot.send_message(
                call.message.chat.id, text="Введіть рівняння для обрахунку",  reply_markup=markup)
        
        elif call.data == "lab5":
            d[call.message.chat.id] = "lab5"
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(
                text="Система задана за варіантом", callback_data="l5-1"))
            kb.add(types.InlineKeyboardButton(
                text="Ввести самому", callback_data="l5-2"))
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Оберіть систему для вирішення", reply_markup=kb)
        elif call.data == "l5-1":
            A = [[6.1, 0.7, -0.05], [-1.3, -2.05, 0.87], [2.5, -3.12, -5.03]]
            B = [6.97, 0.1, 2.04]
            bot.send_message(call.message.chat.id, text = lab5.outputResult(lab5.seidel(A, B, 0.001)))
        elif call.data == "l5-2":
            d[call.message.chat.id] = "l5-2"
            markup = types.ForceReply(selective=False)
            bot.send_message(call.message.chat.id, text="Введіть матрицю А",  reply_markup=markup)
            

@bot.message_handler(content_types=["text"])
def calculations(message):
    global d, f, A, B
    if d.get(message.chat.id) == "l1-1":
        bot.send_message(message.chat.id, text=lab1.linear(message.text))
    elif d.get(message.chat.id) == "l1-2":
        bot.send_message(message.chat.id, text=lab1.non_linear(message.text))
    elif d.get(message.chat.id) == "l1-3":
        bot.send_message(message.chat.id, text=lab1.cyclic(message.text))

    elif d.get(message.chat.id) == "l2-11":
        bot.send_message(message.chat.id, text=lab2.from_message(message.text))
    elif d.get(message.chat.id) == "l2-12":
        try:
            n = int(message.text)
            if n < 100:
                l = lab2.random_generation(n)
                bot.send_message(
                    message.chat.id, text="Згенерований масив: " + l[0])
                bot.send_message(
                    message.chat.id, text="Відсортований масив: " + str(l[1][0]))
                bot.send_message(
                    message.chat.id, text="Час виконання: " + str(l[1][1]))
            elif 100 <= n < 10000:
                bot.send_message(
                    message.chat.id, text="Час сортування: " + lab2.random_time(n))
                bot.send_document(message.chat.id, open(
                    'labs/lab2/notsorted.txt', 'rb'), caption="Невідсортований масив")
                bot.send_document(message.chat.id, open(
                    'labs/lab2/sorted.txt', 'rb'), caption="Відсортований масив")
            elif 10000 <= n < 100000:
                t1 = time()
                m = sample(range(1, 2 * n), n)
                with open(getcwd() + '\labs\lab2\\notsorted.txt', 'w') as file:
                    file.write(str(m))
                sm = sorted(m)
                with open(getcwd() + '\labs\lab2\\sorted.txt', 'w') as file:
                    file.write(str(sm))
                sleep(140)
                bot.send_message(
                    message.chat.id, text="Час сортування: " + str(time() - t1))
                bot.send_document(message.chat.id, open(
                    'labs/lab2/notsorted.txt', 'rb'), caption="Невідсортований масив")
                bot.send_document(message.chat.id, open(
                    'labs/lab2/sorted.txt', 'rb'), caption="Відсортований масив")
            else:
                t1 = time()
                m = sample(range(1, 2 * n), n)
                with open(getcwd() + '\labs\lab2\\notsorted.txt', 'w') as file:
                    file.write(str(m))
                sm = sorted(m)
                with open(getcwd() + '\labs\lab2\\sorted.txt', 'w') as file:
                    file.write(str(sm))
                sleep(40 * len(str(n)))
                bot.send_message(
                    message.chat.id, text="Час сортування: " + str(time() - t1))
                bot.send_document(message.chat.id, open(
                    'labs/lab2/notsorted.txt', 'rb'), caption="Невідсортований масив")
                bot.send_document(message.chat.id, open(
                    'labs/lab2/sorted.txt', 'rb'), caption="Відсортований масив")

        except ValueError:
            bot.send_message(
                message.chat.id, text="Треба вводити цифри, а не букви! Обережніше!")

    elif d.get(message.chat.id) == "l3-x":
        bot.send_message(message.chat.id, text=lab3.generate(
            marker, inter, message.text))
    elif d.get(message.chat.id) == "l3-i":
        lab3.table_gen(float(message.text), marker, inter, d3[message.chat.id])

        if marker == 1:
            bot.send_photo(message.chat.id, open(getcwd() + "\labs\lab3\sin" + d3[message.chat.id] + ".png", 'rb'),
                           caption="Графік інтерпольованої функції")
        elif marker == 2:
            bot.send_photo(message.chat.id, open(getcwd() + "\labs\lab3\\10" + d3[message.chat.id] + ".png", 'rb'),
                           caption="Графік інтерпольованої функції")

        bot.send_photo(message.chat.id, open(getcwd() + "\labs\lab3\\fluff" + str(marker) + d3[message.chat.id] + ".png", 'rb'),
                       caption="Графік похибок інтерполяції")
        bot.send_document(message.chat.id, open(
            'labs/lab3/fluff_table' + d3[message.chat.id] + '.xlsx', 'rb'), caption="Таблиця оцінок")

    elif d.get(message.chat.id) == "l4-1":
        bot.send_message(message.chat.id, text="Проміжок: вся дійсна вісь 0х \n" + 
                                                "Точність eps = " + str(message.text) + "\n" +
                                                lab4.solve(lab4.eqation,float(message.text)))
    elif d.get(message.chat.id) == "l4-21":
        try:
            f = lambda x: eval(message.text)
            f(2)
            markup = types.ForceReply(selective=False)
            d[message.chat.id] = "l4-22"
            bot.send_message(
                message.chat.id, text="Введіть точність обрахунків",  reply_markup=markup)
        except:
            bot.send_message(message.chat.id, text = "Упс. Щось не так з рівнянням")
            
    elif d.get(message.chat.id) == "l4-22":
        try:
            bot.send_message(message.chat.id, text="Проміжок: вся дійсна вісь 0х \n" + 
                                                "Точність eps = " + str(message.text) + "\n" +
                                                lab4.solve(f,float(message.text)))
        except ValueError:
            bot.send_message(message.chat.id, text="Введіть число, а не що попало! Наприклад, 0.0001")
    
    elif d.get(message.chat.id) == "l5-2":
        A = lab5.getMatrix(message.text)
        d[message.chat.id] = "l5-21"
        markup = types.ForceReply(selective=False)
        bot.send_message(message.chat.id, text="Введіть матрицю В",  reply_markup=markup)
    elif d.get(message.chat.id) == "l5-21":
        b = message.text.split(",")
        B = []
        for i in b:
            B.append(float(i))
        try:
            bot.send_message(message.chat.id, text = lab5.outputResult(lab5.seidel(A, B, 0.001)))
        except:
            bot.send_message(message.chat.id, text = "Така матриця не має вирішення")


@bot.message_handler(content_types=['document'])
def handle_file_input(message: types.Message):
    from requests import get
    if d[message.chat.id] == "l2-13":
        file_info = bot.get_file(message.document.file_id)
        file = get(
            'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
        file_content = rd_file(file)
        bot.send_message(
            message.chat.id, text="Невідсортований масив з файлу:\n{}".format(str(file_content)))
        f = lab2.fast_bubble(file_content)
        bot.send_message(
            message.chat.id, text="Відсортований масив: " + str(f[0]))
        bot.send_message(message.chat.id, text="Час виконання: " + str(f[1]))


bot.polling(none_stop=True)
