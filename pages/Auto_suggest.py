from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.makemytrip.com/')
print(driver.title)
# wait=WebDriverWait(driver,10)
driver.implicitly_wait(10)
# alert_page=wait.until(EC.element_to_be_clickable((By.ID,"webklipper-publisher-widget-container-notification-close-div")))
# alert_page.click()

username=driver.find_element(By.ID,'username')
username.send_keys('9405409071')
continue_page=driver.find_element(By.XPATH,"//span[text()='Continue']")
continue_page.click()
time.sleep(3)
# depart_from=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input')))
# depart_from.click()
# time.sleep(2)
# depart_from.send_keys("Pune")
#
# results=driver.find_elements(By.XPATH,'//ul[@class="react-autosuggest__suggestions-list"]')
# print(len(results))
#
# for i in results:
#     if "Pune, India" in i.text:
#         i.click()
#         break