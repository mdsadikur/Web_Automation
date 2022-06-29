from selenium import webdriver

''' Firefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://bbc.com")
driver.close()
'''

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://google.com")
driver.close()

'''
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.get("https://apple.com")
driver.close()
'''


