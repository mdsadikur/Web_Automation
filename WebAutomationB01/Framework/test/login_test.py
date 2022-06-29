import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginTests(unittest.TestCase):

    def test_invalid_Login(self):
        baseURL = "https://demo.opencart.com"
       # driver = webdriver.Firefox(executable_path="F:\Training\eSkillBd\Batch 1\Tools\geckodriver-v0.31.0-win64_2\geckodriver.exe")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        lp.login('test2@mail.com', '12342342')

        driver.close()

    @pytest.mark.skip
    def test_valid_Login(self):
        baseURL = "https://demo.opencart.com"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")
        lp.login('test2@mail.com', '12342342')

        driver.close()

