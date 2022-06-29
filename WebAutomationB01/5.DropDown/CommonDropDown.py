from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

# Country Dropdown locate
Countries = driver.find_element(By.ID, 'Form_submitForm_Country')
# All options
all_countries = Select(Countries)


# select bangladesh by select_by_value()
all_countries.select_by_value('Bangladesh')
time.sleep(5000)

'''
# select bangladesh by select_by_index()
all_countries.select_by_index(2)
time.sleep(5000)
'''

'''
# select bangladesh by select_by_text()
all_countries.select_by_visible_text('Finland')
time.sleep(4000)
'''






