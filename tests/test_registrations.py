from pages.authorization_page import AuthorizationPage
from pages.main import MainPage
from pages.register_page import RegisterPage


def test_authorization(driver):
    print("\nAuthorization")
    rp = AuthorizationPage(driver)
    rp.main_authorization()
    mp = MainPage(driver)
    mp.confirm_main_page()


def test_register_without_auto_and_onboard(driver):
    print("\nRegistration")
    rp = RegisterPage(driver)
    rp.registration()
    rp.base_register()
    rp.no_auto_no_onboard()
    rp.close_popap()
    mp = MainPage(driver)
    mp.confirm_main_page()


def test_register_with_auto_and_onboard(driver):
    print("\nRegistration")
    rp = RegisterPage(driver)
    rp.registration()
    rp.base_register()
    rp.add_auto()
    rp.onboarding()
    rp.close_popap()
    mp = MainPage(driver)
    mp.confirm_main_page()
