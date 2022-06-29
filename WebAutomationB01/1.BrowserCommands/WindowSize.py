from selenium import webdriver

# 1. Chrome config
driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")

# 2. Screen full
driver.maximize_window()

# 3. Get maximize Window size
window_maximize_size = driver.get_window_size()
print(window_maximize_size)  # {'width': 1382, 'height': 744}

# 4. set specific window size
driver.set_window_size(800, 500)
window_set_size = driver.get_window_size()
print(window_set_size)
