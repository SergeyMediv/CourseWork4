import json
from abc import ABC, abstractmethod

from src.vacancies import Vacancy


class Saver(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def add_vacancies(self, vacancies) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, query) -> list[dict]:
        pass

    def del_vacancy(self, query) -> None:
        pass


class JSONSaver(Saver):

    def add_vacancies(self, vacancies: list[Vacancy]):
        all_vacancies = [vacancy.to_json() for vacancy in vacancies]
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(all_vacancies, file, indent=2, ensure_ascii=False)

    def get_vacancies(self, query):
        pass
