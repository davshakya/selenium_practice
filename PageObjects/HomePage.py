from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
from Utilities.logger import Logclass


class Home(Logclass):
    def __init__(self, driver):
        self.driver = driver
        self.checkbox1 = "//input[@id='checkBoxOption1']"
        self.checkbox2 = "//input[@id='checkBoxOption2']"
        self.checkbox3 = "//input[@id='checkBoxOption3']"
        self.open_window = "//button[@id='openwindow']"
        self.set_text = "//input[@id='name']"
        self.dropdown = "//*[@id='dropdown-class-example']"
        self.dropdown_option1 = "//*[@id='dropdown-class-example']/option[2]"
        self.dropdown_option2 = "//*[@id='dropdown-class-example']/option[3]"
        self.dropdown_option3 = "//*[@id='dropdown-class-example']/option[4]"

    def input_text(self, user_name):
        log = self.get_logs()
        self.driver.find_element(By.XPATH, self.set_text).send_keys(user_name)
        entered_text = self.driver.find_element(By.XPATH, self.set_text).get_attribute("value")
        log.info("Entered user name")
        return entered_text

    def enable_checkbox(self):
        self.driver.find_element(By.XPATH, self.checkbox1).click()
        self.driver.find_element(By.XPATH, self.checkbox2).click()
        self.driver.find_element(By.XPATH, self.checkbox3).click()

    def is_element_enabled(self):
        is_checkbox_enabled = self.driver.find_element(By.XPATH, self.checkbox3).is_selected()
        try:
            assert is_checkbox_enabled == True
        finally:
            if AssertionError:
                print("Screenshot attached successfully")
                allure.attach(self.driver.get_screenshot_as_png(), name="CheckBox status",
                              attachment_type=AttachmentType.PNG)

    def assertion_equal(self, expected_string, actual_string):
        log = self.get_logs()
        try:
            assert actual_string == expected_string, log.info("#####Test case failed")
        finally:
            if AssertionError:
                print("Screenshot attached successfully")
                allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                              attachment_type=AttachmentType.PNG)
