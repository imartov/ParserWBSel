import csv, os, json, time
from paths import RESULT_CSV, FILE_ALL_GOODS_JSON


class DataFromInput:
    
    def __init__(self) -> None:
        self.input_data_dict = {}
        
    def input_data_for_list(self, query:str, example:str, key_dict:str) -> None:
        
        print(f'\nEnter a list of {query} separated by commas and spaces.\nFor example "{example}"\n')
        input_data = input('Here: ')

        input_data = input_data.split(',')
        data_list = []
        if len(input_data) > 1:
            for data in input_data:
                data = data.strip()
                if data:
                    data_list.append(data)
        else:
            data_list.append(input_data[0])

        self.input_data_dict[key_dict] = data_list

        
    def input_city(self) -> None:
        query = 'cities'
        example = 'Moscow, Volgograd'
        key_dict = 'cities'

        self.input_data_for_list(query=query, example=example, key_dict=key_dict)


    def input_search_goods(self) -> None:
        query = 'searched goods'
        example = 'Jeans, Jacket'
        key_dict = 'search_goods'

        self.input_data_for_list(query, example, key_dict)


    def input_page_number(self) -> None:
        query = 'pages count for ever searched goods'
        example = '3'
        key_dict = 'count_pages'

        self.input_data_for_list(query, example, key_dict)


    def run_all_inputs(self) -> dict:
        self.input_city()
        self.input_search_goods()
        self.input_page_number()

        return self.input_data_dict


def save_json_and_create_csv(basic_goods_info:dict) -> None:

    with open(FILE_ALL_GOODS_JSON, 'w', encoding='utf-8') as file:
        json.dump(basic_goods_info, file, indent=4, ensure_ascii=False)
    
    with open(RESULT_CSV, 'w', encoding='utf-8', newline='') as file_csv:
        writer = csv.writer(file_csv)

        for index, product in enumerate(basic_goods_info):
            if index == 0:
                table_headers = list(product.keys())
                table_row = list(product.values())
                writer.writerow(table_headers)
                writer.writerow(table_row)
            
            elif index > 0:
                table_row = list(product.values())
                writer.writerow(table_row)


def checking_exist_path_and_create_if_not(list_paths:str) -> None:
    for path in list_paths:
        if not os.path.exists(path):
            os.mkdir(path)


def first_start() -> None:
    checking_exist_path_and_create_if_not(['data', 'data\\html'])


def main():
    pass


if __name__ == '__main__':
    main()


# exe_app 0e08eac
