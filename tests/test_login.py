import pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By

def login(username, password):
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/login")
    driver.find_element(By.ID, "Email").clear()
    driver.find_element(By.ID,"Email").send_keys(username)

    driver.find_element(By.ID, "Password").clear()
    driver.find_element(By.ID, "Password").send_keys(password)

    driver.find_element(By.XPATH, "//input[@value='Log in']").click()

    # return "success" if username and password else "fail"


def test_login(username, password):
    login(username, password)

