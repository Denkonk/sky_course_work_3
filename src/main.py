import utils
import os


file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')



transaction_first_5 = utils.get_first_5_trans(utils.sorted_operations(utils.filter_operations(utils.load_json_data(file_path))))

def get_main():
    for transactions in transaction_first_5:
        if transactions['description'] == 'Открытие вклада':
            print(f"{utils.get_data_trans(transactions)} {transactions['description']}\n"
                  f"{utils.mask_number_from_to(transactions['to'])}\n"
                  f"{utils.get_amount(transactions)}\n")
        else:
            print(f"{utils.get_data_trans(transactions)} {transactions['description']}\n"
                  f"{utils.mask_number_from_to(transactions['from'])} -> {utils.mask_number_from_to(transactions['to'])}\n"
                  f"{utils.get_amount(transactions)}\n")

get_main()
