from paths import FILE_DICT_FOR_SEARCH_ARTICLE
import json
from utils import DataFromInput
from parserwbsel import get_data


class GetPage:

    def __init__(self,
                 search_goods:str,
                 cities:list,
                 count_pages=3,
                 search_article:str=None) -> None:
        
        self.search_article = search_article
        self.search_goods = search_goods
        self.product_brand_name = 'not found'
        self.cities = cities
        self.count_pages = count_pages

        self.message = f'\nПозиция в поиске по запросу: {self.search_goods[0]}\nТовар: {self.search_article}, '


    def get_page_from_json(self) -> None:

        get_data(cities=self.cities,
                 search_goods=self.search_goods,
                 count_pages=self.count_pages,
                 search_article=self.search_article)

        with open(FILE_DICT_FOR_SEARCH_ARTICLE, 'r', encoding='utf-8') as file:
            dict_for_search_article = json.load(file)

            for city in self.cities:
                city_true = False
                for goods in self.search_goods:
                    for page_number in range(self.count_pages):

                        page = 'page' + f'{page_number + 1}'
                        article_and_brand_name = dict_for_search_article[city][goods][page]

                        for position_on_page, key_value in enumerate(article_and_brand_name.items()):
                            if self.search_article == key_value[0]:
                                city_true = True
                                if key_value[1] in self.message:
                                    pass
                                else:
                                    self.message += key_value[1] + '\n'
                                self.message += f'\n{city}: {page_number + 1} страница, {position_on_page + 1} место'

                if not city_true:
                    self.message += f'\n{city}: нет на первых {self.count_pages} страницах'

            return self.message
                            

def main():
    # p = GetPage(cities=['Самара', 'Волгоград'],
    #             search_goods=['Куртка'],
    #             count_pages=2,
    #             search_article='1575327275')
    # print(p.get_page_from_json())

    data_input = DataFromInput().run_all_inputs_for_get_page()
    p = GetPage(cities=data_input['cities'],
                search_goods=data_input['search_goods'],
                count_pages=int(data_input['count_pages'][0]),
                search_article=int(data_input['search_article'][0]))
    p = p.get_page_from_json()
    print(p)

    pass


if __name__ == '__main__':
    main()