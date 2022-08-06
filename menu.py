import json
import id_number as id
import files_editor as fe


def menu_admin():
    print('Введите пароль: ')


def menu_user():
    print('База данных')
    choice = input(
        'Для работы, введите номер пункта меню.\n'
        '1. Добавить. \n'
        '2. Поиск. \n'
        '3. Изменить. \n'
        '4. Удалить.\n'
        '5. Показать список работников\n'
        '>> ')
    
    match choice:
        case '1': add_contact()
        case '2': print(find_contact())
        case '3': edit_contact()
        case '4': del_contact()
        case '5': view_workers()


def add_contact():
    global id_number, name, type_doc, number_tel, department, type_worker, comment, all_workers
    
    name = input('Введите Имя Фамилию >> ')
    type_doc = input('Введите тип документа >> ')
    number_tel = input('Введите номер телефона >> ')
    department = input('Введите отдел >> ')
    type_worker = input('Введите должность >> ')
    comment = input('Введите комментарий >> ')
    id_number = id.set_id()

    worker = [{'id_number': id_number, 'type_doc': type_doc,
               'number_tel': number_tel, 'department': department,
               'type_worker': type_worker, 'comment': comment}]
    
    id_to_name = fe.load_json('data_files\id_to_name.json')
    id_to_name[id_number] = name
    fe.save_json(id_to_name,'data_files\id_to_name.json')
    all_workers = fe.load_json()
    all_workers[name] = worker
    fe.save_json(all_workers)


def del_contact():
    print('Введите Имя Фамилию, если вы хотите удалить по id, введите "id"')
    name = input('>> ')
    all_workers = fe.load_json()
    all_workers.pop(name)
    fe.save_json(all_workers)


def edit_contact():
    return 0


def find_contact():
    finder = init_find()
    if finder.isdigit():
        print(finder)
        print(type(finder))
        id_to_name = fe.load_json('data_files\id_to_name.json')
        name = id_to_name.get(finder)
        all_workers = fe.load_json()
        
        if name is None:
            print('Пользователь не найден')
            if quit():
                find_contact()
            else:
                exit()
        else:
            return f'{name} : {all_workers.get(name)}'
        
    else:
        print(finder)
        print(type(finder))
        all_workers = fe.load_json()
        if all_workers.get(finder) is None:
            print('Пользователь не найден')
            if quit():
                find_contact()
            else:
                exit()
        else:
            return f'{finder} : {all_workers.get(finder)}'
        
        
# Просто ввод отдельной функцией
def init_find():
    print('Введите Имя Фамилию или "id"')
    msg = input('>> ')
    return msg
    
def view_workers():
    dict = fe.load_json('data_files\id_to_name.json')
    for i in dict.keys():
        print(f'{i}: {dict.get(i)}')
        
def quit():
    print(('Продолжить поиск?\n'
           '"y" или "n"'))
    choice = input('>> ')
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        quit()