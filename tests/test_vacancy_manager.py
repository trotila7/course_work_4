from src.vacancy import Vacancy, VacancyManager


def test_compare_vacancies_by_salary():
    vacancy1 = Vacancy("Python Developer", "url1", 100000, "Description 1", "Company 1")
    vacancy2 = Vacancy("Java Developer", "url2", 120000, "Description 2", "Company 2")
    sorted_vacancies = VacancyManager.compare_vacancies_by_salary([vacancy1, vacancy2])
    assert sorted_vacancies[0].salary == 120000


def test_vacancy_validation():
    vacancy = Vacancy("Python Developer", "url1", None, "Description 1", "Company 1")
    VacancyManager.validate_vacancy_data(vacancy)
    assert vacancy.salary == 0
