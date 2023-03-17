import datetime
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import BaseClass


class MapPage(BaseClass):

    # locators
    button_raiting = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView"
    close_local = "com.android.permissioncontroller:id/permission_deny_button"
    close_popap_local2 = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView"



    #Getters
    def get_button_raiting(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_raiting)))

    def get_close_local(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, self.close_local)))

    def get_close_popap_local2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.close_popap_local2)))


    #Actions
    def click_button_raiting(self):
        self.get_button_raiting().click()
        print("Click button_raiting")

    def click_close_local(self):
        self.get_close_local().click()
        print("Click close_local")

    def click_close_popap_local2(self):
        self.get_close_popap_local2().click()
        print("Click close_popap_local2")


    #Metods
    def open_map(self):
        self.click_button_raiting()
        self.click_close_local()
        self.click_close_popap_local2()

    def see_raiting(self):
        self.do_tap()
"""
596 2079
"""