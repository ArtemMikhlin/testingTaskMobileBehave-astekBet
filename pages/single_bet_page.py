from selenium.webdriver.common.by import By
from pages.basic_page import BasicPage


class SingleBetPage(BasicPage):
    __LABEL_BALANCE_NAME = (By.ID, "org.astekbet.client:id/single_bet_balance_name")
    __FIELD_ENTER_AMOUNT = (By.ID, "org.astekbet.client:id/money_field_edit_text")
    __BUTTON_BET = (By.ID, "org.astekbet.client:id/make_bet")

    # alert
    __ALERT_MESSAGE = (By.ID, "android:id/message")

    def check_text_from_alert_not_enough_funds(self):
        self.check_text_from_element("Not enough funds in the account",
                                     "expected text doesn't match with actual", *self.__ALERT_MESSAGE)

    def check_page_visible(self):
        assert self.wait_element_present(*self.__LABEL_BALANCE_NAME) or\
               self.wait_element_present(*self.__BUTTON_BET) is True, "'single bet' screen isn't present"

    def input_amount(self, stake):
        self.input(stake, *self.__FIELD_ENTER_AMOUNT)

    def click_on_button_bet(self):
        self.click(*self.__BUTTON_BET)
