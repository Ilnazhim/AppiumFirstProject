import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import BaseClass
from pages.data import DataPage


class AuthorizationPage(BaseClass):

    # locators
    button_enter = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"
    input_number = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText"
    button_next_1 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"

    # Getters
    def get_button_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_enter)))

    def get_input_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_number)))

    def get_button_next_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_1)))

    # Actions
    def click_button_enter(self):
        self.get_button_enter().click()
        print("Click Enter button")

    def input_input_authorization_number(self, acc_number):
        self.get_input_number().send_keys(acc_number)
        print("Input number")

    def click_button_next_1(self):
        self.get_button_next_1().click()

    #Metods
    def main_authorization(self):
        with allure.step("main authorization"):
            self.click_button_enter()
            self.input_input_authorization_number(*DataPage.main_account)
            self.click_button_next_1()

    def second_authorization(self):
        with allure.step("second authorization"):
            self.click_button_enter()
            self.input_input_authorization_number(*DataPage.second_account)
            self.click_button_next_1()