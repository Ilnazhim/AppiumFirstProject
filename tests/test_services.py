from pages.autorization import AutorizationPage
from pages.main import MainPage
from pages.services_page import ServicesPage


def test_services_rent_apartament(driver):
    rp = AutorizationPage(driver)
    rp.autorisation()
    sp = ServicesPage(driver)
    sp.add_new_service()
    sp.add_rent_apartament()
    sp.fill_the_form_services()

    mp = MainPage(driver)
    mp.confirm_main_page()


