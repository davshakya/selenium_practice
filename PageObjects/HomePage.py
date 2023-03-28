from selenium.webdriver.common.by import By


class Home:
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

    def input_text(self,user_name):
        self.driver.find_element(By.XPATH, self.set_text).send_keys(user_name)
