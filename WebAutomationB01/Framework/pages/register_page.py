import time

from selenium.webdriver.common.by import By


class RegisterPage():

    def __init__(self, driver):
        self.driver = driver

    def register(self, FirstName, LastName, Email, Password):
        myAccount = self.driver.find_element(By.LINK_TEXT, "My Account")
        myAccount.click()
        loginLink = self.driver.find_element(By.LINK_TEXT, 'Register')
        loginLink.click()

        first_name_Field = self.driver.find_element(By.ID, "input-firstname")
        first_name_Field.send_keys(FirstName)
        time.sleep(2)

        last_name_Field = self.driver.find_element(By.ID, "input-lastname")
        last_name_Field.send_keys(LastName)
        time.sleep(2)

        email_Field = self.driver.find_element(By.ID, "input-email")
        email_Field.send_keys(Email)
        time.sleep(2)

        password_Field = self.driver.find_element(By.ID, "input-password")
        password_Field.send_keys(Password)
        time.sleep(2)

        privacy_policy = self.driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/div/input')
        privacy_policy.click()
        time.sleep(2)

        continue_button = self.driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/button')
        continue_button.click()
