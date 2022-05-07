from selenium.webdriver.common.by import By
from pages.basic_page import BasicPage


class LaunchPage(BasicPage):
    __IMAGE_LOGO = (By.ID, "org.astekbet.client:id/app_logo")
    __LABEL_APP_VERSION = (By.ID, "org.astekbet.client:id/app_version")
    __LABEL_STATUS = (By.ID, "org.astekbet.client:id/status_text")
