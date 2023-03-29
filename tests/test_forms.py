from pages.authorization_page import AuthorizationPage
from pages.burger_page import BurgerPage
from pages.first_page import FirstPage
from pages.forms_page import FormsPage
from pages.main import MainPage
from pages.register_page import RegisterPage


def test_send_the_form_no_zhk(driver):
    print("\nNo ZhK form")
    rp = RegisterPage(driver)
    rp.registration()
    fp = FormsPage(driver)
    fp.fill_the_form_no_zhk()
    fp = FirstPage(driver)
    fp.confirm_first_page()


def test_send_the_form_do_app_better_from_burger_menu(driver):
    print("\nDo app better form")
    rp = AuthorizationPage(driver)
    rp.authorization()
    mp = MainPage(driver)
    mp.open_burger_menu()
    bp = BurgerPage(driver)
    bp.open_feedback_form()
    fp = FormsPage(driver)
    fp.fill_the_form_do_app_better_from_burger()
    mp = MainPage(driver)
    mp.confirm_main_page()
