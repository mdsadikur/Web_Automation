from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Screenshot():
    def test_screenshots(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://apple.com")
        time.sleep(3)

        # Capture Screenshot on window size
        driver.get_screenshot_as_file("F:\Training\eSkillBd\Batch 1\Project\WebAutomationB01\ScreenshotFiles\Apple.png")

        driver.close()


test_obj = Screenshot()
test_obj.test_screenshots()
