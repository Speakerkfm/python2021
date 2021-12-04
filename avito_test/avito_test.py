import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = '/Users/usanin/chromedriver'


def data_comparison(left: tuple, right: tuple) -> bool:
    """
    функция проверки наличия данных в двух массивах
    если хотя бы одно значение совпадёт - вернется True
    иначе - False
    """
    for left_item in left:
        for right_item in right:
            if str(left_item).lower().find(str(right_item).lower()) != -1:
                return True
    return False


def convert_result_to_bool(list_data: list, list_size: int) -> bool:
    """
    функция преобразования списка входных значений в булево значение
    если сумма TRUE-значений во входном больше 80% размера списка входного - возвращается True
    - иначе - False
    """
    summa = 0
    for item in list_data:
        if item:
            summa = summa + 1

    if summa >= int(list_size * 0.8):
        return True
    return False


class TestSearchProductInCategory:
    data_set = ['стол', 'смартфон', 'сервер', 'Volkswagen Bora', 'Sennheiser', 'настольная лампа']
    expected_results = [
        ('стол', 'стол-книжка', 'столик'),
        ('смартфон', 'iphone', 'xiaomi', 'samsung', 'телефон'),
        ('сервер', 'удаленный', 'удалённый', 'стойк', 'dell', 'HP', 'supermicro'),
        ('Volkswagen', 'vw', 'Bora'),
        ('sennheiser', 'микрофон', 'наушник', 'система'),
        ('ламп', 'стол', 'настольн')
    ]
    params = []
    for index, item in enumerate(data_set):
        params.append((item, expected_results[index]))

    def setup_method(self, test_positive_param):
        self.browser = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
        self.browser.get('https://www.avito.ru')
        assert self.browser.title == 'Авито: недвижимость, транспорт, работа, услуги, вещи'

    def teardown_method(self, test_positive_param):
        self.browser.close()

    @pytest.mark.parametrize("search_query, expected_serp", params)
    def test_positive_param(self, search_query, expected_serp):
        search_line = self.browser.find_element(by='xpath', value='//input[@data-marker="search-form/suggest"]')
        search_button = self.browser.find_element(by='xpath', value='//button[@data-marker="search-form/submit-button"]')

        search_line.click()
        search_line.send_keys(search_query)
        search_button.click()

        result = []
        serp = self.browser.find_elements(by='xpath', value='//h3[@itemprop="name"]')[:10]

        for item in serp:
            title_item = tuple(str(str(item.text).split('\n')[0]).split())
            result.append(data_comparison(title_item, expected_serp))

        assert convert_result_to_bool(list_data=result, list_size=len(serp))


if __name__ == "__main__":
    pytest.main(sys.argv)