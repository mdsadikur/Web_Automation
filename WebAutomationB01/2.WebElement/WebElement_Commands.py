from selenium import webdriver
from selenium.webdriver.common.by import By

# Commands
# 1. Click
# 2. Send_keys
# 3. clear()
# 4. text
# 5. size
# 6. is_displayed
# 7. is_enabled
# 8. is_selected

# 1. Chrome config
driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")

# 2. Screen full
driver.maximize_window()

driver.get("https://demo.opencart.com/index.php?route=account/login")


# Invalid Test
# clear , send_keys
driver.find_element(By.ID, 'input-email').clear()
driver.find_element(By.ID, 'input-email').send_keys("invalidemail@test.com")
driver.find_element(By.ID, 'input-password').clear()
driver.find_element(By.ID, 'input-password').send_keys("saas23142134")
driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()

# text
print('Forgot password text is: ' + driver.find_element(By.LINK_TEXT, 'Forgotten Password').text)

# size
sizeOfEmail = driver.find_element(By.ID, 'input-email').size
print('Width of Email is: ' + str(sizeOfEmail["width"]))
print('Height of Email is: ' + str(sizeOfEmail["height"]))

# is_displayed
Email_displayed = driver.find_element(By.ID, 'input-email').is_displayed()
print('Display Status: ' + str(Email_displayed))

# is_enabled
Email_enabled = driver.find_element(By.ID, 'input-email').is_enabled()
print('Enabled status: ' + str(Email_enabled))

driver.get("https://demo.opencart.com/index.php?route=account/register")

# is_selected
Privacy_selected = driver.find_element(By.NAME, 'agree').is_selected()
print('Selected status: ' + str(Privacy_selected))

driver.close()
