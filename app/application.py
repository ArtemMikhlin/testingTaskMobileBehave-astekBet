from pages.basic_page import BasicPage
from pages.launch_page import LaunchPage
from pages.main_page import EventsPage
from pages.registration_type_page import RegistrationTypePage
from pages.one_click_registration_page import OneClickRegistrationPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.single_bet_page import SingleBetPage


class Application:

    def __init__(self, driver):
        self.basic_page = BasicPage(driver)
        self.launch_page = LaunchPage(driver)
        self.events_page = EventsPage(driver)
        self.registration_type_page = RegistrationTypePage(driver)
        self.one_click_registration_page = OneClickRegistrationPage(driver)
        self.login_page = LoginPage(driver)
        self.my_account_page = MyAccountPage(driver)
        self.single_bet_page = SingleBetPage(driver)
