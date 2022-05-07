from selenium.webdriver.common.by import By
from pages.basic_page import BasicPage


class OneClickRegistrationPage(BasicPage):
    __CHECKBOX_CONFIRM_PP = (By.ID, "org.astekbet.client:id/ready_for_anything_checkbox")
    __BUTTON_ACCEPT = (By.ID, "org.astekbet.client:id/fab")

    # Pop-up registration successful
    __POPUP_REGISTRATION_SUCCESSFUL = (By.ID, "org.astekbet.client:id/card")
    __LABEL_LOGIN = (By.ID, "org.astekbet.client:id/tvLogin")
    __LABEL_PASSWORD = (By.ID, "org.astekbet.client:id/tvPassword")
    __BUTTON_COPY = (By.ID, "org.astekbet.client:id/copyContainer")
    __BUTTON_NEXT = (By.ID, "org.astekbet.client:id/btnNext")

    def click_on_checkbox_confirm_pp(self):
        self.click(*self.__CHECKBOX_CONFIRM_PP)

    def click_on_button_accept(self):
        self.click(*self.__BUTTON_ACCEPT)

    def check_page_visible(self):
        assert self.wait_element_present(*self.__CHECKBOX_CONFIRM_PP) or \
               self.wait_element_present(*self.__BUTTON_ACCEPT) is True, "'one slick registration' screen isn't present"

    def click_on_button_copy(self):
        self.click(*self.__BUTTON_COPY)

    def click_on_button_next(self):
        self.click(*self.__BUTTON_NEXT)

    def check_popup_registration_successful_visible(self):
        assert self.is_element_present(*self.__POPUP_REGISTRATION_SUCCESSFUL) or\
               self.is_element_present(*self.__BUTTON_COPY) or\
               self.is_element_present(*self.__BUTTON_NEXT) is True, "'registration successful' pop-up isn't present"

