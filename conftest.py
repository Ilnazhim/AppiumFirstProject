import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def driver():
    desired_cap = {
        "deviceName": "ZY225FGPXH",
        "platformName": "Android",
        "app": "C:\\Users\\ilnazhim\\builds\\app-release32.apk",
        "automationName": "uiautomator2",
        "appPackage": "",
        "appWaitActivity": ""
    }
    print("\nstart browser for test..")
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

    yield driver
