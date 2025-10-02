from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os

# Set custom download directory
# download_dir = "D:\\Pycharm\\"



download_dir_1 = "D\\Pycharm\\"

# chrome_options = Options()
# prefs = {"download.default_directory": download_dir}
# chrome_options.add_experimental_option("prefs", prefs)


chrome_options_1 = Options()
# prefs_1 = {"download.default_directory": download_dir_1}
# chrome_options_1.add_experimental_option("prefs_1", prefs_1)


# Start browser with download preferences
# driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(options=chrome_options_1)



download_2 = "D:\\Pycharm\\"

chrome_option_2= Options()
pref_2 = {"download.default_directory":download_2}
chrome_option_2.add_experimental_option("pref_2", pref_2)

driver = webdriver.Chrome(options=chrome_option_2)




# Open your web application
driver.get("https://www.lambdatest.com/selenium-playground/download-file-demo")

# Locate and click the download button/link
download_button = driver.find_element(By.XPATH, "//button[@type='button']")  # update locator
download_button.click()

# Wait for file to download
time.sleep(5)

# Check if file is downloaded
# files = os.listdir(download_dir)
files = os.listdir(download_dir_1)
print("Downloaded files:", files)

driver.quit()
