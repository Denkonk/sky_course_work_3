# tests/test_utils.py
import json
from src import utils
import os

file_test_operations_1 = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_operations_1.json')
file_test_operations_2 = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_operations_2.json')
file_test_operations_3 = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_operations_3.json')
file_test_operations_4 = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_operations_4.json')

def test_load_json_data():
    """
    Тест загрузки файла
    """
    file_test_operations_1_verif = [
  {"id": 596171168,"state": "EXECUTED","date": "2018-07-11T02:26:18.671407",
  "operationAmount": {"amount": "79931.03","currency": {"name": "руб.","code": "RUB"}
  },"description": "Открытие вклада","to": "Счет 72082042523231456215"},
  {"id": 716496732,"state": "EXECUTED","date": "2018-04-04T17:33:34.701093",
  "operationAmount": {"amount": "40701.91","currency": {"name": "USD","code": "USD"}
  },"description": "Перевод организации","from": "Visa Gold 5999414228426353","to": "Счет 72731966109147704472"},
  {"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582",
  "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}
  }, "description": "Открытие вклада", "to": "Счет 90424923579946435907"}
]
    assert utils.load_json_data(file_test_operations_1) == file_test_operations_1_verif

def test_filter_operations():
    """
    Проверка что в filter_operations(operations) списке нету значений CANCELED
    """
    file_test_operations_2_verif = [
    {"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582",
     "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}
                         }, "description": "Открытие вклада", "to": "Счет 90424923579946435907"},
    {"id": 596171168, "state": "EXECUTED", "date": "2018-07-11T02:26:18.671407",
      "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}
                          }, "description": "Открытие вклада", "to": "Счет 72082042523231456215"
    }
  ]
    assert utils.filter_operations(utils.load_json_data(file_test_operations_2)) == file_test_operations_2_verif


def test_sorted_operations():
  """
  Тест сортировки файла по дате
  """
  file_test_operations_1_verif = [
    {"id": 863064926, "state": "EXECUTED", "date": "2019-12-08T22:46:21.935582",
     "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}
                         }, "description": "Открытие вклада", "to": "Счет 90424923579946435907"},
    {"id": 596171168, "state": "EXECUTED", "date": "2018-07-11T02:26:18.671407",
     "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}
                         }, "description": "Открытие вклада", "to": "Счет 72082042523231456215"},
    {"id": 716496732, "state": "EXECUTED", "date": "2018-04-04T17:33:34.701093",
     "operationAmount": {"amount": "40701.91", "currency": {"name": "USD", "code": "USD"}
                         }, "description": "Перевод организации", "from": "Visa Gold 5999414228426353",
     "to": "Счет 72731966109147704472"}
  ]
  assert utils.sorted_operations(utils.load_json_data(file_test_operations_1)) == file_test_operations_1_verif

def test_get_first_5_trans():
    """
    Тест выбора 5 транзакций
    """
    file_test_operations_3_verif = [
      {"id": 596171168,"state": "EXECUTED","date": "2018-07-11T02:26:18.671407",
        "operationAmount": {"amount": "79931.03","currency": {"name": "руб.","code": "RUB"}},
        "description": "Открытие вклада","to": "Счет 72082042523231456215"},
      {"id": 716496732,"state": "EXECUTED","date": "2018-04-04T17:33:34.701093",
        "operationAmount": {"amount": "40701.91","currency": {"name": "USD","code": "USD"}},
        "description": "Перевод организации","from": "Visa Gold 5999414228426353","to": "Счет 72731966109147704472"},
      {"id": 863064926,"state": "EXECUTED","date": "2019-12-08T22:46:21.935582",
        "operationAmount": {"amount": "41096.24","currency": {"name": "USD","code": "USD"}
        },
        "description": "Открытие вклада","to": "Счет 90424923579946435907"
      },
      {"id": 542678139,"state": "EXECUTED","date": "2018-10-14T22:27:25.205631",
        "operationAmount": {"amount": "90582.51","currency": {"name": "USD","code": "USD"}},
        "description": "Перевод организации","from": "Visa Platinum 2256483756542539","to": "Счет 78808375133947439319"},
      {"id": 558167602,"state": "EXECUTED","date": "2019-04-12T17:27:27.896421",
        "operationAmount": {"amount": "43861.89","currency": {"name": "USD","code": "USD"}},
        "description": "Перевод со счета на счет","from": "Счет 73654108430135874305","to": "Счет 89685546118890842412"}
    ]
    assert utils.get_first_5_trans(utils.load_json_data(file_test_operations_3)) == file_test_operations_3_verif

def test_get_data_trans():
    """
    Тест выбора и перевода даты
    """
    file_test_operations_4_verif = '11.07.2018'
    assert utils.get_data_trans(utils.load_json_data(file_test_operations_4)) == file_test_operations_4_verif

def test_mask_number_from_to():
    """
    Тест разделения и шифрования номера карты и счета
    """
    number_card_1 = "Visa Platinum 2256483756542539"
    assert utils.mask_number_from_to(number_card_1) == "Visa Platinum 2256 48** **** 2539"
    number_card_2 = "Счет 78808375133947439319"
    assert utils.mask_number_from_to(number_card_2) == "Счет **9319"







