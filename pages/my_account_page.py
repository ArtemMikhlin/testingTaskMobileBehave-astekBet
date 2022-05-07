from selenium.webdriver.common.by import By
from pages.basic_page import BasicPage


class MyAccountPage(BasicPage):
    __LABEL_ACCOUNT_ID = (By.ID, "org.astekbet.client:id/current_id_view")
    __LABEL_BALANCE_ID = (By.ID, "org.astekbet.client:id/balance_id_view")

    def check_page_visible(self):
        assert self.wait_element_present(*self.__LABEL_ACCOUNT_ID) or\
               self.wait_element_present(*self.__LABEL_ACCOUNT_ID) \
               is True, "my account screen isn't present"

    def check_account_id(self, account_id):
        self.check_text_from_element(account_id, "account id isn't actual", *self.__LABEL_ACCOUNT_ID)
