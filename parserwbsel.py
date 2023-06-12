from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import random, json
from loguru import logger
from selenium.webdriver.common.keys import Keys
from bsparser import BsParser
from utils import (checking_exist_path_and_create_if_not,
                   save_json_and_create_csv,
                   first_start,
                   DataFromInput)
from trans import Trans
# from paths import DRIVER_CHROME_PATH
from paths import PATH_HTML_PAGES, FILE_DICT_FOR_SEARCH_ARTICLE


@logger.catch()
def get_data(cities:list, search_goods:list, count_pages=3, search_article:int=None) -> None:

    first_start()
    # driver = webdriver.Chrome(executable_path=DRIVER_CHROME_PATH)
    
    # options for Docker
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--start-maximized')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    # options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}
    # options.add_argument("--disable-setuid-sandbox")
    
    driver = webdriver.Chrome(options=options)

    sleep(0.5)

    url = 'https://www.wildberries.ru/'
    driver.get(url=url)
    driver.maximize_window()
    sleep(3)

    basic_goods_info = []

    if search_article:
        dict_for_search_article = {}
    
    for city in cities:
        print(f'Посик ПВЗ для {city}...')
    
        button_city = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/ul/li[2]/span')
        button_city.click()
        sleep(5)

        search_pvz_form = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div[1]/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[1]/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps/ymaps[1]/ymaps/ymaps[1]/ymaps[1]/input')
        for letter_city in str(city):
            search_pvz_form.send_keys(letter_city)
            sleep(0.2)
        sleep(2)
        search_pvz_form.send_keys(Keys.RETURN)
        sleep(2)
        
        try:
            list_of_cities = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div[1]/ymaps/ymaps/ymaps/ymaps[4]/ymaps[1]/ymaps[1]/ymaps/ymaps[1]/ymaps/ymaps/ymaps/ymaps/ymaps[2]/ymaps/ymaps/ymaps[2]/ymaps/ymaps/ymaps[1]/ymaps/ymaps')
            if list_of_cities.is_displayed():
                list_of_cities.click()
        except Exception:
            pass
                
        sleep(3)

        random_pvz_index = random.choice([1, 2, 3, 4, 5])
        button_random_pvz = driver.find_element(By.XPATH, f'//*[@id="pooList"]/div[{random_pvz_index}]')
        button_random_pvz.click()
        sleep(2)

        button_choise_pvz = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/div[3]/button')
        button_choise_pvz.click()
        print(f'ПВЗ выбран.')
        sleep(2)

        if search_article:
            goods_dict = {}
        
        for goods in search_goods:
            print(f'Скрапинг товара "{goods}"...')

            search_form = driver.find_element(By.XPATH, '//*[@id="searchInput"]')
            search_form.send_keys(Keys.CONTROL, "a")
            sleep(0.5)
            search_form.send_keys(Keys.DELETE)
            for symbol in goods:
                search_form.send_keys(symbol)
                sleep(0.1)
            search_form.send_keys(Keys.RETURN)
            sleep(3)
            
            if search_article:
                page_dict = {}

            for page_number in range(count_pages):

                key_current_page_number = 'page' + str(page_number + 1)

                speed=5
                current_scroll_position, new_height = 0, 1
                while current_scroll_position <= new_height:
                    current_scroll_position += speed
                    driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
                    new_height = driver.execute_script("return document.body.scrollHeight")

                page_source = driver.page_source

                city_path, search_goods_path = Trans(list_text=[city, goods]).from_ru_to_en()
                list_paths = [f'{PATH_HTML_PAGES}\\{city_path}',
                             f'{PATH_HTML_PAGES}\\{city_path}\\{search_goods_path}']
                
                checking_exist_path_and_create_if_not(list_paths=list_paths)

                with open(f'{PATH_HTML_PAGES}\\{city_path}\\{search_goods_path}\\page_{page_number + 1}.html', 'w', encoding='utf-8') as file:
                    file.write(page_source)
                
                temp_basic_goods_info, current_page = BsParser().basic_parser(html_data=page_source,
                                                                page_number=page_number + 1,
                                                                city=city,
                                                                search_goods=goods,
                                                                search_article=search_article)
                
                basic_goods_info += temp_basic_goods_info

                # get dict of article(key) and product brand name(value) on current page
                if current_page:
                    page_dict[key_current_page_number] = current_page
                    
                if page_number + 1 == count_pages:
                    print(f'Поиск товара "{goods}" в городе {city} завершен.\n')
                    break

                botton_next_page = driver.find_element(By.XPATH, "// a[contains(text(),\'Следующая страница')]")
                botton_next_page.click()
                print(f'Переход на страницу № {page_number + 2}\n')

                sleep(2)

            # get dict of search_goods(key) and prev dict(value)
            if search_article:
                goods_dict[goods] = page_dict

        # get dict of city(key) and prev dict(value)
        if search_article:
            dict_for_search_article[city] = goods_dict
    
    driver.close()
    driver.quit()

    if search_article:
        with open(FILE_DICT_FOR_SEARCH_ARTICLE, 'w', encoding='utf-8') as file:
            json.dump(dict_for_search_article, file, indent=4, ensure_ascii=False)

    save_json_and_create_csv(basic_goods_info)


def main():
    logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='100 KB', compression='zip')

    # get_data(cities=['Волгоград', 'Самара'],
    #          search_goods=['Куртка', 'Джинсы'],
    #          count_pages=2,
    #          search_article=79774695)

    # data_input = DataFromInput().run_all_inputs()
    # get_data(cities=data_input['cities'],
    #          search_goods=data_input['search_goods'],
    #          count_pages=int(data_input['count_pages'][0]))
    pass


if __name__ == '__main__':
    main()
