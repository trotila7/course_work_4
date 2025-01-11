import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "logs", "vacancy.log")
file_handler = logging.FileHandler(path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


class Vacancy:
    def __init__(self, title: str, url: str, salary: Optional[float], description: str, company: str):
        self.title = title
        self.url = url
        self.salary = salary if salary else "Зарплата не указана"
        self.description = description
        self.company = company

    def __repr__(self):
        return f"Vacancy(title={self.title}, company={self.company}, salary={self.salary})"

    def __eq__(self, other):
        """Сравниваем вакансии по зарплате"""
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        return False

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Создание вакансии из словаря"""
        return cls(
            title=data["name"],
            url=data["url"],
            salary=data.get("salary", {}).get("from", 0),
            description=data.get("snippet", {}).get("responsibility", ""),
            company=data.get("employer", {}).get("name", "Не указано")
        )


class VacancyManager:
    @staticmethod
    def validate_vacancy_data(vacancy: Vacancy):
        """Валидация данных вакансии"""
        if not vacancy.salary or vacancy.salary == "Зарплата не указана":
            vacancy.salary = 0

    @staticmethod
    def compare_vacancies_by_salary(vacancies: list):
        """Сортировка вакансий по зарплате"""
        return sorted(vacancies, key=lambda x: x.salary, reverse=True)
