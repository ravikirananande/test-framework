from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
wait=WebDriverWait(driver,10)
driver.get('https://www.yatra.com/')
driver.maximize_window()
class LaunchPage:
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    def departfrom(self,location):
        depart_from=self.wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="BE_flight_origin_city"]')))
        depart_from.click()
        time.sleep(1)
        depart_from.send_keys(location)
        depart_from.send_keys(Keys.ENTER)

        print('-------------------------------')

    def goto(self, location):
        go_to= self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="BE_flight_arrival_city"]')))
        go_to.click()
        time.sleep(2)
        go_to.send_keys(location)
        time.sleep(1)
        search_result=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div[1]/li")))
        for results in search_result:
            if 'New York (JFK)' in results.text:
                time.sleep(2)
                results.click()
                break
        print('+++++++++++++++++++++++++++++++')

    def selectdate(self,departuredate):
        date=self.wait.until(EC.element_to_be_clickable((By.ID,'BE_flight_origin_date')))
        all_dates=date.find_elements(By.ID,'BE_flight_origin_date')

        for dep_date in all_dates:
            if dep_date.get_attribute("data-date")==departuredate:
                dep_date.click()
                break
        time.sleep(2)
        # date.click()

        print('****************************************')

    def click_search_button(self):
        search_button=self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#BE_flight_flsearch_btn')))
        search_button.click()
        time.sleep(2)
        print('________________________________________________')



lp=LaunchPage(driver,wait)
lp.departfrom("Mumbai")
lp.goto("New York")
lp.selectdate('30/08/2023')
lp.click_search_button()
time.sleep(4)

