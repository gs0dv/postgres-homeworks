import csv


def load_data_from_cvs_file(path):
    """Возвращает список данных, загруженных из файла .csv"""
    with open(path, 'r', encoding='utf-8') as csv_file:
        data_list = []
        data = csv.reader(csv_file)

        i = True
        for item in data:
            if i:
                i = False
                continue
            data_list.append(tuple(item))

        return data_list


def insert_data_in_table_db(connect, name_table, data):
    """Добавляет данные в таблицу базы данных"""
    if not data:
        print(f'Данные в таблицу {name_table} не удалось загрузить')
        return

    conn = connect

    items = '(' + ''.join('%s,' * len(data[0]))[:-1] + ')'

    with conn.cursor() as cur:
        cur.executemany(f'INSERT INTO {name_table} VALUES {items}', data)
    print(f'Данные в таблицу {name_table} успешно добавлены!')
