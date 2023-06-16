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


def print_message(message: str):
    print("=" * len(message))
    print(message)
    print("=" * len(message))


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


def user_event_5():
    # Эта функция собирает искомые данные
    element = input(event_5)
    return element


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


def user_event_7():
    # Эта функция запрашивает данные для удаления
    print("=" * len(event_7))
    del_user = input(event_7)
    print("=" * len(event_7))
    return del_user
