from bs4 import BeautifulSoup
from time import strftime, localtime
from loguru import logger
import os, json
from utils import save_json_and_create_csv
from trans import Trans
from convertnumber import ConvertNumber
from paths import PATH_HTML_PAGES, FILE_ALL_GOODS_JSON


class BsParser:
    def __init__(self) -> None:
        self.basic_goods_info = []

    def basic_parser(self, html_data:str, page_number:int, city:str, search_goods:str, search_article:int=None) -> dict:
        soup = BeautifulSoup(html_data, 'lxml')
        all_cards_goods = soup.find_all('div', class_='product-card__wrapper')
        
        if search_article:
            current_page = 'page' + str(page_number)
            current_page = {}

        for position_on_page, goods_card in enumerate(all_cards_goods, start=1):

            added_time = strftime('%d.%m.%Y %H:%M:%S', localtime())

            brand_name = goods_card.find('h2', {'class': 'product-card__brand-wrap'}).find('span', {'class': 'product-card__brand'}).text
            product_name = goods_card.find('h2', {'class': 'product-card__brand-wrap'}).find('span', {'class': 'product-card__name'}).text.replace(' / ', '')
            product_brand_name = brand_name + ' | ' + product_name

            price_no_sale = str(goods_card.find('p', {'class': 'product-card__price price'}).find('del'))
            price_no_sale = ConvertNumber(price_no_sale).convert_price_to_float()
            if price_no_sale == 'None':
                price_no_sale = str(goods_card.find('span', {'class': 'price__lower-price'}).text)
                price_no_sale = ConvertNumber(price_no_sale).convert_price_to_float()

            price_sale = str(goods_card.find('p', {'class': 'product-card__price price'}).find('ins', {'class': 'price__lower-price'}))
            price_sale = ConvertNumber(price_sale).convert_price_to_float()
            if price_sale == 'None':
                price_sale = str(goods_card.find('span', {'class': 'price__lower-price'}).text)
                price_sale = ConvertNumber(price_sale).convert_price_to_float()
            
            article = str(goods_card.find('a', {'class': 'product-card__link j-card-link j-open-full-product-card'}).get('href'))
            article = ConvertNumber(article).convert_href_to_int_and_get_article()
            
            try:
                count_review = goods_card.find('p', {'class': 'product-card__rating-wrap'}).find('span').get('class')
                count_review = int(count_review[-1][-1])
            except Exception:
                count_review = 0
            
            try:
                count_stars = str(goods_card.find('span', {'class': 'product-card__count'}).text)
                count_stars = ConvertNumber(count_stars).convert_review_to_int()
            except Exception:
                count_stars = 0

            self.basic_goods_info.append(
                {
                    'search_goods': search_goods,
                    'city': city,
                    'added_time': added_time,
                    'page_number': page_number,
                    'position_on_page': position_on_page,
                    'product_brand_name': product_brand_name,
                    'price_sale': price_sale,
                    'price_no_sale': price_no_sale,
                    'article': article,
                    'count_review': count_review,
                    'count_stars': count_stars
                }
            )

            if search_article:
                current_page[article] = product_brand_name

        if search_article:
            return self.basic_goods_info, current_page
        else:    
            return self.basic_goods_info, None
    

    @logger.catch()
    def get_data_from_files(self, search_article:int=None) -> None:
        basic_goods_info = []
        for folder_city in os.listdir(PATH_HTML_PAGES):
            for folder_search_goods in os.listdir(f'{PATH_HTML_PAGES}\\{folder_city}'):
                city, search_goods = Trans([folder_city, folder_search_goods]).from_en_to_ru()
                
                for page in os.listdir(f'{PATH_HTML_PAGES}\\{folder_city}\\{folder_search_goods}'):
                    page_number = int(str(page).split('.')[0][-1])

                    with open(f'{PATH_HTML_PAGES}\\{folder_city}\\{folder_search_goods}\\{page}', 'r', encoding='utf-8') as file_html:
                        page_source = file_html.read()

                    basic_goods_info += self.basic_parser(html_data=page_source,
                                                          page_number=page_number,
                                                          city=city,
                                                          search_goods=search_goods,
                                                          search_article=search_article)
        
        save_json_and_create_csv(basic_goods_info)


def main():
    logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='100 KB', compression='zip')
    # p = BsParser().get_data_from_files()
    pass


if __name__ == '__main__':
    main()
