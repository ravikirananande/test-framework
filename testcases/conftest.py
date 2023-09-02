from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
@pytest.fixture(scope='class')
def setup(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    driver.get('https://www.yatra.com/')
    request.cls.driver=driver
    request.cls.wait=wait
    yield
    driver.close()