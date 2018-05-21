import requests
from datetime import date
from app import app
FIXER_ACCESS_KEY = app.config['FIXER_ACCESS_KEY']


def get_historical_currency_rates(base_currency_code:str, exchange_date:date):
    payload = {'access_key': FIXER_ACCESS_KEY, 'base': base_currency_code}
    response = requests.get(f'http://data.fixer.io/api/{exchange_date}', params=payload)
    response_json = response.json()
    if response_json.get('success') is True:
        return response_json['rates']
    else:
        raise Exception('Error happened during fetching historical exchange rates\n'
                        f'Date: {exchange_date}\n'
                        f'Base currency: {base_currency_code}\n'
                        f'Fixer answer: {response.status_code} {response.json()}')


def get_current_currency_rates(base_currency_code:str):
    payload = {'access_key': FIXER_ACCESS_KEY}
    response = requests.get('http://data.fixer.io/api/latest', params=payload)
    response_json = response.json()
    if response_json.get('success') is True:
        return response_json['rates']
    else:
        raise Exception('Error happened during fetching currenct exchange rates\n'
                        f'Base currency: {base_currency_code}\n'
                        f'Fixer answer: {response.status_code} {response.json()}')
