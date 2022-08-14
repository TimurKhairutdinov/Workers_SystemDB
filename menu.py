import json
import math
import id_number as id
import files_editor as fe
import logging as log
import datetime

now = datetime.datetime.now()

log.basicConfig(level=log.DEBUG,
                filename="WORKERS_LOG.log",
                encoding='utf-8')


def menu_admin():
    print('Введите пароль: ')


def menu_user():
    log.debug(f' {now}: Запуск программы.')
    print('База данных предприятия')
    choice = input(
        'Для управления, введите номер пункта меню.\n'
        '1. Добавить. \n'
        '2. Поиск. \n'
        '3. Изменить. \n'
        '4. Удалить.\n'
        '5. Показать список работников\n'
        '6. Выход.\n'
        '>> ')
    
    log.debug(f' {now}: Ввод пользователем: {choice}')
    
    match choice:
        case '1': add_contact()
        case '2': print(find_contact())
        case '3': edit_contact() 
        case '4': del_contact()
        case '5': view_workers() 
        case '6': exit()
        
# Добавление нового работника
def add_contact():
    log.debug(f' {now}: add_contact: Добавление пользователя')
    
    global id_number, name, type_doc, number_tel, department, type_worker, comment, all_workers
    
    name = input('Введите Имя Фамилию >> ')
    type_doc = input('Введите тип документа >> ')
    number_tel = input('Введите номер телефона >> ')
    department = input('Введите отдел >> ')
    type_worker = input('Введите должность >> ')
    comment = worker_status(init_status(),name)
    
    id_number = id.set_id()
    
    log.debug(f' {now}: Ввод данных {[name, type_doc, number_tel, department, type_worker, comment, id_number]}')
    
    worker = {'id_number': id_number, 'type_doc': type_doc,
               'number_tel': number_tel, 'department': department,
               'type_worker': type_worker, 'comment': comment}
    
    id_to_name = fe.load_json('data_files\id_to_name.json')
    
    # Привязка id к name
    id_to_name[id_number] = name
    fe.save_json(id_to_name,'data_files\id_to_name.json')
    log.info(f' {now} Сохранение данных: {[name, id_number]} в data_files\id_to_name.json')
    
    # Сохранение работника в базу
    all_workers = fe.load_json()
    all_workers[name] = worker
    fe.save_json(all_workers)
    
    log.info(f' {now}: Дабавление контакта: {name} выполнено!')


def del_contact():
    log.debug(f' {now}: del_contact: удаление контакта.')
    contact = find_contact() # tuple (name or id, contact) 2 Элемента
    if contact != False:
        all_workers = fe.load_json()
        id_to_name = fe.load_json('data_files\id_to_name.json')
        
        name = contact[0]
        worker = all_workers.get(name)  
        id = worker.get('id_number')
        
        id_to_name.pop(f'{id}')
        all_workers.pop(f'{name}')
        log.warning(f' {now}: Удалён контакт: {id, name}!')
        
        fe.save_json(id_to_name,'data_files\id_to_name.json')
        fe.save_json(all_workers)
        
        print(f'Удалён: {contact}')
    else:
        print('Поиск завершен.')
        
        
# Функция изменения контакта: Контакт полностью перезаписывается и сохраняется как новый,
# но сохраняя уникальный id. Старые данные полностью удаляются.
# Из-за особенности работы со словарем изменение данных возможно, только при использовании ключа name,
# Что не даёт изменить сам ключ name - Имя Фамилия
def edit_contact():
    log.debug(f' {now}: edit_contact: изменение контакта.')
    
    contact = find_contact()
    if contact != False:
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
        comment = edit_worker_status(name, new_name)
        id_number = worker.get('id_number')
        
        new_worker = {'id_number': id_number, 'type_doc': type_doc,
                'number_tel': number_tel, 'department': department,
                'type_worker': type_worker, 'comment': comment}
        
        all_workers.pop(name)
        all_workers[f'{new_name}'] = new_worker
        id_to_name[f'{worker.get("id_number")}'] = new_name
        
        fe.save_json(all_workers)
        fe.save_json(id_to_name, 'data_files\id_to_name.json')
        
        log.warning(f' {now}: изменение данных id: {id_number} name: {name} внесены.')
        print(f'Изменения внесены: {(new_name, new_worker)}')
    else:
        print('Поиск завершен!')
        
        
# Поиск работника по id или Имя Фамилии
# Возвращает кортеж из: Имени, данных работника, флага
def find_contact():
    log.debug(f' {now}: find_contact: поиск контакта.')
    
    id_to_name = fe.load_json('data_files\id_to_name.json')
    all_workers = fe.load_json()
    
    quit_status = True
    while quit_status != False:
        finder = init_find()
        if finder.isdigit():
            if finder in id_to_name.keys():
                name = id_to_name.get(finder)
                log.info(f' {now}: Пользователь найден: id: {finder}, name: {name}')
                return (name, all_workers.get(name))
            else:
                log.info(f' {now} Пользователь не найден. id: {finder}')
                print('Пользователь не найден')
        else:
            if finder in all_workers.keys():
                log.info(f' {now}: Пользователь найден: name: {finder}')
                return (finder, all_workers.get(finder))
            else:
                log.info(f' {now} Пользователь не найден. name: {finder}')
                print('Пользователь не найден')
        if not stop_prog('поиск'): 
            quit_status = False
            return False
        
        
# Просто ввод отдельной функцией
def init_find():
    print('Введите Имя Фамилию или "id"')
    msg = input('>> ')
    return msg
    
def view_workers():
    dict = fe.load_json('data_files\id_to_name.json')
    for i in dict.keys():
        print(f'{i}: {dict.get(i)}')
        
def stop_prog(text):
    print((f'Продолжить {text}?\n'
           '"y" или "n"'))
    choice = input('>> ')
    if choice == "y":
        return True
    elif choice == "n":
        log.debug(f' {now}: Завершение работы.')
        return False
    else:
        stop_prog(text)
        
        
def edit_worker_status(name, new_name):
    all_workers = fe.load_json()
    worker = all_workers.get(name)
    
    print(f'Изменить комментарий: {worker.get("comment")} : >> ')
    
    job_status = init_status()
    statuses = fe.load_json('data_files\worker_status.json')
    
    for key in statuses:
        lst = statuses.get(key)
        if name in lst:
            lst.remove(name)
            transfer = statuses.get(job_status)
            transfer.append(new_name)
            statuses[job_status] = transfer
            fe.save_json(statuses,'data_files\worker_status.json')
            break
    return job_status
        
        
def worker_status(job_status,name):
    stats = fe.load_json('data_files\worker_status.json')
    stats[job_status].append(name)
    fe.save_json(stats,'data_files\worker_status.json')
    return job_status
    
def init_status():
    status = input('Выберите статус работника.\n'
                    '1. Больничный.\n'
                    '2. Отпуск.\n'
                    '3. Работает.\n'
                    '>> ')
    flag = True
    while flag != False:
        if status == "1": 
            flag = False
            return "hospital"
        elif status == "2": 
            flag = False
            return "vacation"
        elif status == "3": 
            flag = False
            return "works"
        else:
            print('Неккоректный ввод. \n'
                  'Повторите!')
