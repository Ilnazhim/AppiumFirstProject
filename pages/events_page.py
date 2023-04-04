import time

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
from selenium.common import NoSuchElementException, TimeoutException

from pages.main import MainPage


class EventsPage(BaseClass):

    # locators
    input_event_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.EditText"
    input_event_address = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.EditText"
    button_date = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView"
    choose_date_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
    button_time = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView"
    button_send_event = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.widget.TextView"
    button_ok = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"

    # Getters
    def get_input_event_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_event_name)))

    def get_input_event_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_event_address)))

    def get_button_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_date)))

    def get_choose_date_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.choose_date_time)))

    def get_button_time(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_time)))

    def get_button_send_event(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_send_event)))

    def get_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_ok)))

    # Actions
    def input_input_event_name(self, event_name):
        self.get_input_event_name().send_keys(event_name)
        print("input_event_name")

    def input_input_event_address(self):
        self.get_input_event_address().send_keys("Авто двор")
        print("input_station")

    def click_button_date(self):
        self.get_button_date().click()
        print("Click button_date")

    def click_choose_date_time(self):
        self.get_choose_date_time().click()
        print("Click choose_date_time")

    def click_button_time(self):
        self.get_button_time().click()
        print("Click button_time")

    def click_button_send_event(self):
        self.get_button_send_event().click()
        print("Click button_send_event")

    def click_button_ok(self):
        self.get_button_ok().click()
        print("Click button_ok")

    # Metods
    def input_name_occ(self):
        with allure.step("input_name_occ"):
            self.input_input_event_name("Автотест ОСС")

    def input_name_meet_neighbor(self):
        with allure.step("input_name_meet_neighbor"):
            self.input_input_event_name("Автотест Сбор соседей")

    def input_name_sport_event(self):
        with allure.step("input_name_sport_event"):
            self.input_input_event_name("Автотест Спортивное мероприятие")

    def fill_the_form_events(self):
        with allure.step("fill_the_form_events"):
            self.input_input_event_address()
            self.click_button_date()
            self.click_choose_date_time()
            self.click_button_time()
            self.click_choose_date_time()
            self.click_button_send_event()
            time.sleep(1)
            self.click_button_ok()
