import json
import logging as log
import datetime

now = datetime.datetime.now()

log.basicConfig(level=log.DEBUG,
                filename="WORKERS_LOG.log",
                encoding='utf-8')

def save_json(arg, file_json=r"data_files\table_workers.json"):
    with open(f'{file_json}', 'w', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))
        log.debug(f'{now}: Save to {file_json} complete!')
        


def save_csv(arg, file_csv=r'data_files\table_workers.json'):
    with open(f'{file_csv}', 'a', encoding='utf-8') as file:
        file.write(json.dumps(arg, ensure_ascii=False))


def load_json(file_json=r'data_files\table_workers.json'):
    with open(f'{file_json}', 'r', encoding='utf-8') as file:
        item = json.load(file)
        log.debug(f'{now}: Load from {file_json} complete!')
        return item
