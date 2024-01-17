from src.vacancies import Vacancy, SJVacancy, HHVacancy


def hh_vacancies_list(vacancies: list[dict]):
    vacancies_list = []
    for vacancy in vacancies:
        example_vacancy = HHVacancy(
            vacancy_name=vacancy['name'],
            salary_from=vacancy['salary']['from'],
            salary_to=vacancy['salary']['to'],
            vacancy_currency=vacancy['salary']['currency'],
            vacancy_skills=vacancy['snippet']['requirement'],
            vacancy_duties=vacancy['snippet']['responsibility'],
            vacancy_url=vacancy['alternate_url']
        )
        vacancies_list.append(example_vacancy)
    return vacancies_list


def sj_vacancies_list(vacancies: list[dict]):
    vacancies_list = []
    for vacancy in vacancies:
        example_vacancy = SJVacancy(
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


def sort_vacancies_by_salary(vacancies: list[Vacancy], min_salary=0):
    sorted_vacancies = []
    for vacancy in vacancies:
        if vacancy.salary_from >= min_salary and vacancy.vacancy_currency == 'RUR' or vacancy.vacancy_currency == 'rub':
            sorted_vacancies.append(vacancy)
    return sorted(sorted_vacancies)


def validate_platform_input():
    while True:
        platform = ''
        platform_query = int(input("Выберите платформу для поиска вакансии:\n"
                                   "0 - Неважно\n"
                                   "1 - HeadHunter\n"
                                   "2 - SuperJob\n"
                                   "Ваш выбор: "))
        if platform_query == 1:
            platform = 'HeadHunter'
            break
        elif platform_query == 2:
            platform = 'SuperJob'
            break
        elif platform_query == 0:
            platform = None
            break
        else:
            print("Неверный выбор")
            continue
    return platform


def validate_salary_input():
    while True:
        salary = 0
        salary_query = input("Введите минимальную желаемую ЗП: ")
        if not salary_query.isdigit():
            print("Введите целое число")
            continue
        elif int(salary_query) < 0:
            print("Введите целое число")
            continue
        else:
            salary = salary_query
            break
    return int(salary)


def filter_vacancies_by_platform(vacancies, platform):
    filtered_vacancies = []
    if platform:
        for vacancy in vacancies:
            if vacancy.platform == platform:
                filtered_vacancies.append(vacancy)
    else:
        filtered_vacancies = vacancies
    return filtered_vacancies


def vacancy_presentation(vacancies):
    while True:
        number = input("Сколько вывести на экран?\n"
                       "Введите целое число: ")
        if not number.isdigit():
            print("Введите целое число")
            continue
        else:
            break
    print("\nВот, что мы для Вас подобрали:\n")
    for vacancy in vacancies[0:int(number)]:
        if vacancy.vacancy_skills:
            skills = vacancy.vacancy_skills.split('.')
        if vacancy.salary_to > 0:
            print(f'Вакансия: {vacancy.vacancy_name}\n'
                  f'ЗП : {vacancy.salary_repr}\n'
                  f'Описание: {skills[0].replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n'
                  f'\n')
        else:
            print(f'Вакансия: {vacancy.vacancy_name}\n'
                  f'ЗП : от {vacancy.salary_from}\n'
                  f'Описание: {skills[0].replace("<highlighttext>", "").replace("</highlighttext>", "")}\n'
                  f'Ссылка на вакансию: {vacancy.vacancy_url}\n'
                  f'\n')
