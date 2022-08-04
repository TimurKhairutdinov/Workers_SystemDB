import json

import files_editor as fe


def get_id():
    global id_numbers
    id_numbers = fe.load_json('data_files\id_workers.json')
    for i in range(1, 10000):
        if id_numbers.count(i) == 0:
            return i


def set_id():
    global id_worker
    id_worker = get_id()
    save_id(id_worker)
    return id_worker


def save_id(id):
    id_numbers.append(id)
    fe.save_json(id_numbers, 'data_files\id_workers.json')
