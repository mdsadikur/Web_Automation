import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils import excel_utils

'''
Data Driven Approach
'''


class LoginTests(unittest.TestCase):

    def test_invalid_Login(self):
        baseURL = "https://demo.opencart.com"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        login_data_file = 'F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\Framework\data\login_data.xlsx'
        login_sheet = 'Sheet1'
        number_of_rows = excel_utils.get_row_count(login_data_file, login_sheet)
        number_of_column = excel_utils.get_column_count(login_data_file, login_sheet)

        for r in range(2, number_of_rows + 1):
            dd_email = excel_utils.read_data(login_data_file, login_sheet, r, 1)
            dd_password = excel_utils.read_data(login_data_file, login_sheet, r, 2)

            lp = LoginPage(driver)
            lp.login(dd_email, dd_password)

        driver.close()
