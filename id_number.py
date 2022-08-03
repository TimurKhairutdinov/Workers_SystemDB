import json


def get_id():
    global id_numbers
    id_numbers = load_id_json()
    for i in range(1, 10000):
        if id_numbers.count(i) == 0:
            return i


def set_id():
    global id_worker
    id_worker = get_id()
    return id_worker


def save_id(id):
    id_numbers.append(id)
    return id_numbers


def load_id_json():
    with open('id_workers.json', 'r', encoding='utf-8') as id_list:
        id = json.load(id_list)
        return id


def save_data_json():
    with open('id_workers.json', 'w', encoding='utf-8') as id_list:
        id_list.write(json.dumps(save_id(id_worker), ensure_ascii=False))
        


set_id()
save_data_json()