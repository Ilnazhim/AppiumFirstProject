from base.base_class import BaseClass
from pages.authorization_page import AuthorizationPage
from pages.main import MainPage
from pages.events_page import EventsPage


class TestEvents:

    def test_send_occ_event(self, driver):
        print("\nTest OCC event")
        rp = AuthorizationPage(driver)
        rp.authorization()

        mp = MainPage(driver)
        mp.click_occ()

        ep = EventsPage(driver)
        ep.input_name_occ()
        ep.fill_the_form_events()

        mp = MainPage(driver)
        mp.confirm_main_page()

    def test_send_meet_neighbor_event(self, driver):
        print("\nTest Meet event")
        rp = AuthorizationPage(driver)
        rp.authorization()

        mp = MainPage(driver)
        mp.click_meet_neighbor()

        ep = EventsPage(driver)
        ep.input_name_meet_neighbor()
        ep.fill_the_form_events()

        mp = MainPage(driver)
        mp.confirm_main_page()

    def test_send_sport_event(self, driver):
        print("\nTest Sport event")
        rp = AuthorizationPage(driver)
        rp.authorization()

        bp = BaseClass(driver)
        bp.do_scroll()
        bp.do_scroll()

        mp = MainPage(driver)
        mp.click_sport_event()

        ep = EventsPage(driver)
        ep.input_name_sport_event()
        ep.fill_the_form_events()

        mp = MainPage(driver)
        mp.confirm_main_page()
