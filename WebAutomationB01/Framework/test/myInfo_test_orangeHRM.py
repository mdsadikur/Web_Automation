import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Framework.pages.login_page_orangeHRM import LoginPage_orange
from Framework.pages.myInfo_page_orangeHRM import MyInfoPage_orange
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class MyInfoTests(unittest.TestCase):

    def test_add_contact(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage_orange(driver)
        lp.login_orange("Admin", "admin123")

        mi = MyInfoPage_orange(driver)
        mi.emergency_contact_add('Test1234', 'something', '12345', '122132123', '12321312')

        driver.close()

    def test_edit_contact(self):
        baseURL = "https://opensource-demo.orangehrmlive.com/"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        lp = LoginPage_orange(driver)
        lp.login_orange("Admin", "admin123")

        mi = MyInfoPage_orange(driver)
        # add
        mi.emergency_contact_add('NY1001', 'something', '12345', '122132123', '12321312')

        # Edit
        mi.emergency_contact_edit('New Name', 'nothing', '1232321', '132321', '12313')
