## Задание написать программу учёта работников предприятия.

1. files_editor.py отвечает за работу с файлами (json,csv)
2. id_numbmer.py отвечает за проверку существующих id, присвоение уникального id и сохранение в файл id_workers.json.
3. logger.py отвечает за логирование, в данный момент не подключен.
4. menu.py отвечает за основную логику работы приложения, в дальнейшем все функции не относящиеся к меню будут разнесены в другие модули.
5. main.py главный файл запуска.
6. Папка data_files содержит: 

                          * id_to_name.json хранит связь id к name (Имени)
                          * id_workers.json хранит список присвоенных id
                          * table_workers.json хранит элементы всех работников
                          * table_workers.csv 
