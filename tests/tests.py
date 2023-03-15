import time

from pages.register_page import RegisterPage


def test_register_without_auto_and_onboard(driver):

    print("\nDo register")
    rp = RegisterPage(driver)
    rp.register()


