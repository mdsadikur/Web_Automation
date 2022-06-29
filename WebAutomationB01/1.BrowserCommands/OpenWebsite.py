from selenium import webdriver

# Firefox Config
driver = webdriver.Firefox(executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\geckodriver.exe")

# Open Test Website
driver.get("https://www.google.com/")