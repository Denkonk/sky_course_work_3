import json
import datetime

file_path = r'C:\Programm\Programm\Python\python_kurs_3\data\operations.json'
def load_json_data(file_path):
    """
    Загружает данные из файла JSON
    """
    with open(file_path, "r", encoding='utf-8') as json_file:
        data_json = json.load(json_file)
        return data_json

def filter_operations(operations):
    """
    Фильтрует операции по ключу "state", у которых значение "EXECUTED"
    """
    executed_operations = [operation for operation in operations if operation.get('state') == 'EXECUTED']
    return executed_operations

def sorted_operations(transactions):
    """
    Сортирует транзакции по дате, от самых новых к самым старым.
    """
    sorted_transactions = sorted(transactions, key=lambda x: datetime.datetime.fromisoformat(x['date']), reverse=True)
    return sorted_transactions


#print(filter_operations(load_json_data(file_path)))
#print(sorted_operations(filter_operations(load_json_data(file_path))))
#print(datetime.datetime.fromisoformat("2018-12-24T20:16:18.819037"))








