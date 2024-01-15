from src.api import HHApi, SJApi


def main():
    search_query = input("Введите поисковый запрос: ")
    hh_api = HHApi(search_query)
    super_job_api = SJApi(search_query)


if __name__ == '__main__':
    main()
