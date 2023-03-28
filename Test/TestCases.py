import time
from selenium.webdriver.common.by import By
from PageObjects.HomePage import Home
import pytest
from Utilities.logger import Logclass


@pytest.mark.usefixtures("setup")
class TestUiPractice(Logclass):
    def test_set_text(self):
        log = self.get_logs()
        hp = Home(self.driver)
        hp.input_text("Devendra Shakya")
        log.info("Entered user name")
        entered_text = self.driver.find_element(By.XPATH, hp.set_text).get_attribute("value")
        print("entered_text" + "=" + entered_text)
        assert entered_text == "Devendra Shakya", log.info("#####Test case failed")
        log.info("test_set_text case passed")

    def test_checkboxes(self):
        log = self.get_logs()
        hp = Home(self.driver)
        self.driver.find_element(By.XPATH, hp.checkbox1).click()
        self.driver.find_element(By.XPATH, hp.checkbox2).click()
        self.driver.find_element(By.XPATH, hp.checkbox3).click()
        is_checkbox_enabled = self.driver.find_element(By.XPATH, hp.checkbox3).is_selected()
        assert is_checkbox_enabled == True
        log.info("test_checkboxes case passed")

    def test_switch_windows(self):
        log = self.get_logs()
        hp = Home(self.driver)
        main = self.driver.window_handles[0]
        current_title = self.driver.title
        print(current_title)
        assert current_title == "Practice Page"
        self.driver.find_element(By.XPATH, hp.open_window).click()
        w1 = self.driver.window_handles[1]
        self.driver.switch_to.window(w1)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//div[@id='navbarSupportedContent']//a[contains(text(),'Courses')]").click()
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(main)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@id='opentab']").click()
        t1 = self.driver.window_handles[1]
        self.driver.switch_to.window(t1)
        self.driver.find_element(By.XPATH, "//a[contains(text(),'JOIN NOW')]").click()
        self.driver.close()
        log.info("test_switch_windows case passed")
