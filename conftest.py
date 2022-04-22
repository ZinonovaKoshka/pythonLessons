import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture(scope="function", autouse=True)
def init_webdriver():
    """Инициализация драйвера"""

    options = Options()
    # options.add_argument("window-size=1920,1080")
    options.add_argument("--kiosk")
    driver = webdriver.Chrome(options=options)
    driver.get("https://tt-develop.quality-lab.ru")
    # driver.maximize_window()
    yield driver
    driver.quit()