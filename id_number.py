import json

import files_editor as fe


def get_id():
    global id_numbers
    id_numbers = fe.load_json('data_files\id_workers.json')
    return id_numbers[-1]+ 1


def set_id():
    global id_worker
    id_worker = get_id()
    save_id(id_worker)
    return id_worker


def save_id(id):
    id_numbers.append(id)
    fe.save_json(id_numbers, 'data_files\id_workers.json')
