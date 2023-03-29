import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
from selenium.common import NoSuchElementException, TimeoutException

from pages.main import MainPage


class Help4Page(BaseClass):

    # locators
    # get on the way
    way_to_house = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
    way_from_house = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView"
    input_station = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText"
    choose_station = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
    button_send_help = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView"
    resubmission_error = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]"
    button_back_to_main_if_error = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup"
    hello_text = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.TextView"

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
    def get_way_to_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.way_to_house)))

    def get_way_from_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.way_from_house)))

    def get_input_station(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_station)))

    def get_choose_station(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.choose_station)))

    def get_resubmission_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.resubmission_error)))

    def get_button_back_to_main_if_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_back_to_main_if_error)))


    def get_button_send_help(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_send_help)))

    def get_input_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_number)))

    def get_button_search_owner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_search_owner)))

    def get_button_close_popap(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_close_popap)))

    def get_button_well_ad(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_well_ad)))

    #Actions
    def click_way_to_house(self):
        self.get_way_to_house().click()
        print("Click way_to_house")

    def click_way_from_house(self):
        self.get_way_from_house().click()
        print("Click way_from_house")

    def input_input_station(self, station):
        self.get_input_station().send_keys(station)
        print("input_station")

    def click_choose_station(self):
        self.get_choose_station().click()
        print("Click choose_station")

    def click_button_back_to_main_if_error(self):
        self.get_button_back_to_main_if_error().click()
        print("Click button_back_to_main_if_error")

    def click_button_send_help(self):
        self.get_button_send_help().click()
        print("Click button_send_help")

    def input_input_number(self, number):
        self.get_input_number().send_keys(number)
        print("Input number")

    def click_button_search_owner(self):
        self.get_button_search_owner().click()
        print("Click button_search_owner")

    def click_button_close_popap(self):
        self.get_button_close_popap().click()
        print("Click button_close_popap")

    def click_button_well_ad(self):
        self.get_button_well_ad().click()
        print("Click button_well_ad")

    # Metods
    def open_way_to_house(self):
        with allure.step("way_to_house"):
            try:
                self.click_way_to_house()
                self.input_input_station("Нагат")
                self.click_choose_station()
                self.click_button_send_help()
                self.confirm_main_page_for_helps()
            except TimeoutException:
                print("Help already was send, please try  in 20 minutes")
                self.click_button_back_to_main_if_error()

    def open_way_from_house(self):
        with allure.step("way_from_house"):
            try:
                self.click_way_from_house()
                self.input_input_station("ленин")
                self.click_choose_station()
                self.click_button_send_help()
                self.confirm_main_page_for_helps()
            except TimeoutException:
                print("Help already was send, please try  in 20 minutes")
                self.click_button_back_to_main_if_error()

    def confirm_main_page_for_helps(self):
        with allure.step("way_from_house"):
            get_hello_text = AppiumBy.XPATH, self.hello_text
            self.assert_element_has_text(get_hello_text, text="Привет")
            print("Привет, сосед!")

    def open_search_car_owner(self):
        with allure.step("search_car_owner"):
            self.input_input_number("с613ва174")
            self.click_button_search_owner()

    def open_search_neighbor(self):
        with allure.step("search_neighbor"):
            self.input_input_number("56")
            self.click_button_search_owner()

    def open_loud_noise_neighbor(self):
        with allure.step("loud_noise_neighbor"):
            self.input_input_number("56")
            self.click_button_search_owner()

    def neighbor_found(self):
        with allure.step("neighbor_found"):
            get_popap_text = AppiumBy.XPATH, self.text_owner_found
            self.assert_element_has_text(get_popap_text, text="найден")
            print("Сосед найден!")
            self.click_button_close_popap()

    def neighbor_loud_noise(self):
        with allure.step("loud_noise"):
            get_popap_text = AppiumBy.XPATH, self.text_ad_published
            self.assert_element_has_text(get_popap_text, text="опубликовано")
            print("Ваша просьба сделать потише отправлена соседу")
            self.click_button_well_ad()
