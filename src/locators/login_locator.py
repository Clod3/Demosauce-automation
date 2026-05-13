from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGINBTN = (By.ID, "login-button")
