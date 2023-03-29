import datetime

import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import BaseClass


class Help4Page(BaseClass):

    # locators
    # get on the way

    # search neighbor
    input_number = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.EditText"
    button_search_owner = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView"

    text_owner_found = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]"
    button_close_popap = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"

    text_ad_published = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]"
    button_well_ad = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
    button_write = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.widget.TextView"
    button_call = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.widget.TextView"



    #Getters
    def get_input_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_number)))

    def get_button_search_owner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_search_owner)))

    def get_button_close_popap(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_close_popap)))

    #Actions
    def input_input_number(self, number):
        self.get_input_number().send_keys(number)
        print("Input number")

    def click_button_search_owner(self):
        self.get_button_search_owner().click()
        print("Click button_search_owner")

    def click_button_close_popap(self):
        self.get_button_close_popap().click()
        print("Click button_close_popap")

    #Metods
    def open_search_car_owner(self):
        with allure.step("search_car_owner"):
            self.input_input_number("с613ва174")
            self.click_button_search_owner()

    def neighbor_found(self):
        get_popap_text = AppiumBy.XPATH, self.text_owner_found
        self.assert_element_has_text(get_popap_text, text="найден")
        print("Сосед найден!")
        self.click_button_close_popap()
