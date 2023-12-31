from selenium.webdriver.common.by import By

from tests import conftest
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")

    def fazer_login(self, usuario, senha):
        # self.driver.find_element(*self.username_field).send_keys(usuario)
        # self.driver.find_element(*self.password_field).send_keys(senha)
        # self.driver.find_element(*self.btn_login).click()
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.btn_login)
