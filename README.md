# Содержание

1. [Аннотация](#аннотация)
2. [Установка](#установка)  
2.1. [Скрипт](#скрипт_2)  
2.2. [.exe - временнно недоступно](#exe_2)  
3. [Запуск](#запуск)  
3.1. [Скрипт](#скрипт_3)  
3.1.1. [Input](#input)  
3.1.2. [parserwbsel.py](#parserwbsel)  
3.2. [.exe - временно недоступно](#exe_3)  
4. [Данные HTML и bs4](#html_data)
5. [Logger](#logger)  
6. [Разработчик](#developer)

## <a name='аннотация'>1. Аннотация</a>

[ParserSelWB](#https://github.com/imartov/ParserSelWB.git) - это парсер для https://www.wildberries.ru/, разработанный на базе Python + Selenium, который возвращает файл <b>result.csv</b> с содержащимися в нем следующими данными:
- искомый товар (запрос поиска);
- город (пункт выдачи товаров);
- время добавления записи;
- номер страницы;
- позиция на странице;
- имя бренда товара (резальтата поиска);
- стоимость товара со скодикой;
- стоимость товара без скидки;
- артикул товара;
- количество отзывов;
- рейтинг (количество звезд).

## <a name='установка'>2. Установка</a>

Установить и использовать <b>ParserSelWB</b> можно двумя способами:  
### <a name='скрипт_2'>2.1. Скрипт</a>
Для запуска <b>ParserSelWB</b> из-под среды разработки необходимо выполнить следующие шаги:  
1. Установить последнюю стабильную версию Python по ссылке: https://www.python.org/downloads/
2. Установить Git по ссылке https://git-scm.com/downloads
3. Клонировать репозиторий, выполнив команду (для Windows):
    ```python
    $ git clone https://github.com/imartov/ParserSelWB.git
    ```
4. Создать виртуальное окружение, выполнив команду:
    ```python
    $ python -m venv your_name_venv
    ```
5. Активировать виртуальное окружение, выполнив команду:
    ```python
    $ cd your_name_venv\Scripts\activate
    ```
6. Установить зависимости, выполнив команду:
    ```python
    $ pip install -r requirements.txt
    ```
7. Установите и распакуйте драйвер [chromedriver.exe](https://chromedriver.chromium.org/downloads), соответствующий версии Вашего Chrome.

Структура проекта должна выглядеть следующим образом:
![image](https://github.com/imartov/ParserSelWB/assets/116018998/e0146bf9-60d7-4ffe-b000-5998622c0aaa)

### <a name='exe_2'>2.2. .exe - временно недоступно</a>
Установите исполняемый файл <b>[ParserSelWB.exe](https://github.com/imartov/ParserSelWB/blob/main/ParserSelWB.exe)</b> на устройство и пользуйтесь, как обычным приложением.

## <a name='запуск'>3. Запуск</a>

В зависимости от предпочитаемого Вами способа использования <b>[ParserSelWB](https://github.com/imartov/ParserSelWB.git)</b> запустить его можно соответствующими способами.

### <a name='скрипт_3'>3.1. Скрипт</a>
#### <a name='input'>3.1.1. Input</a>
Для запуска <b>[ParserSelWB](https://github.com/imartov/ParserSelWB.git)</b> и введения необходимых для парсинга данных в объект <b>input</b> запустите <b>parserwbsel.py</b>, выполнив команду:
```py
$ your_local_repository\python parserwbsel.py
```
#### <a name='parserwbsel'>3.1.2. parserwbsel.py</a>
С помощью редактора, поддерживающего Python (например, [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) или [VS Code](https://code.visualstudio.com/download)) перейдитите в <b>[parserwbsel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> и замените функцию <b>main()</b> на следующую:  

```python
def main():
    logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', rotation='100 KB', compression='zip')

    get_data(cities=['Волгоград', 'Самара'],
             search_goods=['Шапка', 'Куртка'],
             count_pages=2)

    # data_input = DataFromInput().run_all_inputs()
    # get_data(cities=data_input['cities'],
    #          search_goods=data_input['search_goods'],
    #          count_pages=int(data_input['count_pages'][0]))
    pass
```
Измените параметры на необходимые Вам данные:
- cities;
- search_goods;
- count_pages.

### <a name='exe_3'>3.2. .exe - временно недоступно</a>

Запустите <b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> как обычное приложение, после чего введите в терминал необходимые данные для поиска.

## <a name='html_data'>4. Данные HTML и bs4</a>

При первом запуске <b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> на локальном репозитории будут созданы следующие директории: "data"/"html", в которые будут помещаться получаемые данные. В папке "html" будут находиться объекты <b>"page_source"</b> каждой страницы в виде файлов html. В "data" будет помещаться <b>result.csv</b>, а также <b>basic_goods_info.json</b> для взаимодействия с другими приложениями.  
Поскольку данные html-страниц сохраняются, Вы можете повторно к ним обратиться, переопределив и собрав иную информацию о товаре, не прибегая к <b>Selenium</b>. Для этого необходимо выполнять функцию <b>get_data_from_files()</b> в <b>[parserwbsel.py](https://github.com/imartov/ParserSelWB/blob/main/bsparser.py)</b>, создав соответствующий экземпляр класса.

## <a name='logger'>5. Logger</a>

<b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> дополнен средствами логирования, позволяющими удобно и быстро отслеживать исключения и ошибки. При преждевременном прекращении <b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> в локальном дериктории проекта будет создан файл <b>debug.log</b>, в котором будет содержаться подробная информация о возникшем исключении.

## <a name='developer'>6. Разработчик</a>

- Телеграм: @alr_ks (прямая ссылка: https://t.me/alr_ks)
- Почта: alexandr.kosyrew@mail.ru


