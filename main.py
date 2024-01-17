from cfg import VACANCIES_JSON
from src.api import HHApi, SJApi
from src.saver import JSONSaver
from src.utils import hh_vacancies_list, sj_vacancies_list, sort_vacancies_by_salary, validate_platform_input, \
    validate_salary_input, filter_vacancies_by_platform, vacancy_presentation


def main():
    json_file = JSONSaver(VACANCIES_JSON)

    search_query = input("Введите поисковый запрос: ")
    platform = validate_platform_input()
    min_salary = validate_salary_input()

    hh_api = HHApi(search_query)
    super_job_api = SJApi(search_query)

    hh_vacs = hh_vacancies_list(hh_api.get_vacancies())
    sj_vacs = sj_vacancies_list(super_job_api.get_vacancies())

    json_file.add_vacancies(hh_vacs + sj_vacs)

    sorted_vacancies_by_salary = sort_vacancies_by_salary(hh_vacs + sj_vacs, min_salary)
    sorted_vacancies_by_platform = filter_vacancies_by_platform(sorted_vacancies_by_salary, platform)
    if len(sorted_vacancies_by_platform) == 0:
        print("Нет подходящих вакансий")
    else:
        print(f"Мы подобрали {len(sorted_vacancies_by_platform)} вакансий")
        vacancy_presentation(sorted_vacancies_by_platform)


if __name__ == '__main__':
    main()
