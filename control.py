import json


def add_worker():
    global name, comment, number_tel, type_doc, type_worker, id_number,department
    id_number = input('Введите номер сотрудника >> ')
    name = input('Введите Имя Фамилию >> ')
    type_doc = input('Введите тип документа >> ')
    number_tel = input('Введите номер телефона >> ')
    department = input('Введите одтел >> ')
    type_worker = input('Введите доджность >> ')
    comment = input('Введите комментарий >> ')


def init_data():
    add_worker()
    global data_worker
    data = [id_number,name,type_doc,number_tel,department,type_worker,comment]
    data_worker = {}
    data_worker[name] = data
    return data_worker


def save_data_workers():
    
    with open('workers.json', 'a', encoding = 'utf-8') as workers:
        workers.write(json.dumps(init_data(), ensure_ascii=False))
        print('Save')


def save_data_json():
    with open('book.json', 'a', encoding='utf-8') as telephon_book:
        telephon_book.write(json.dumps(init_data(), ensure_ascii=False))


def load_data_json():
    with open('workers.json', 'r', encoding='utf-8') as telephon_book:
        data_from_telephon_book = json.load(telephon_book)
        return data_from_telephon_book
