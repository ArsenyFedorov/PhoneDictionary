from text import *


def user_event():
    # Эта функция заставляет появится главное меню
    while True:
        print(meny)
        choice = input(event)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        print("=" * len(event_error_69))
        print(event_error_69)
        print("=" * len(event_error_69))


def user_event_1():
    # Эта функция сообщает о завершении 1 события
    print("=" * 22)
    print(event_1)
    print("=" * 22)


def error_1():
    # Эта функция сообщает об ошибке 1 события
    print("=" * 11)
    print(error_event_1)
    print("=" * 11)


def user_event_2():
    # Эта функция сообщает о завершении 2 события
    print("=" * len(event_2))
    print(event_2)
    print("=" * len(event_2))


def error_2():
    # Эта функция сообщает об ошибке 2 события
    print("=" * len(error_event_2))
    print(error_event_2)
    print("=" * len(error_event_2))


def user_event_3(book: list[dict[str, str]]):
    # Эта функция выводит телефонную книгу
    if book:
        print('\n' + '=' * 67)
        for contact in book:
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{uid:>3}. {name:<20} {phone:<20} {comment:<20}')
        print('=' * 67 + '\n')
    else:
        """Эта часть кода выводит ошибку третьего события"""
        print("=" * len(book_error))
        print(book_error)
        print("=" * len(book_error))


class NewUser:
    """Этот класс собирает новые данные"""

    def __init__(self):
        self.name = input(new_name)
        self.phone = input(new_phone)
        self.comment = input(new_comment)


def user_event_4():
    # Эта функция сообщает о том что контакт создан
    print("=" * len(event_4))
    print(event_4)
    print("=" * len(event_4))


def error_4():
    # Эта функция сообщает о том что файл не открыт
    print("=" * len(error_event_4))
    print(error_event_4)
    print("=" * len(error_event_4))


def error_input():
    # Эта функция сообщает об ошибке когда пользователь ничего не ввёл в поле имя или номер
    print("=" * len(name_phone_error))
    print(name_phone_error)
    print("=" * len(name_phone_error))


def user_event_5():
    # Эта функция собирает искомые данные
    element = input(event_5)
    return element


def error_5():
    # Эта функция сообщает о том что файл пустой или не открыт
    print("=" * len(event_error_5))
    print(event_error_5)
    print("=" * len(event_error_5))


def error_55():
    # Эта функция сообщает об отсутствие искомых данных
    print('=' * len(event_error_55))
    print(event_error_55)
    print('=' * len(event_error_55))


def user_event_6():
    # Эта функция запрашивает уникальный номер контакта
    print("=" * len(event_6))
    user_id = input(event_6)
    print("=" * len(event_6))
    return user_id


def change_event():
    # Эта функция выводит меню того что можно изменить
    print("=" * len(change))
    print(meny_change)
    command = input(change)
    print("=" * len(change))
    return command


def user_variation():
    # Эта функция прости пользователя ввести изменения
    print("=" * len(variation))
    u_variation = input(variation)
    print("=" * len(variation))
    return u_variation


def f_event_6():
    # Эта функция сообщает об окончании 6 события
    print("=" * len(event_6_finish))
    print(event_6_finish)
    print("=" * len(event_6_finish))


def error_6():
    # Эта функция сообщает что контакта который ввёл пользователь нет
    print("=" * len(event_error_6))
    print(event_error_6)
    print("=" * len(event_error_6))


def error_66():
    # Эта функция сообщает о том что файл пустой
    print("=" * len(event_error_66))
    print(event_error_66)
    print("=" * len(event_error_66))


def error_69():
    # Эта функция сообщает о том что такой функции нет
    print("=" * len(event_error_69))
    print(event_error_69)
    print("=" * len(event_error_69))


def var_error():
    # Эта функция сообщает о том что пользователь ничего не изменил
    print("=" * len(variation_error))
    print(variation_error)
    print("=" * len(variation_error))


def user_event_7():
    # Эта функция запрашивает данные для удаления
    print("=" * len(event_7))
    del_user = input(event_7)
    print("=" * len(event_7))
    return del_user


def f_event_7():
    # Эта команда сообщает о завершении 7 функции
    print("=" * len(event_7_finish))
    print(event_7_finish)
    print("=" * len(event_7_finish))


def error_7():
    # Эта функция сообщает об ошибке в 7 функции
    print("=" * len(event_error_7))
    print(event_error_7)
    print("=" * len(event_error_7))
