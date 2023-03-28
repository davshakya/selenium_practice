import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def setup(request):
    request.cls.driver = webdriver.Chrome(executable_path="c:\work\chromedriver.exe")
    request.cls.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    request.cls.driver.maximize_window()
    yield
    time.sleep(5)
    request.cls.driver.quit()

