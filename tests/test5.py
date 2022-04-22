from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# поиск элементов https://habr.com/ru/post/250975/

class TestLogin:
    def test_incorrect_user_name_and_password(self, init_webdriver):
        #init_webdriver.find_element_by_name("_username").send_keys("TestUser")  устарело, но работает
        init_webdriver.find_element(by=By.NAME, value="_username").send_keys("TestUser")
        init_webdriver.find_element(by=By.ID, value="password").send_keys("Password")
        invalidLoginLocator="//*[contains(text(),'Invalid credentials.')]"
        try:
            init_webdriver.find_element(by=By.XPATH, value=invalidLoginLocator)
        except NoSuchElementException:
            print("Passed, text not found before logon")
        init_webdriver.find_element(by=By.XPATH, value="//input[@value='Войти']").click()
        init_webdriver.find_element(by=By.XPATH, value=invalidLoginLocator)
        time.sleep(3)





