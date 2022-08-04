import json


def save_json(arg, file_json=r"data_files\table_workers.json"):
    with open(f'{file_json}', 'w', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))


def save_csv(arg, file_csv=r'data_files\table_workers.json'):
    with open(f'{file_csv}', 'a', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))


def load_json(file_json=r'data_files\table_workers.json'):
    with open(f'{file_json}', 'r', encoding='utf-8') as file:
        table = json.load(file)
        return table
