# python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe test_selenium_pf.py

import pytest
from selenium import webdriver
import uu
import os
import uuid
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures()
def test_show_my_pets():

    # выставление величины неявного ожидания
    pytest.driver.implicitly_wait(1)

    # расширение окна браузера
    pytest.driver.maximize_window()

    # поиск поля e-mail и ввод данных
    field_email = pytest.driver.find_element_by_id("email")
    field_email.clear()
    field_email.send_keys("abra@cadabra.com")

    # поиск поля password и ввод данных
    field_pass = pytest.driver.find_element_by_id("pass")
    field_pass.clear()
    field_pass.send_keys("abra@cadabra.com")

    # поиск и нажатие кнопки "Войти"
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # поиск и нажатие меню "Мои Питомцы"
    pytest.driver.find_element_by_class_name("nav-link").click()

    # подтвержение о нахождении на нужной странице
    assert pytest.driver.find_element_by_tag_name('h2').text == "abra"

    # поиск кол-ва питомцев в таблице
    my_pets = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr')

    """ тот же поиск с ипользованием явного ожидания
    my_pets = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                             '//div[@id="all_my_pets"]/table[@class="table table-hover"]/tbody/tr'))
    )
    """

    # поиск кол-ва питомцев в статистике юзера в текстовом формате
    pets_stat = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]'))
    )
    assert 'Питомцев:' in pets_stat.text

    # преобразование текста в число
    pets_qty = int(pets_stat.text.split('\n')[1].split(':')[1])

    table = len(my_pets)

    # сравнение кол-вa питомцев в статистике с таблицей питомцев
    assert pets_qty == table

    # та же проверка вручную
    # assert len(my_pets) == 6

    # images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    images = pytest.driver.find_elements_by_xpath('//img[@class="card-img-top"]')
    # images = pytest.driver.find_elements_by_class_name('card-img-top')

    # names = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_xpath('//h5[@class="card-title"]')
    # names = pytest.driver.find_elements_by_class_name('card-title')

    # descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    descriptions = pytest.driver.find_elements_by_xpath('//p[@class="card-text"]')
    # descriptions = pytest.driver.find_elements_by_class_name('card-text')

    # проверка карточек питомцев на наличие фото, имя, возраст и вид из модуля (НЕ РАБОТАЕТ!!!)
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

    #  НЕ РАБОТАЕТ!!!
    # photo_list = WebDriverWait(pytest.driver, 10).until(
    #     EC.presence_of_all_elements_located((By.XPATH,
    #                                          '//div[@id="all_my_pets"]/table[@class="table table-hover"]/tbody/tr/th/img'))
    # )
    # photo_qty = 0
    # for photo in photo_list:
    #     if photo.get_attribute('src') != '':
    #         photo_qty += 1
    # assert photo_qty >= pets_qty / 2

    """ проверка имени, вида и возраста животных "вручную"
    assert pytest.driver.find_elements_by_css_selector('#all_my_pets tr')[1].text == "тЯф булька 1,5\n×"
    assert pytest.driver.find_elements_by_css_selector('#all_my_pets tr')[2].text == "Baly bear 4\n×"
    assert pytest.driver.find_elements_by_css_selector('#all_my_pets tr')[3].text == "плоскомордый песик 2\n×"
    assert pytest.driver.find_elements_by_css_selector('#all_my_pets tr')[4].text == "hfhdh rr 5\n×"
    assert pytest.driver.find_elements_by_css_selector('#all_my_pets tr')[5].text == "Gerald Llama Twelve\n×"
    """

    # Проверка имени, породы и возраста каждого питомца на уникальность
    info_list = []
    pets_stat = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                             '//div[@id="all_my_pets"]/table[@class="table table-hover"]/tbody/tr'))
    )
    for pet in pets_stat:
        cells = pet.text.split()
        info = tuple([cells[0], cells[1], cells[2]])
        info_list.append(info)
    # Преобразование списка во множество для удаления повторяющихся наименований
    info_set = set(info_list)
    assert len(info_list) == len(info_set)
