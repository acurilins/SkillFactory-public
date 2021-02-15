import pytest
# import uu
# import os
# import uuid

from selenium import webdriver


# запуск веб драйвера
@pytest.fixture(autouse=True)
def testing():
    # путь к вебрадрайверу
    pytest.driver = webdriver.Chrome('C:\\chromedriver.exe')

    # Переход на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


