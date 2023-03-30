from pages.authorization_page import AuthorizationPage
from pages.help_4_page import Help4Page
from pages.main import MainPage


def test_send_help_get_on_the_way(driver):
    print("\nTest get on the way")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.click_get_on_the_way()

    hp = Help4Page(driver)
    hp.open_way_to_house()

    mp = MainPage(driver)
    mp.click_get_on_the_way()

    hp = Help4Page(driver)
    hp.open_way_from_house()


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


def test_search_neighbor(driver):
    print("\nTest search neighbor")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.click_search_neighbor()

    hp = Help4Page(driver)
    hp.open_search_neighbor()
    hp.neighbor_found()

    mp = MainPage(driver)
    mp.confirm_main_page()


def test_loud_noise_neighbor(driver):
    print("\nTest loud noise")
    rp = AuthorizationPage(driver)
    rp.authorization()

    mp = MainPage(driver)
    mp.click_loud_noise()

    hp = Help4Page(driver)
    hp.open_search_neighbor()
    hp.neighbor_loud_noise()

    mp = MainPage(driver)
    mp.confirm_main_page()
