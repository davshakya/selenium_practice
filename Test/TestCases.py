from PageObjects.HomePage import Home
import pytest
import allure
from Utilities.logger import Logclass

@pytest.mark.usefixtures("setup")
class TestUiPractice(Logclass):
    @allure.description("Testing input textbox of RM infotech page")
    @allure.severity(severity_level="Critical")
    def test_set_text(self):
        log = self.get_logs()
        hp = Home(self.driver)
        entered_text = hp.input_text("Devendra Shakya")
        hp.assertion_equal("Devendra Shakya", entered_text)
        log.info("test_set_text case passed")

    @allure.description("Testing checkbox of RM infotech page")
    @allure.severity(severity_level="Normal")
    def test_checkboxes(self):
        log = self.get_logs()
        hp = Home(self.driver)
        hp.enable_checkbox()
        hp.is_element_enabled()
        log.info("test_checkboxes case passed")

    # def test_switch_windows(self):
    #     log = self.get_logs()
    #     hp = Home(self.driver)
    #     main = self.driver.window_handles[0]
    #     current_title = self.driver.title
    #     print(current_title)
    #     assert current_title == "Practice Page"
    #     self.driver.find_element(By.XPATH, hp.open_window).click()
    #     w1 = self.driver.window_handles[1]
    #     self.driver.switch_to.window(w1)
    #     self.driver.maximize_window()
    #     self.driver.find_element(By.XPATH, "//div[@id='navbarSupportedContent']//a[contains(text(),'Courses')]").click()
    #     time.sleep(5)
    #     self.driver.close()
    #     self.driver.switch_to.window(main)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "//a[@id='opentab']").click()
    #     t1 = self.driver.window_handles[1]
    #     self.driver.switch_to.window(t1)
    #     self.driver.find_element(By.XPATH, "//a[contains(text(),'JOIN NOW')]").click()
    #     self.driver.close()
    #     log.info("test_switch_windows case passed")
