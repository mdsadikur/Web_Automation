from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")

# 2. Screen full
driver.maximize_window()

driver.get("https://www.bbc.com/")


# Scroll to the end of thw web page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
