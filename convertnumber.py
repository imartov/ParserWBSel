import re


class ConvertNumber:

    def __init__(self, text:str) -> None:
        self.text = text
        self.numbers_list = re.findall(r'\d+', self.text)


    def convert_price_to_float(self) -> float:
        if self.text == 'None':
            return self.text
        
        elif ',' in self.text or '.' in self.text:
            price_float = ''
            for symbol in self.text:
                if symbol.isdigit() or symbol == ',' or symbol == '.':
                    price_float += symbol

            price_float = re.findall(r'\d+', price_float)
            price_float = int(price_float[0]) + (int(price_float[1]) / 10**len(int(price_float[1])))
            return price_float

        elif ',' not in self.text and '.' not in self.text and len(self.numbers_list) > 1:
            return float(''.join(self.numbers_list))
        else:
            price_float = float(self.numbers_list[0])
        return price_float


    def convert_review_to_int(self) -> int:
        return int(''.join(self.numbers_list))
    

    def convert_href_to_int_and_get_article(self) -> int:
        return int(self.numbers_list[0])
    