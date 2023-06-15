from console import *
from func import *


def start():
    while True:
        choice = user_event()
        check = check_file()
        match choice:
            case 1:
                if check == "":
                    error_1()
                else:
                    open_file()
                    user_event_1()
            case 2:
                if phone_list == []:
                    error_2()
                else:
                    save_file()
                    user_event_2()
            case 3:
                user_event_3(phone_list)
            case 4:
                if check != "" and phone_list == []:
                    error_4()
                else:
                    new_user = NewUser()
                    if new_user.name == "" or new_user.phone == "":
                        error_input()
                    else:
                        new_contact(new_user.name, new_user.phone, new_user.comment)
                        user_event_4()
            case 5:
                if check == "" or phone_list == []:
                    error_5()
                else:
                    search_list = search_contact(user_event_5())
                    if search_list == []:
                        error_55()
                    else:
                        user_event_3(search_list)
            case 6:
                if phone_list == []:
                    error_66()
                else:
                    user_id = user_event_6()
                    if not user_id.isdigit():
                        error_6()
                    elif int(user_id) > int(phone_list[-1].get("id")):
                        error_6()
                    else:
                        command = change_event()
                        if not command.isdigit():
                            error_69()
                        elif 0 > int(command) or int(command) > 4:
                            error_69()
                        elif int(command) == 4:
                            continue
                        else:
                            u_variation = user_variation()
                            if u_variation == "":
                                var_error()
                            else:
                                user_var(user_id, command, u_variation)
                                f_event_6()
            case 7:
                if check == "" or phone_list == []:
                    error_5()
                else:
                    user_del = user_event_7()
                    if not user_del.isdigit():
                        error_7()
                    elif int(user_del) > int(phone_list[-1].get("id")):
                        error_7()
                    else:
                        del_user(user_del)
                        f_event_7()
            case 8:
                break
