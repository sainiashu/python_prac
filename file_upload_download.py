# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Start browser (Chrome in this case)
# driver  = webdriver.Chrome()
#
# # Open your web application
# driver.get("https://www.lambdatest.com/selenium-playground/upload-file-demo")
#
#
# # Locate the file input element on the page (replace with the correct locator)
# # upload_element = driver.find_element(By.ID, "file")  # or By.NAME / By.XPATH
#
# upload_file = driver.find_element(By.ID, "file")
#
# # Send the file path to the input element
# upload_file.send_keys("D:\\Pycharm\\test.PNG")
#
# # If there's an upload/submit button, click it
# # submit_button = driver.find_element(By.ID, "upload-button")
# # submit_button.click()
#
# time.sleep(3)  # wait for upload to finish
#
# print("File uploaded successfully!")
#
# driver.quit()


from selenium import  webdriver
from selenium.webdriver.common.by import By
import  time

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com/selenium-playground/upload-file-demo")
filePath = driver.find_element(By.ID, "file")
filePath.send_keys("D:\\Pycharm\\test.PNG")
# submit_button = driver.find_element(By.ID, "upload-button")
# submit_button.click()
# driver.find_element(By.ID, "upload-button").click()
time.sleep(10)  # wait for upload to finish

print("File uploaded successfully!")
driver.quit()