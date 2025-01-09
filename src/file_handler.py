import json
import os
import logging
from typing import List
from src.vacancy import Vacancy

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "logs", "file_handler.log")
file_handler = logging.FileHandler(path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class FileHandler:
    @staticmethod
    def save_to_json(file_path: str, vacancies: List[Vacancy]):
        """Сохранение вакансий в JSON файл"""
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([v.__dict__ for v in vacancies], f, ensure_ascii=False, indent=4)
        logger.info(f"Вакансии сохранены в файл: {file_path}")

    @staticmethod
    def load_from_json(file_path: str) -> List[Vacancy]:
        """Загрузка вакансий из JSON файла"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                logger.info(f"Вакансии загружены из файла: {file_path}")
                return [Vacancy(**vacancy) for vacancy in data]
        except FileNotFoundError:
            logger.warning(f"Файл не найден: {file_path}")
            return []
        except Exception as e:
            logger.error(f"Ошибка при загрузке файла: {e}")
            return []
