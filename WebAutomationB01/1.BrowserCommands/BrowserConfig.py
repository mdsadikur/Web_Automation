from selenium import webdriver

# 1. Chrome config
driver = webdriver.Chrome(executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")

# 2. Screen full
driver.maximize_window()

# 3. Firefox Config
# driver2 = webdriver.Firefox(executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\geckodriver.exe")