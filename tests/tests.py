import time
import pytest

from pages.autorization import AutorizationPage
from pages.forms import FormsPage
from pages.map import MapPage
from pages.register_page import RegisterPage


# class Testregistrations:
def test_autorization(driver):
    print("\nAutorization")
    rp = AutorizationPage(driver)
    rp.autorisation()


def test_register_without_auto_and_onboard(driver):
    print("\nRegistration")
    rp = RegisterPage(driver)
    rp.registration()
    rp.base_register()
    rp.no_auto_no_onboard()
    rp.close_popap()


def test_register_with_auto_and_onboard(driver):
    print("\nRegistration")
    rp = RegisterPage(driver)
    rp.registration()
    rp.base_register()
    rp.add_auto()
    rp.onboarding()
    rp.close_popap()

# class TestForms:
def test_send_the_form_no_zhk(driver):
    print("\nNo ZhK form")
    rp = RegisterPage(driver)
    rp.registration()

    fp = FormsPage(driver)
    fp.fill_the_form_no_zhk()
    fp.send_the_form()

def test_see_raiting_zhk(driver):
    mp = MapPage(driver)
    mp.open_map()
    mp.see_raiting()
