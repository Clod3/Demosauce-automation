from selenium import webdriver
from selenium.webdriver.common.by import By

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        