from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

normal_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
normal_alert.click()
driver.switch_to.alert.accept()  # OK

confirm_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
confirm_alert.click()
driver.switch_to.alert.dismiss() # cancel

prompt_alert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
prompt_alert.click()
driver.switch_to.alert.send_keys('Test Automation')
driver.switch_to.alert.accept()

time.sleep(4000)