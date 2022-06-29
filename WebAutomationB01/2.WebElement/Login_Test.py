from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Chrome config
driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")

# 2. Screen full
driver.maximize_window()

driver.get("https://demo.opencart.com/index.php?route=account/login")

# Invalid Test
driver.find_element(By.ID, 'input-email').clear()
driver.find_element(By.ID, 'input-email').send_keys("invalidemail@test.com")
driver.find_element(By.ID, 'input-password').clear()
driver.find_element(By.ID, 'input-password').send_keys("saas23142134")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()

# Valid Test
driver.find_element(By.ID, 'input-email').clear()
driver.find_element(By.ID, 'input-email').send_keys("user6@bd.com")
driver.find_element(By.ID, 'input-password').clear()
driver.find_element(By.ID, 'input-password').send_keys("123456")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()
