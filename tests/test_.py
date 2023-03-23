from pages.autorization import AutorizationPage
from pages.burger import BurgerPage
from pages.forms import FormsPage
from pages.main import MainPage
from pages.map import MapPage
from pages.register_page import RegisterPage


# class Testregistrations:
def test_autorization(driver):
    print("\nAutorization")
    rp = AutorizationPage(driver)
    rp.autorisation()
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

# class TestForms:
def test_send_the_form_no_zhk(driver):
    print("\nNo ZhK form")
    rp = RegisterPage(driver)
    rp.registration()
    fp = FormsPage(driver)
    fp.fill_the_form_no_zhk()


# class TestBurger
def test_terms_of_use(driver):
    rp = AutorizationPage(driver)
    rp.autorisation()
    bp = BurgerPage(driver)
    bp.open_burger_menu()
    bp.see_terms()
    bp.open_burger_menu()
    bp.see_policy()
    bp.open_burger_menu()
    bp.see_rate_app()

# def test_see_raiting_zhk(driver):
#     mp = MapPage(driver)
#     mp.open_map()
#     mp.see_raiting()