from googletrans import Translator


class Trans:

    def __init__(self, list_text:list) -> None:
        self.list_text = list_text
        self.translated_list = []
        self.translator = Translator()
    
    def from_ru_to_en(self) -> list:
        for text in self.list_text:
            translated_value = self.translator.translate(text=text, dest='en')
            translated_value = translated_value.text.strip().replace(' ', '_').replace('-', '_').replace("'", '').lower()
            self.translated_list.append(translated_value)

        return self.translated_list
    
    def from_en_to_ru(self) -> list:
        for text in self.list_text:
            translated_value = text.strip().capitalize().replace('_', ' ')
            translated_value = self.translator.translate(text=translated_value, dest='ru').text
            self.translated_list.append(translated_value)

        return self.translated_list
