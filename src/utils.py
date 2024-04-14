import json

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

print(filter_operations(load_json_data(file_path)))








