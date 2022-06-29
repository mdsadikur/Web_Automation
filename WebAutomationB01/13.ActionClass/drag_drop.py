from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ActionChains


class DragDrop():
    def test_dragdrop(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        time.sleep(3)

        fromElement = driver.find_element(By.ID, 'column-a')
        toElement = driver.find_element(By.ID, 'column-b')
        time.sleep(2)

        actions = ActionChains(driver)
        actions.drag_and_drop(fromElement, toElement).perform()
        time.sleep(2)

        driver.close()


test_obj = DragDrop()
test_obj.test_dragdrop()