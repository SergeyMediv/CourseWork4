from src.api import HHApi, SJApi
from src.utils import hh_vacancies_list, sj_vacancies_list


def main():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HHApi(search_query)
    super_job_api = SJApi(search_query)

    hh_vacs = hh_vacancies_list(hh_api.get_vacancies())
    sj_vacs = sj_vacancies_list(super_job_api.get_vacancies())

#    print(sj_vacs[1].vacancy_name, sj_vacs[1].salary_repr, sj_vacs[1].vacancy_currency)
#    print('----')
#    print(hh_vacs[1].vacancy_name, hh_vacs[1].salary_repr, hh_vacs[1].vacancy_currency)


if __name__ == '__main__':
    main()
