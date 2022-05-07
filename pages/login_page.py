from selenium.webdriver.common.by import By
from pages.basic_page import BasicPage


class LoginPage(BasicPage):
    __FIELD_LOGIN = (By.ID, 'org.astekbet.client:id/username')
    __FIELD_PASSWORD = (By.ID, 'org.astekbet.client:id/et_password')
    __BUTTON_LOGIN = (By.ID, 'org.astekbet.client:id/enter_button')

    def input_login(self, login):
        self.input(login, *self.__FIELD_LOGIN)

    def input_password(self, password):
        self.input(password, *self.__FIELD_PASSWORD)

    def click_on_button_login(self):
        self.click(*self.__BUTTON_LOGIN)

    def check_page_visible(self):
        assert self.wait_element_present(*self.__BUTTON_LOGIN) \
               or self.wait_element_present(*self.__FIELD_LOGIN) is True, "log in screen isn't present"
