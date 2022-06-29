from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SwitchIframe():
    def test_iframe(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/iframe")
        time.sleep(3)

        # switch to iframe
        driver.switch_to.frame('mce_0_ifr')

        paragraph = driver.find_element(By.XPATH, '//*[@id="tinymce"]/p')
        paragraph.clear()
        paragraph.send_keys("Test Automation")
        time.sleep(3)


test_obj = SwitchIframe()
test_obj.test_iframe()