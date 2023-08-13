# Content table

[Annotation](#anotation)  
[Get started](#get_started)  
[Scripts](#scripts)  
[.exe - temporarily unavailable](#exe_2)  
[Run](#run)  
[Script](#script)  
[Input](#input)  
[parserwbsel.py](#parserwbsel)  
[.exe - временно недоступно](#exe_3)  
[HTML data and bs4](#html_data)  
[Logger](#logger)  

## <a name='anotation'>Annotation</a>

[ParserSelWB](#https://github.com/imartov/ParserSelWB.git) - this parser for https://www.wildberries.ru/, observed on the basis of Python + Selenium, which returns the <b>result.csv</b> file, taking into account the received data in it:
- the desired product (search request);
- city (point of issue of goods);
- time of adding the entry;
- page number;
- position on the page;
- product brand name (search result);
- the cost of the goods with the code;
- the cost of goods without discount;
- item number;
- the number of reviews;
- rating (number of stars).

## <a name='get_started'>Get started</a>

There are two ways to install and use <b>ParserSelWB</b>: 
### <a name='scripts'>Scripts</a>

To run <b>ParserSelWB</b> from under the development environment, you must perform the following steps:
1. Install the latest stable version of Python from the link: https://www.python.org/downloads/
2. Install Git from https://git-scm.com/downloads
3. Clone the repository by running the command (for Windows):
     ```python
     $ git clone https://github.com/imartov/ParserSelWB.git
     ```
4. Create a virtual environment by running the command:
     ```python
     $ python -m venv your_name_venv
     ```
5. Activate the virtual environment by running the command:
     ```python
     $ cd your_name_venv\Scripts\activate
     ```
6. Install dependencies by running the command:
     ```python
     $ pip install -r requirements.txt
     ```
7. Install and extract the driver [chromedriver.exe](https://chromedriver.chromium.org/downloads) corresponding to your Chrome version.

The project structure should look like this:
![image](https://github.com/imartov/ParserSelWB/assets/116018998/e0146bf9-60d7-4ffe-b000-5998622c0aaa)

### <a name='exe_2'>.exe - temporarily unavailable</a>

Install the executable file <b>[ParserSelWB.exe](https://github.com/imartov/ParserSelWB/blob/main/ParserSelWB.exe)</b> on your device and use it like a normal application.

## <a name='run'>Run</a>

Depending on how you prefer to use <b>[ParserSelWB](https://github.com/imartov/ParserSelWB.git)</b>, you can run it in the appropriate ways.

### <a name='script'>Script</a>
#### <a name='input'>Input</a>

To run <b>[ParserSelWB](https://github.com/imartov/ParserSelWB.git)</b> and enter the data necessary for parsing into the <b>input</b> object, run <b>parserwbsel.py </b> by running the command:
```py
$ your_local_repository\python parserwbsel.py
```
#### <a name='parserwbsel'>parserwbsel.py</a>

Using an editor that supports Python (for example, [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) or [VS Code](https://code.visualstudio.com/download) ) go to <b>[parserwbsel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> and replace the <b>main()</b> function with next:

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
Change the parameters to the data you need:
- cities;
- search_goods;
- count_pages.

### <a name='exe_3'>.exe - temporarily unavailable</a>

Запустите <b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> как обычное приложение, после чего введите в терминал необходимые данные для поиска.

## <a name='html_data'>HTML data and bs4</a>

The first time you run <b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> the following directories will be created on the local repository: "data"/"html ", in which the received data will be placed. The "html" folder will contain the <b>"page_source"</b> objects of each page as html files. "data" will contain <b>result.csv</b> as well as <b>basic_goods_info.json</b> for interacting with other applications.
Since the html page data is saved, you can re-access it by redefining and collecting other information about the product without resorting to <b>Selenium</b>. To do this, you need to execute the <b>get_data_from_files()</b> function in <b>[parserwbsel.py](https://github.com/imartov/ParserSelWB/blob/main/bsparser.py)</b>, by creating an appropriate instance of the class.

## <a name='logger'>5. Logger</a>

<b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> is supplemented with logging tools that allow you to conveniently and quickly track exceptions and errors. Aborting <b>[ParserWBSel.py](https://github.com/imartov/ParserSelWB/blob/main/parserwbsel.py)</b> will create a <b>debug.log< file in the local project directory /b> , which will contain detailed information about the exception that was thrown.


