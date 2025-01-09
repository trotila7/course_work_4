# класс для работы с API платформы hh.ru
import requests
import os
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "logs", "api.log")
file_handler = logging.FileHandler(path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class AbstractAPI(ABC):
    """абстрактный класс для парсинга вакансий"""

    @abstractmethod
    def get_vacancies(self, search_query: str):
        pass


class HeadHunterAPI(AbstractAPI):
    BASE_URL = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, search_query: str):
        """Запрос вакансий с hh.ru по ключевому запросу"""
        params = {"text": search_query}
        try:
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            logger.info(f"Вакансии получены для запроса: {search_query}")
            return response.json()["items"]
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при получении данных: {e}")
            return []
