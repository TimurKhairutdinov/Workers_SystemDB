import json
import id_number as id
import files_editor as fe


def menu_admin():
    print('Введите пароль: ')


def menu_user():
    print('База данных предприятия')
    choice = input(
        'Для управления, введите номер пункта меню.\n'
        '1. Добавить. \n'
        '2. Поиск. \n'
        '3. Изменить. \n'
        '4. Удалить.\n'
        '5. Показать список работников\n'
        '>> ')
    
    match choice:
        case '1': add_contact(), log.debug("Это сообщение для отладки программы")
        case '2': print(find_contact())
        case '3': edit_contact()
        case '4': del_contact()
        case '5': view_workers()

# Добавление нового работника
def add_contact():
    global id_number, name, type_doc, number_tel, department, type_worker, comment, all_workers
    
    name = input('Введите Имя Фамилию >> ')
    type_doc = input('Введите тип документа >> ')
    number_tel = input('Введите номер телефона >> ')
    department = input('Введите отдел >> ')
    type_worker = input('Введите должность >> ')
    comment = input('Введите комментарий >> ')
    id_number = id.set_id() 

    worker = {'id_number': id_number, 'type_doc': type_doc,
               'number_tel': number_tel, 'department': department,
               'type_worker': type_worker, 'comment': comment}
    
    id_to_name = fe.load_json('data_files\id_to_name.json')
    
    # Привязка id к name
    id_to_name[id_number] = name
    fe.save_json(id_to_name,'data_files\id_to_name.json')
    all_workers = fe.load_json()
    
    # Сохранение работника в базу
    all_workers[name] = worker
    fe.save_json(all_workers)


def del_contact():
    contact = find_contact() # tuple (name or id, contact, flag) 3 Элемента
    all_workers = fe.load_json()
    id_to_name = fe.load_json('data_files\id_to_name.json')
    
    name = contact[0]
    worker = all_workers.get(name)  
    id = worker.get('id_number')
    
    id_to_name.pop(f'{id}')
    all_workers.pop(f'{name}')
    
    fe.save_json(id_to_name,'data_files\id_to_name.json')
    fe.save_json(all_workers)
    
    print(f'Удалён: {contact}')
    
# Функция изменения контакта: Контакт полностью перезаписывается и сохраняется как новый,
# но сохраняя уникальный id. Старые данные полностью удаляются.
# Из-за особенности работы со словарем изменение данных возможно, только при использовании ключа name,
# Что не даёт изменить сам ключ name - Имя Фамилия
def edit_contact():
    contact = find_contact()
    all_workers = fe.load_json()
    id_to_name = fe.load_json('data_files\id_to_name.json') 
    
    # contact это кортеж, элемент[0] Содержит переменную name Имя работника
    name = contact[0]
    worker = all_workers.get(name)
    new_name = input(f'Изменить Имя Фамилию: {name} : >> ')
    type_doc = input(f'Изменить тип документа: {worker.get("type_doc")} : >> ')
    number_tel = input(f'Изменить номер телефона: {worker.get("number_tel")} : >> ')
    department = input(f'Изменить отдел: {worker.get("department")} : >> ')
    type_worker = input(f'Изменить должность: {worker.get("type_worker")} : >> ')
    comment = input(f'Изменить комментарий: {worker.get("comment")} : >> ')
    id_number = worker.get('id_number')
    
    new_worker = {'id_number': id_number, 'type_doc': type_doc,
               'number_tel': number_tel, 'department': department,
               'type_worker': type_worker, 'comment': comment}
    
    all_workers.pop(name)
    all_workers[f'{new_name}'] = new_worker
    id_to_name[f'{worker.get("id_number")}'] = new_name
    
    fe.save_json(all_workers)
    fe.save_json(id_to_name, 'data_files\id_to_name.json')
    print(f'Изменения внесены: {(new_name, worker)}')
    
# Поиск работника по id или Имя Фамилии
# Возвращает кортеж из: Имени, данных работника, флага
def find_contact():
    finder = init_find()
    if finder.isdigit():
        id_to_name = fe.load_json('data_files\id_to_name.json')
        name = id_to_name.get(finder)
        all_workers = fe.load_json()
        # Если в словаре отсутствует ключ name
        if name is None:
            print('Пользователь не найден')
            if stop_prog():
                find_contact()
            else:
                exit()
        else:
            flag = 1
            return (name, all_workers.get(name), flag)
            
        
    else:
        all_workers = fe.load_json()
        
        # Если в словаре отсутствует ключ id
        if all_workers.get(finder) is None:
            print('Пользователь не найден')
            if stop_prog():
                find_contact()
            else:
                exit()
        else:
            flag = 0
            return (finder, all_workers.get(finder), flag)
        
        
# Просто ввод отдельной функцией
def init_find():
    print('Введите Имя Фамилию или "id"')
    msg = input('>> ')
    return msg
    
def view_workers():
    dict = fe.load_json('data_files\id_to_name.json')
    for i in dict.keys():
        print(f'{i}: {dict.get(i)}')
        
def stop_prog():
    print(('Продолжить?\n'
           '"y" или "n"'))
    choice = input('>> ')
    if choice == "y":
        return True
    elif choice == "n":
        return False
    else:
        stop_prog()
