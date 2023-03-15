import time

from pages.register_page import RegisterPage

# class Testregistrations:
def test_register_without_auto_and_onboard(driver):

    print("\nAutorization")
    rp = RegisterPage(driver)
    rp.autorization()
    rp.base_register()
    rp.no_auto_no_onboard()
    rp.close_popap()


def test_register_with_auto_and_onboard(driver):
    print("\nAutorization")
    rp = RegisterPage(driver)
    rp.autorization()
    rp.base_register()
    rp.add_auto()
    rp.onboarding()
    rp.close_popap()

