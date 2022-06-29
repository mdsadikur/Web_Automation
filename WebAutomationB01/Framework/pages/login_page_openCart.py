import time

from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        myAccount = self.driver.find_element(By.LINK_TEXT, "My Account")
        myAccount.click()
        loginLink = self.driver.find_element(By.LINK_TEXT, 'Login')
        loginLink.click()

        emailField = self.driver.find_element(By.ID, "input-email")
        emailField.send_keys(username)
        time.sleep(2)

        passwordField = self.driver.find_element(By.ID, "input-password")
        passwordField.send_keys(password)
        time.sleep(3)

        loginButton = self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div/div[2]/div/div/form/button")
        loginButton.click()