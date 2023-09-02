import pytest
from selenium import webdriver
from pages.yatra_launch_page import *

@pytest.mark.usefixtures('setup')
class TestSearchAndVerifyFilter:
    def test_search_flights(self):
        lp=LaunchPage(self.driver,self.wait)
        lp.departfrom("New Delhi")
        lp.goto('New York')
        lp.selectdate('26/08/2023')
        lp.click_search_button()


