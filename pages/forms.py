import datetime
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import BaseClass


class FormsPage(BaseClass):

    # locators
    no_zhk = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
    choose_town = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"
    input_number = ""
    input_number = ""


    #Getters
    def get_no_zhk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.no_zhk)))

    def get_input_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_number)))

    def get_button_next_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_1)))

    def get_input_town(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_town)))

    def get_button_next_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_2)))

    def get_input_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_street)))

    def get_button_next_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_3)))

    def get_button_next_4(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_4)))

    def get_input_appart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_appart)))

    def get_button_next_5(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_5)))

    def get_input_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_name)))

    def get_button_next_6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_6)))

    def get_button_no_auto(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_no_auto)))

    def get_button_no_onboard(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_no_onboard)))

    def get_close_popap_otzyv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.close_popap_otzyv)))



    #Actions
    def click_button_enter(self):
        self.get_button_enter().click()
        print("Click Enter button")

    def input_input_number(self):
        now = datetime.datetime.utcnow().strftime("%d%H%M%S")
        self.get_input_number().send_keys("891" + str(now))
        print("Input number")

    def click_button_next_1(self):
        self.get_button_next_1().click()
        print("Click button Next 1")

    def input_input_town(self):
        self.get_input_town().send_keys("Челябинск")
        print("Input Town")

    def click_button_next_2(self):
        self.get_button_next_2().click()
        print("Click button Next 2")

    def input_input_street(self):
        self.get_input_street().send_keys("Рязанская улица, 20")
        print("Input Street")

    def click_button_next_3(self):
        self.get_button_next_3().click()
        print("Click button Next 3")

    def click_button_next_4(self):
        self.get_button_next_4().click()
        print("Click button Next 4")

    def input_input_appart(self):
        appart = datetime.datetime.utcnow().strftime("%H%M%S")
        self.get_input_appart().send_keys(appart)
        print("Input number of Appartament")

    def click_button_next_5(self):
        self.get_button_next_5().click()
        print("Click button Next 5")

    def input_input_name(self):
        name = datetime.datetime.utcnow().strftime("%d.%m.%Y..%H:%M")
        self.get_input_appart().send_keys("Автотест регистрация" + str(name))
        print("Input Name")

    def click_button_next_6(self):
        self.get_button_next_6().click()
        print("Click button Next 6")

    def click_button_no_auto(self):
        self.get_button_no_auto().click()
        print("Click button No Auto")

    def click_button_no_onboard(self):
        self.get_button_no_onboard().click()
        print("Click button No Onbording")

    def click_close_popap_otzyv(self):
        self.get_close_popap_otzyv().click()
        print("Click button No Onbording")



    #Metods
    def register(self):
        self.click_button_enter()
        self.input_input_number()
        self.click_button_next_1()
        time.sleep(7)
        self.input_input_town()
        time.sleep(3)
        self.click_button_next_2()
        time.sleep(3)
        self.input_input_street()
        self.click_button_next_3()
        self.click_button_next_4()
        time.sleep(3)
        self.input_input_appart()
        self.click_button_next_5()
        time.sleep(3)
        self.input_input_name()
        self.click_button_next_6()
        self.click_button_no_auto()
        self.click_button_no_onboard()
        self.click_close_popap_otzyv()
