import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Chrome config
driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")

# 2. Screen full
driver.maximize_window()

driver.get("https://demo.opencart.com/index.php?route=account/login")

# Explicit wait / hard wait
email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'input-email')))
email.clear()
email.send_keys("dasdsad@fffsad.ccc")

password = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'input-password')))
password.clear()
password.send_keys("5451231")

login = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div['
                                                                                 '2]/div/form/input')))
login.click()

# time - Not recommended
time.sleep(10)

# Implicit wait / soft wait
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT, 'Forgotten Password').click()


