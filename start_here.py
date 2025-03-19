from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Install the Chrome Webdriver from: https://sites.google.com/chromium.org/driver/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")


search = driver.find_element(By.CLASS_NAME, "gLFyf")
search.send_keys("Dogs and Cats")


time.sleep(10)

driver.quit()


