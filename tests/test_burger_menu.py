import pytest

from pages.authorization_page import AuthorizationPage
from pages.burger_page import BurgerPage
from pages.main import MainPage
from pages.register_page import RegisterPage


def test_see_instructions_from_burger_menu(driver):
    print("\nTest onboarding")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.open_burger_menu()

    bp = BurgerPage(driver)
    bp.see_instructions_burger()

    rp = RegisterPage(driver)
    rp.onboarding()

    mp = MainPage(driver)
    mp.confirm_main_page()


@pytest.mark.xfail
def test_terms_of_use_agreement(driver):
    print("\nTest agreement")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.open_burger_menu()

    bp = BurgerPage(driver)
    bp.see_terms()

    mp = MainPage(driver)
    mp.open_burger_menu()

    bp = BurgerPage(driver)
    bp.see_policy()

    mp = MainPage(driver)
    mp.open_burger_menu()

    bp = BurgerPage(driver)
    bp.see_rate_app()
