from appium import webdriver
from app.application import Application
import os


def before_scenario(context, scenario):
    path_to_folder = os.getcwd()
    desired_capabilities = {"platformName": "Android",
                            "app": fr"{path_to_folder}\data\apk\test.apk"}
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
