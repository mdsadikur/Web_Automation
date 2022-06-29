from selenium import webdriver

# 1. Chrome config
driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")
print('Browser launch Successfully')

# 2. Screen full
driver.maximize_window()
print('Browser Maximize')

# 3. Close Current tab/Active Tab
# driver.close()
# print('Current tab close')

# 4. Quit Browser
driver.quit()
print('Browser Closed')
