from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demo.opencart.com/index.php?route=account/register")

checkbox = driver.find_element(By.NAME, "agree")

enable_status = checkbox.is_enabled()  # True
print(enable_status)
select_status = checkbox.is_selected()  # False
print(select_status)

if (enable_status == True) and (select_status == False):
    checkbox.click()


select_status = checkbox.is_selected()  # True
print(select_status)
