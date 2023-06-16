from console import *
from func import *
from text import *

def start():
    while True:
        choice = user_event()
        check = check_file()
        match choice:
            case 1:
                if check == "":
                    print_message(error_event_1)
                else:
                    open_file()
                    print_message(event_1)
            case 2:
                if phone_list == []:
                    print_message(error_event_2)
                else:
                    save_file()
                    print_message(event_2)
            case 3:
                user_event_3(phone_list)
            case 4:
                if check != "" and phone_list == []:
                    print_message(error_event_4)
                else:
                    new_user = NewUser()
                    if new_user.name == "" or new_user.phone == "":
                        print_message(name_phone_error)
                    else:
                        new_contact(new_user.name, new_user.phone, new_user.comment)
                        print_message(event_4)
            case 5:
                if check == "" or phone_list == []:
                    print_message(event_error_5)
                else:
                    search_list = search_contact(user_event_5())
                    if search_list == []:
                        print_message(event_error_55)
                    else:
                        user_event_3(search_list)
            case 6:
                if phone_list == []:
                    print_message(event_error_66)
                else:
                    user_id = user_event_6()
                    if not user_id.isdigit():
                        print_message(event_error_6)
                    elif int(user_id) > int(phone_list[-1].get("id")):
                        print_message(event_error_6)
                    else:
                        command = change_event()
                        if not command.isdigit():
                            print_message(event_error_69)
                        elif 0 > int(command) or int(command) > 4:
                            print_message(event_error_69)
                        elif int(command) == 4:
                            continue
                        else:
                            u_variation = user_variation()
                            if u_variation == "":
                                print_message(variation_error)
                            else:
                                user_var(user_id, command, u_variation)
                                print_message(event_6_finish)
            case 7:
                if check == "" or phone_list == []:
                    print_message(event_error_5)
                else:
                    user_del = user_event_7()
                    if not user_del.isdigit():
                        print_message(event_error_7)
                    elif int(user_del) > int(phone_list[-1].get("id")):
                        print_message(event_error_7)
                    else:
                        del_user(user_del)
                        print_message(event_7_finish)
            case 8:
                break
