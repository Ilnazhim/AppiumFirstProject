import datetime

import allure
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from base.base_class import BaseClass
from pages.data import DataPage


class FirstPage(BaseClass):

    # locators
    #no ZhK form
    first_page_text = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.TextView"

    #Getters
    # no ZhK form
    def get_no_zhk(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.no_zhk)))

    #Actions

    #Metods
    def confirm_first_page(self):
        get_first_page_text =AppiumBy.XPATH, self.first_page_text
        self.assert_element_has_text(get_first_page_text, text="Экосистема")
        print("Экосистема SosediService для комфортной жизни")

