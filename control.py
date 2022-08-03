import json


def save_d(arg):
    with open('table_workers.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))

def save2(arg):
    with open('table_workers.csv', 'a', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))

def load_d():
    with open('table_workers.json', 'r+', encoding='utf-8') as file:
        table = json.load(file)
        print(type(table))

load_d()


