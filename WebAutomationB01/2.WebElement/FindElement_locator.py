from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Chrome config
driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")

# 2. Screen full
driver.maximize_window()

driver.get("http://127.0.0.1:5500/home.html")

driver.find_element(By.ID, "myInput").send_keys("Selenium")
driver.find_element(By.NAME, "my_Input").send_keys("Automation")
#driver.find_element(By.XPATH, '//*[@id="myID"]/input[3]').send_keys("Python")
driver.find_element(By.CSS_SELECTOR, '#myID > input.input_2').send_keys("Python new")
#driver.find_element(By.CLASS_NAME, "input_2").send_keys("Python")

driver.find_element(By.LINK_TEXT, 'About').click()