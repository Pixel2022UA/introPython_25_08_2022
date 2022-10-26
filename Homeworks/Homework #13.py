import json
import requests

url = "http://api.forismatic.com/api/1.0/"
filename = "data_quote.json"

def sort_by_surname(str_):
    surname = str_['quoteAuthor']
    sort_sur = surname.split()[-1]
    return sort_sur


class Quotes:
    def __init__(self, quantity=int, filename=filename):
        self.quantity = quantity
        self.filename = filename

    def get_quotes(self, quantity) -> list:
        data_list = []
        key = 0
        try:
            while len(data_list) < quantity:                                                                # for key in range():  не использовал т.к. из взятого
                params = {"method": "getQuote", "format": "json", "key": key, "lang": "ru"}                 # количества мы удаляем строки без авторов и нужно
                response = requests.get(url, params=params)                                                 # добирать недостающие строки. ("Это при условии что нам нужно
                if response.json()['quoteAuthor']:                                                          # выводить строго указанное кол-во цитат)
                    data_list.append(response.json())
                key += 1
        except:
            pass
        return data_list

    def print_quotes(self, quantity, separator):
        for str_ in self.get_quotes(quantity):
            print(f"{str_['quoteText']}{separator}{str_['quoteAuthor']}")

    def save_quotes(self, quantity):
        sort_data = sorted(self.get_quotes(quantity), key=sort_by_surname)
        with open(filename, "w", encoding="utf-8") as json_file:
            json_file.write(json.dumps(sort_data, ensure_ascii=False))


example = Quotes()

example.get_quotes(4)
example.print_quotes(2, separator=" - ")
example.save_quotes(5)
