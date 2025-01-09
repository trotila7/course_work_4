# класс для работы с API платформы hh.ru
import requests
import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)


class AbstractAPI(ABC):
    """абстрактный класс для парсинга вакансий"""
    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass


class HeadHunterAPI(AbstractAPI):
    BASE_URL = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_query: str):
        """Запрос вакансий с hh.ru по ключевому запросу"""

