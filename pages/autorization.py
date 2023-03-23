import datetime

import allure
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import BaseClass


class AutorizationPage(BaseClass):

    # locators
    button_enter = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
    input_number = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText"
    button_next_1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"


    #Getters
    def get_button_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_enter)))

    def get_input_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_number)))

    def get_button_next_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_1)))

    #Actions
    def click_button_enter(self):
        self.get_button_enter().click()
        print("Click Enter button")

    def input_input_autorization_number(self):
        au_number = "89191153292"
        self.get_input_number().send_keys(au_number)
        print(f"Input number {au_number}")

    def click_button_next_1(self):
        self.get_button_next_1().click()


    #Metods
    def autorisation(self):
        with allure.step("autorisation"):
            self.click_button_enter()
            self.input_input_autorization_number()
            self.click_button_next_1()
