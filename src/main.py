import os
import logging
from src.api import HeadHunterAPI
from src.vacancy import Vacancy, VacancyManager
from src.file_handler import FileHandler

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR, "logs", "main.log")
file_handler = logging.FileHandler(path, encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def user_interaction():
    print("Введите поисковый запрос для вакансий:")
    query = input()
    api = HeadHunterAPI()
    vacancies = api.get_vacancies(query)

    # Преобразуем данные вакансий в объекты Vacancy
    vacancies_list = [Vacancy.from_dict(vacancy) for vacancy in vacancies]
    for vacancy in vacancies_list:
        VacancyManager.validate_vacancy_data(vacancy)

    # Сортируем вакансии по зарплате
    sorted_vacancies = VacancyManager.compare_vacancies_by_salary(vacancies_list)

    # Сохранение в файл
    FileHandler.save_to_json("vacancies.json", sorted_vacancies)

    # Вывод топ N вакансий
    print("Введите количество вакансий для вывода:")
    top_n = int(input())
    top_vacancies = sorted_vacancies[:top_n]

    for vacancy in top_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
