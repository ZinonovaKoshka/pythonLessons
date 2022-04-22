from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class TestLogin:
    def testinitWebDriver(self):
        options = Options()
        options.add_argument("window-size=500,500")
        driver = webdriver.Chrome(options=options)
        driver.get("https://tt-develop.quality-lab.ru")
        time.sleep(2)
        driver.set_window_size(200, 100)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.quit()





