data = {}
phone_data = {}


def reg():
    while True:
        phone = str(input("Введите ваш номер телефона: +7"))
        if len(phone) >= 10 and len(phone) < 13:
            login = str(input("Придумайте имя пользователя: "))
            while True:
                password = str(input("Придумайте оригинальный пароль: "))

                if password.islower() == False and password.isalpha() == False and password.isdigit() == False and phone.isdigit() and len(password) >= 6:
                    data[login] = password
                    phone_data[login] = phone
                    print("Регистрация завершена.")
                    return
                else:
                    print("Обратите внимание: Длина пароля должна составлять не менее 6 символов, пароль должен содержать уникальные символы и хотя бы одну заглавную букву.")
        else:
            print("Введите правильный номер телефона.")


def vhod():
    attempts_3 = 4
    attenpts = 0
    input_login = str(input("Имя пользователя: "))

    while attenpts < attempts_3:
        input_password = str(input("Пароль: "))
        if input_login in data and data[input_login] == input_password:
            print("Успешный вход.")
            return

        else:
            w = str(input("Забыли пароль? Да(1), Нет(2): "))
            if w == "1":
                input_phone = str(input("Введите номер телефона: +7"))
                if input_login in phone_data and phone_data[input_login] == input_phone:
                    while True:
                        new_password = str(input("Придумайте новый пароль: "))
                        if new_password.islower() == False and new_password.isalpha() == False and new_password.isdigit() == False and input_phone.isdigit() and len(new_password) >= 6:
                            data[input_login] = new_password
                            print("Пароль успешно изменён.")
                            return
                        else:
                            print("Пароль не соответствует требованиям. Обратите внимание: Длина пароля должна составлять не менее 6 символов, пароль должен содержать уникальные символы и хотя бы одну заглавную букву.")
                else:
                    print("Неверный логин или номер телефона.")

            if w == "2":
                attenpts += 1
                print("Неверный пароль. Попыток осталось:", attempts_3 - attenpts)

    print("Вы исчерпали количество попыток.")

def vyhod():
    print("Работа завершена.")
    return


while True:
    a = str(input("Добро пожаловать на сайт gdz! Нажмите (1) для регистрации, (2) для входа, (3) для завершения работы: "))
    if a == "1":
        reg()
    elif a == "2":
        vhod()
    elif a == "3":
        vyhod()
        break
