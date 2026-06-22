from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

        #selectores
        self.username_input = (By.ID,"user-name")
        self.password_input = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.error_password = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get("https://saucedemo.com/")

    def ingresar_usuario(self, usuario):
        self.driver.find_element(*self.username_input).send_keys(usuario)

    def ingresar_contraseña(self, contraseña):
        self.driver.find_element(*self.password_input).send_keys(contraseña)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()


    def login(self,usuario,contraseña):
        self.open()
        self.ingresar_usuario(usuario)
        self.ingresar_contraseña(contraseña)
        self.click_login()

    def get_error_password_message(self):
        error = self.driver.find_element(*self.error_password).text
        print(error)
        return error
