from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ActionChains


class MouseHover():
    def test_mouseHover(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/hovers")
        time.sleep(3)

        user1 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/img')

        actions = ActionChains(driver)
        actions.move_to_element(user1).perform()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/a').click()
        time.sleep(5)

        driver.close()


obj = MouseHover()
obj.test_mouseHover()