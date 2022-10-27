import json
import requests
from config import exchanges


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена в моем списке!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена в моем списке!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"
        headers = {"apikey": "DFmWZjdt0fKhXzxoHchC7Oi6Wd4f1wQ4"}
        response = requests.get(url, headers=headers)
        result = json.loads(response.content)
        price = round(result['result'], 2)
        message = f"Цена {amount} {base} в {sym} : {price}"
        return message
