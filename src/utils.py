from src.vacancies import Vacancy


def hh_vacancies_list(vacancies: list[dict]):
    vacancies_list = []
    for vacancy in vacancies:
        example_vacancy = Vacancy(
            vacancy_name=vacancy['name'],
            salary_from=vacancy['salary']['from'],
            salary_to=vacancy['salary']['to'],
            vacancy_currency=vacancy['salary']['currency'],
            vacancy_skills=vacancy['snippet']['requirement'],
            vacancy_duties=vacancy['snippet']['responsibility'],
            vacancy_url=vacancy['url']
        )
        vacancies_list.append(example_vacancy)
    return vacancies_list


def sj_vacancies_list(vacancies: list[dict]):
    vacancies_list = []
    for vacancy in vacancies:
        example_vacancy = Vacancy(
            vacancy_name=vacancy['profession'],
            salary_from=vacancy['payment_from'],
            salary_to=vacancy['payment_to'],
            vacancy_currency=vacancy['currency'],
            vacancy_skills=vacancy['candidat'],
            vacancy_duties=vacancy['work'],
            vacancy_url=vacancy['link']
        )
        vacancies_list.append(example_vacancy)
    return vacancies_list

