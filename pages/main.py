import datetime

import allure
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import BaseClass


class MainPage(BaseClass):

    # locators
    hello_text = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView"

    burger_menu =  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup"

    # 4 helps
    get_on_the_way = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]"
    search_car = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]"
    search_neighbor = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]"
    loud_noise = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]"

    #services
    button_add_services = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup"

    #Getters
    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.burger_menu)))

    def get_get_on_the_way(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.get_on_the_way)))

    def get_search_car(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.search_car)))

    def get_search_neighbor(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.get_search_neighbor)))

    def get_loud_noise(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.loud_noise)))

    def get_button_add_services(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_add_services)))

    #Actions
    def click_burger_menu(self):
        self.get_burger_menu().click()
        print("Click burger_menu")

    def click_get_on_the_way(self):
        self.get_get_on_the_way().click()
        print("Click get_on_the_way")

    def click_search_car(self):
        self.get_search_car().click()
        print("Click search_car")

    def click_search_neighbor(self):
        self.get_search_neighbor().click()
        print("Click search_neighbor")

    def click_loud_noise(self):
        self.get_loud_noise().click()
        print("Click loud_noise")

    def click_button_add_services(self):
        self.get_button_add_services().click()
        print("Click button_add_services")


    #Metods
    def confirm_main_page(self):
        get_hello_text = AppiumBy.XPATH, self.hello_text
        self.assert_element_has_text(get_hello_text, text="Привет")
        print("Привет, сосед!")

    def add_new_service(self):
        self.click_button_add_services()

    def open_burger_menu(self):
        with allure.step("open_burger_menu"):
            time.sleep(1)
            self.click_burger_menu()
