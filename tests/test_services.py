from pages.authorization_page import AuthorizationPage
from pages.main import MainPage
from pages.services_page import ServicesPage


def test_services_rent_apartment(driver):
    print("\nTest rent apartment")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.add_new_service()

    sp = ServicesPage(driver)
    sp.add_rent_apartment()
    sp.fill_the_form_services()

    mp = MainPage(driver)
    mp.confirm_main_page()


# def test_services_rent_auto(driver):
#     print("\nTest rent auto")
#     rp = AuthorizationPage(driver)
#     rp.authorization()
#
#     mp = MainPage(driver)
#     mp.add_new_service()
#
#     sp = ServicesPage(driver)
#     sp.add_rent_auto()
#     sp.fill_the_form_services()
#
#     mp = MainPage(driver)
#     mp.confirm_main_page()


def test_services_sell_apartment(driver):
    print("\nTest sell apartment")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.add_new_service()

    sp = ServicesPage(driver)
    sp.add_sell_apartment()
    sp.fill_the_form_services()

    mp = MainPage(driver)
    mp.confirm_main_page()

#
# def test_services_sell_park_place(driver):
#     print("\nTest sell park place")
#     rp = AuthorizationPage(driver)
#     rp.authorization()
#
#     mp = MainPage(driver)
#     mp.add_new_service()
#
#     sp = ServicesPage(driver)
#     sp.add_sell_park_place()
#     sp.fill_the_form_services()
#
#     mp = MainPage(driver)
#     mp.confirm_main_page()


def test_services_food_delivery(driver):
    print("\nTest food delivery")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.add_new_service()

    sp = ServicesPage(driver)
    sp.add_food_delivery()
    sp.fill_the_form_services()

    mp = MainPage(driver)
    mp.confirm_main_page()
