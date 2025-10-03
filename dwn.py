from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
import time

from dowload import prefs

download_dir = "D:\\Pycharm\\"

chrome_options = Options()
prefs = {"download.default_directory": prefs}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.lambdatest.com/selenium-playground/download-file-demo")

# Locate and click the download button/link
download_button = driver.find_element(By.XPATH, "//button[@type='button']")  # update locator
download_button.click()

# Wait for file to download
time.sleep(5)

files = os.listdir(download_dir)
print("file", files)

driver.quit()