import os
from abc import ABC, abstractmethod
import requests
from dotenv import load_dotenv

from cfg import HH_URL, SJ_URL

load_dotenv()


class API(ABC):
    @abstractmethod
    def get_vacancies(self) -> list[dict]:
        pass


class HHApi(API):
    def __init__(self, query: str):
        self.query = query
        self.params = {
            'text': self.query,
            'page': 0,
            'per_page': 100,
            'only_with_salary': True,
            'search_field': 'name'
        }

    def get_vacancies(self) -> list[dict]:

        response = requests.get(url=HH_URL, params=self.params).json()
        return response['items']


class SJApi(API):

    def __init__(self, query: str):
        self.query = query
        self.params = {
            'keyword': self.query,
            'keywords': {'srws': 1,
                         'skwc': 'particular',
                         'keys': self.query},
            'page': 0,
            'count': 100
        }

    def get_vacancies(self) -> list[dict]:
        headers = {
            'X-Api-App-Id': os.getenv('SJ_API_KEY')
        }
        response = requests.get(url=SJ_URL, params=self.params, headers=headers).json()
        return response['objects']


x = SJApi('python')
# for x, y in x.get_vacancies()[16].items():
#     print(f'{x} - {y}')
# print(x.get_vacancies()[0]['profession'])
