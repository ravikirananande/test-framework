from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.flipkart.com/')
wait=WebDriverWait(driver,10)
depart_from=wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@class="_1w3ZZo _1YBGQV _2EjOJB lZd1T6 _2vegSu _2mFmU7"]')))
# depart_from.click()
time.sleep(2)
depart_from.send_keys("Pune")
# results=driver.find_elements(By.XPATH,'//ul[@class="react-autosuggest__suggestions-list"]')
# print(len(results))
#
# for i in results:
#     if "Pune, India" in i.text:
#         i.click()
#         break