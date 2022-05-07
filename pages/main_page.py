from selenium.webdriver.common.by import By
from pages.basic_page import BasicPage


class EventsPage(BasicPage):
    __BUTTON_BURGER = (By.CLASS_NAME, "android.widget.ImageButton")
    __TOOLBAR = (By.ID, "org.astekbet.client:id/toolbar")
    __FRAME_LIVE_TOP = (By.ID, "org.astekbet.client:id/live_top_title")
    __FRAME_PRE_MATCH_TOP = (By.ID, "org.astekbet.client: id / line_top_title")
    __FIELD_BETTING_ODDS = (By.ID, "org.astekbet.client:id/recycler_view")

    # Menu
    __OPTION_REGISTRATION = (By.ID, "org.astekbet.client:id/drawer_menu_registration")
    __OPTION_MY_ACCOUNT = (By.ID, "org.astekbet.client:id/root_layout")
    __OPTION_LOG_IN = (By.ID, "org.astekbet.client:id/drawer_menu_authorization")
    __OPTION_LOG_OUT = (By.ID, "org.astekbet.client:id/logout_item_drawer")

    # Betting odds bottomsheet
    __FRAME_BETTING_ODDS = (By.ID, "org.astekbet.client:id/design_bottom_sheet")
    __OPTION_PLACE_BET = (By.ID, "org.astekbet.client:id/makeBetTextView")

    # alert logout
    __TEXTVIEW_TITLE = (By.ID, "org.astekbet.client:id/alertTitle")
    __BUTTON_YES = (By.ID, "android:id/button1")

    def check_page_visible(self):
        assert self.wait_element_present(*self.__FRAME_LIVE_TOP) or \
               self.wait_element_present(*self.__FRAME_PRE_MATCH_TOP) \
               is True, "events screen isn't present" \


    def check_bottomsheet_betting_odds_visible(self):
        assert self.wait_element_present(*self.__FRAME_BETTING_ODDS) is True, \
            "betting odds bottomsheet isn't present"

    def check_title_from_alert_logout(self):
        self.check_text_from_element("Log out", "expected text doesn't match with actual", *self.__TEXTVIEW_TITLE)

    def click_on_button_yes_from_alert(self):
        self.click(*self.__BUTTON_YES)

    def click_on_burger_button(self):
        self.click(*self.__BUTTON_BURGER)

    def click_on_field_betting_odds(self):
        self.click(*self.__FIELD_BETTING_ODDS)

    def click_on_registration_option(self):
        self.click(*self.__OPTION_REGISTRATION)

    def click_on_login_option(self):
        self.click(*self.__OPTION_LOG_IN)

    def click_on_logout_option(self):
        self.click(*self.__OPTION_LOG_OUT)

    def click_on_my_account_option(self):
        self.click(*self.__OPTION_MY_ACCOUNT)

    def click_on_place_bet_option(self):
        self.click(*self.__OPTION_PLACE_BET)
