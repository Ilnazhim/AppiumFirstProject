from pages.authorization_page import AuthorizationPage
from pages.help_4_page import Help4Page
from pages.main import MainPage
from pages.register_page import RegisterPage


def test_search_owner_of_car(driver):
    print("\nTest cars owner")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.click_search_car()

    hp = Help4Page(driver)
    hp.open_search_car_owner()
    hp.neighbor_found()

    mp = MainPage(driver)
    mp.confirm_main_page()


