phone_list = list()
way = "phone.txt"


def open_file():
    # Эта функция считывает данные с файла и сохраняет их в списке phone_list
    with open(way, encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        user_id, name, phone, comment, *_ = contact.strip().split(':')
        if {'id': user_id, 'name': name, 'phone': phone, 'comment': comment} not in phone_list:
            phone_list.append({'id': user_id, 'name': name, 'phone': phone, 'comment': comment})


def save_file():
    # Эта функция сохраняет файл
    with open(way, "w", encoding="utf-8") as f:
        for item in phone_list:
            id_u = item.get("id")
            name = item.get("name")
            phone = item.get("phone")
            comment = item.get("comment")
            f.write(f"{id_u}:{name}:{phone}:{comment}\n")


def new_contact(name: str, phone: str, comment: str):
    # Эта функция создаёт новый контакт
    if phone_list == []:
        phone_list.append({"id": "1", "name": name, "phone": phone, "comment": comment})
    else:
        phone_list.append(
            {"id": str(int(phone_list[-1].get("id")) + 1), "name": name, "phone": phone, "comment": comment})


def check_file():
    """Эта функция нужна для проверки текстового файла на наличие контактов
    тк если не открыть файл и начать сохранять файл индексация нарушится
    """
    with open(way, encoding="utf-8") as f:
        check = f.read()
    return check


def search_contact(element: str) -> list:
    # Эта функция ищет совпадения с тем что ввёл пользователь
    search_list = list()
    for item in phone_list:
        if element.lower() in item.get("id").lower():
            search_list.append(item)
        if element.lower() in item.get("name").lower():
            search_list.append(item)
        if element.lower() in item.get("phone").lower():
            search_list.append(item)
        if element.lower() in item.get("comment").lower():
            search_list.append(item)
    return search_list


def user_var(u_id: str, command: str, u_variation: str):
    # Эта функция меняет данные контакта по требованиям пользователя
    for item in phone_list:
        if item.get("id") == u_id:
            for i in range(1):
                if i + 1 == int(command):
                    item["name"] = u_variation
                    break
                elif i + 2 == int(command):
                    item["phone"] = u_variation
                    break
                else:
                    item["comment"] = u_variation


def del_user(id_u: str):
    # Эта функция удаляет выбранный элемент
    for item in phone_list:
        if id_u == item.get("id"):
            phone_list.remove(item)
