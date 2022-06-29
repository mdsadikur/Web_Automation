from selenium import webdriver

driver = webdriver.Chrome(
    executable_path="F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Drivers\chromedriver.exe")
print('Browser launch Successfully')

driver.maximize_window()
print('Browser Maximize')

driver.get("https://www.google.com/")
print('Google Open')

# Title verify
expected_title = "Google"
actual_title = driver.title
if expected_title == actual_title:
    print("Title Verification passed")
else:
    print("Title Verification failed." '\n' "Actual Title: " + actual_title + '\n' + "Expected Title: " + expected_title)

driver.quit()
print("Browser Terminated")
