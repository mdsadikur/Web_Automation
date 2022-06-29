from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class SwitchWindow():
    def test_window(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(3)

        # Find parent window handle
        parent_handle = driver.current_window_handle
        # print(parent_handle)

        driver.find_element(By.LINK_TEXT, 'Click Here').click()
        all_handles = driver.window_handles
        time.sleep(2)
        # print(all_handles)

        # switch to child window
        for child_handle in all_handles:
            if child_handle not in parent_handle:
                driver.switch_to.window(child_handle)
                driver.get("https://google.com")
                print('Child Window Title: ' + driver.title)
            #  driver.close()

        # switch to parent window
        for child_handle in all_handles:
            if child_handle not in parent_handle:
                driver.switch_to.window(parent_handle)
                time.sleep(3)
                print('Parent Window Title: ' + driver.title)
            #   driver.close()

        driver.quit()


test_obj = SwitchWindow()
test_obj.test_window()
