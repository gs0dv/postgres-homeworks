"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

from utils.utils import load_data_from_cvs_file, insert_data_in_table_db

path_to_customers_data = 'north_data/customers_data.csv'
path_to_employees_data = 'north_data/employees_data.csv'
path_to_orders_data = 'north_data/orders_data.csv'

try:
    customers_data = load_data_from_cvs_file(path_to_customers_data)
except FileNotFoundError:
    print('Файл не найден')
    customers_data = None

try:
    employees_data = load_data_from_cvs_file(path_to_employees_data)
except FileNotFoundError:
    print('Файл не найден')
    employees_data = None

try:
    orders_data = load_data_from_cvs_file(path_to_orders_data)
except FileNotFoundError:
    print('Файл не найден')
    orders_data = None

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)

try:
    with conn:
        insert_data_in_table_db(conn, 'customers', customers_data)
        insert_data_in_table_db(conn, 'employees', employees_data)
        insert_data_in_table_db(conn, 'orders', orders_data)
finally:
    conn.close()
