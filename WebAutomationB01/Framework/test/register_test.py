import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.register_page import RegisterPage
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegisterTest(unittest.TestCase):

    def test_invalid_Registartion(self):
        baseURL = "https://demo.opencart.com"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        rp = RegisterPage(driver)
        rp.register("John", 'smith', 'john@gmail.com', '123456')

        driver.close()


