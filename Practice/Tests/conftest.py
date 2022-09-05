import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def openbrowser(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    driver.maximize_window()
    request.cls.driver = driver
