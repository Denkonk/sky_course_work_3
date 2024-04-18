import json
import datetime
import os

file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')

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
    Сортирует транзакции по дате, от самых новых к самым старым
    """
    sorted_transactions = sorted(transactions, key=lambda x: datetime.datetime.fromisoformat(x['date']), reverse=True)
    return sorted_transactions

def get_first_5_trans(transactions):
    """
    Получает первые 5 транзакций из списка операций
    """
    first_5_transactions = transactions[:5]
    return first_5_transactions

def get_data_trans(transactions):
    """
    Перевода даты в формат ДД.ММ.ГГГГ
    """
    date_parts = transactions['date'].split('T')[0].split('-')
    date_result = f"{date_parts[2]}.{date_parts[1]}.{date_parts[0]}"
    return date_result

def mask_number_from_to(number_card):
    """
    Разделение и шифрование номера карты и счета
    """
    #number_card = 'счет 37664464522387841234'
    #number_card = number_card[number]
    last_space_index = number_card.rindex(' ')
    first_part = number_card[:last_space_index]
    second_part = number_card[last_space_index + 1:]
    if len(second_part) == 16:
        second_part_result = second_part[0:4] + ' ' + second_part[4:6] + '** **** ' + second_part[-4:]
    elif len(second_part) == 20:
        second_part_result = '**' + second_part[-4:]
    else:
        second_part_result = second_part
    return f"{first_part} {second_part_result}"

def get_amount(transactions):
    """
    Получение суммы и валюты транзакции
    """
    transaction_description = transactions['operationAmount']['amount']
    transaction_name = transactions['operationAmount']['currency']['name']
    return f'{transaction_description} {transaction_name}'







# transaction_first_5 = get_first_5_trans(sorted_operations(filter_operations(load_json_data(file_path))))
#
# print(transaction_first_5)

#
# dates = [get_data_trans(transaction) for transaction in transaction_first_5]
#
# print(dates)

# for transactions in transaction_first_5:
# #     print(mask_number_from_to(number_card['from']))
#
#     print(get_amount(transactions))


#print(filter_operations(load_json_data(file_path)))
#print(sorted_operations(filter_operations(load_json_data(file_path))))
#print(get_first_5_trans(sorted_operations(filter_operations(load_json_data(file_path)))))
#print(get_data_trans(get_first_5_trans(sorted_operations(filter_operations(load_json_data(file_path))))))
#print(datetime.datetime.fromisoformat("2018-12-24T20:16:18.819037"))








