from selenium.webdriver.common.by import By
from PageObjects.HomePage import Home
import pytest
import allure
from Utilities.logger import Logclass
from allure_commons.types import AttachmentType


class BasePage(Logclass):

    def __init__(self, driver):
        self.driver = driver


    # def assertion_equal(self, expected_string, actual_string):
    #     log = self.get_logs()
    #     try:
    #         assert actual_string == expected_string, log.info("#####Test case failed")
    #     finally:
    #         if AssertionError:
    #             print("Screenshot attached successfully")
    #             allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
    #                           attachment_type=AttachmentType.PNG)
