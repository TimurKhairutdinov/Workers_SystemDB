from curses.ascii import isdigit
import id_number as id
import json
def menu_admin():
    print('Введите пароль: ')


def menu_user():
    print('База данных')
    choice = input(
        'Для работы, введите номер пункта меню.\n'
        '1. Добавить. \n'
        '2. Поиск. \n'
        '3. Изменить. \n'
        '>> ')
    
    match choice:
        case 1: add_contact()
        case 2: find_contact()
        case 3: del_contact()


def add_contact():
    global id_number,name,type_doc, number_tel, department, type_worker, comment, all_workers
    
    id_number = id.set_id()
    name = input('Введите Имя Фамилию >> ')
    type_doc = input('Введите тип документа >> ')
    number_tel = input('Введите номер телефона >> ')
    department = input('Введите одтел >> ')
    type_worker = input('Введите доджность >> ')
    comment = input('Введите комментарий >> ')

    worker = [{'id_number' : id_number,'type_doc':type_doc,
               'number_tel':number_tel,'department':department,
               'type_worker':type_worker,'comment':comment}]
    
    all_workers = load_json()
    all_workers[name] = worker
    save_json(all_workers)


def del_contact():
    print('Введите Имя Фамилию, если вы хотите удалить по id, введите "id"')
    name = input('>> ')
    all_workers = load_json()
    all_workers.pop(name)
    save_json(all_workers)
    
    
def edit_contact():
    return 0

def find_contact():
    finder = init_find()
    all_workers = load_json()
    if finder == str:
        all_workers.pop(name)
    else:
        lst = all_workers.get(name)
        

def save_json(arg):
    with open('table_workers.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))

def save_csv(arg):
    with open('table_workers.csv', 'a', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))

def load_json():
    with open('table_workers.json', 'r+', encoding='utf-8') as file:
        table = json.load(file)
        return table
    
def init_find():
    print('Введите Имя Фамилию или "id"')
    msg = str(input('>> '))
    if msg.isdigit():
        return int(msg)
    else:
        return msg
    
