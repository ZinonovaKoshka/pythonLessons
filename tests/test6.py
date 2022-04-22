from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestLoginNegative:
    def test_incorrect_user_name_and_password(self, init_webdriver):
        init_webdriver.find_element(by=By.NAME, value="_username").send_keys("TestUser")
        init_webdriver.find_element(by=By.ID, value="password").send_keys("Password")
        invalidLoginLocator="//*[contains(text(),'Invalid credentials.')]"
        try:
            init_webdriver.find_element(by=By.XPATH, value=invalidLoginLocator)
        except NoSuchElementException:
            print("Passed, text not found before logon")
        init_webdriver.find_element(by=By.XPATH, value="//input[@value='Войти']").click()
        init_webdriver.find_element(by=By.XPATH, value=invalidLoginLocator)
        time.sleep(1)
        print("Тест №1 'Логин и пароль неверные' завершен")

    def test_incorrect_user_name_and_password2(self, init_webdriver):
        init_webdriver.find_element(by=By.XPATH, value="//input[@value='Войти']").click()
        invalidLoginLocator="//*[contains(text(),'Invalid credentials.')]"
        try:
            init_webdriver.find_element(by=By.XPATH, value=invalidLoginLocator)
        except NoSuchElementException:
            print("Passed, text not found before logon")
        urlLogin = init_webdriver.current_url
        assert urlLogin == "https://tt-develop.quality-lab.ru/login"
        time.sleep(1)
        print("Тест №2 'Логин и пароль пустые' завершен")

class TestLoginPositive:
    def test_correct_user_name_and_password(self, init_webdriver):
        init_webdriver.find_element(by=By.NAME, value="_username").send_keys("Лада Демакова")
        init_webdriver.find_element(by=By.ID, value="password").send_keys("AryaHGarForev2034")
        init_webdriver.find_element(by=By.XPATH, value="//input[@value='Войти']").click()
        urlAvtoriz = init_webdriver.current_url
        assert urlAvtoriz == "https://tt-develop.quality-lab.ru/report/group/edit"
        init_webdriver.find_element(by=By.CLASS_NAME, value="avatarCover").click()
        fio = init_webdriver.find_element(by=By.CLASS_NAME, value="m-card-user__name")
        email = init_webdriver.find_element(by=By.CLASS_NAME, value="m-card-user__email")
        assert fio.text == "Демакова Лада Анатольевна"
        emailT = email.text
        eCheck = 0
        if "fake" in emailT:
            eCheck = eCheck + 1
        if "@quality-lab.ru" in emailT:
            eCheck = eCheck + 1
        assert eCheck == 2
        time.sleep(3)
        print("Тест №3 'Успешная авторизация' завершен")
    def test_incorrect_user_name_password_fill(self, init_webdriver):
        init_webdriver.find_element(by=By.NAME, value="_username").send_keys("TestUser")
        init_webdriver.find_element(by=By.XPATH, value="//input[@value='Войти']").click()
        a = init_webdriver.find_element(by=By.NAME, value="_username")
        # print(a.get_attribute('value'))
        assert a.get_attribute('value') == "TestUser"
        b = init_webdriver.find_element(by=By.ID, value="password")
        assert b.get_attribute('value') == ""
        print("Тест №4 'Логин заполнен, пароль пустой' завершен")





