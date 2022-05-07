from selenium.webdriver.common.by import By
from pages.basic_page import BasicPage


class RegistrationTypePage(BasicPage):
    __LIST_OF_REGISTRATION_OPTIONS = (By.ID, "org.astekbet.client:id/registration_type_name")

    def click_on_option(self, registration_option):
        list_of_registration_options = self.find_elements(*self.__LIST_OF_REGISTRATION_OPTIONS)
        if registration_option == 'in one click': list_of_registration_options[0].click()
        elif registration_option == 'by phone': list_of_registration_options[1].click()
        elif registration_option == 'full': list_of_registration_options[2].click()
        else: raise Exception(f"Registration option {registration_option} isn't correct!")
