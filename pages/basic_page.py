from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasicPage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, *element):
        e = self.driver.find_element(*element)
        e.click()

    def check_text_from_element(self, expected_text, error_message, *element):
        actual_text = self.driver.find_element(*element).text
        assert actual_text == expected_text, f"{error_message}, actual text is {actual_text}"

    def input(self, value, *element):
        e = self.driver.find_element(*element)
        e.clear()
        e.send_keys(value)

    def is_element_present(self, *element):
        try:
            self.driver.find_element(*element)
        except NoSuchElementException:
            return False
        return True

    def wait_element_present(self,  *element,  timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(element))
        except TimeoutException:
            return False

        return True

    def find_elements(self, *elements):
        return self.driver.find_elements(*elements)
