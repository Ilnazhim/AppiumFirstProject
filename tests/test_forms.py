from pages.authorization_page import AuthorizationPage
from pages.burger_page import BurgerPage
from pages.first_page import FirstPage
from pages.forms_page import FormsPage
from pages.main import MainPage
from pages.register_page import RegisterPage
from base.base_class import BaseClass
from pages.services_page import ServicesPage


def test_send_the_form_no_zhk(driver):
    print("\nNo ZhK form")
    rp = RegisterPage(driver)
    rp.registration()

    fp = FormsPage(driver)
    fp.fill_the_form_no_zhk()
    fp = FirstPage(driver)
    fp.confirm_first_page()


def test_send_the_form_do_app_better_from_burger_menu(driver):
    print("\nDo app better form burger menu")
    rp = AuthorizationPage(driver)
    rp.main_authorization()

    mp = MainPage(driver)
    mp.open_burger_menu()

    bp = BurgerPage(driver)
    bp.open_feedback_form()

    fp = FormsPage(driver)
    fp.fill_the_form_do_app_better()

    mp = MainPage(driver)
    mp.confirm_main_page()


def test_send_the_form_do_app_better_from_services(driver):
    print("\nDo app better form services")
    rp = AuthorizationPage(driver)
    rp.main_authorization()

    mp = MainPage(driver)
    mp.add_new_service()

    bp = BaseClass(driver)
    bp.do_scroll()
    bp.do_scroll()
    bp.do_scroll()

    sp = ServicesPage(driver)
    sp.click_feedback_button()
    #
    # fp = FormsPage(driver)
    # fp.fill_the_form_do_app_better()
    #
    # sp = ServicesPage(driver)
    # sp.click_button_back_main()
    #
    # mp = MainPage(driver)
    # mp.confirm_main_page()
