from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_class import BaseClass


class ServicesPage(BaseClass):

    # rent
    add_rent = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]"
    rent_apartament = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView"
    rent_auto = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.TextView"

    # sell
    add_sell = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView[1]"
    sell_apartament = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView"
    sell_park_place = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView"

    choose_studia = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView"
    input_square = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.widget.EditText"
    button_next = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"

    # other_services
    add_food = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.widget.TextView[1]"
    cake = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView"

    # feedback
    feedback_button = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[7]/android.view.ViewGroup/android.widget.TextView[2]"
    button_back_main = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup"

    input_name_services = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText"
    button_next_name = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"
    input_description = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText"
    button_next_desc = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"
    input_price = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.EditText"
    button_next_price = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"
    switch_auto_renewal = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup"
    send_service = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[4]/android.widget.TextView"

    button_service_well_done = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView"

    # Getters
    # rent
    def get_add_rent(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.add_rent)))

    def get_rent_apartament(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.rent_apartament)))

    def get_rent_auto(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.rent_auto)))

    # sell
    def get_add_sell(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.add_sell)))

    def get_sell_apartament(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.sell_apartament)))

    def get_sell_park_place(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.sell_park_place)))


    def get_choose_studia(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.choose_studia)))

    def get_input_square(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_square)))

    def get_button_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next)))

    # other_services
    def get_add_food(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.add_food)))

    def get_cake(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.cake)))

    # feedback
    def get_feedback_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.feedback_button)))

    def get_button_back_main(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_back_main)))

    # fill form
    def get_input_name_services(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_name_services)))

    def get_button_next_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_name)))

    def get_input_description(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_description)))

    def get_button_next_desc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_desc)))

    def get_input_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.input_price)))

    def get_button_next_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_next_price)))

    def get_switch_auto_renewal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.switch_auto_renewal)))

    def get_send_service(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.send_service)))

    def get_button_service_well_done(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, self.button_service_well_done)))

    #Actions
    # rent
    def click_add_rent(self):
        self.get_add_rent().click()
        print("Click add_rent")

    def click_rent_apartament(self):
        self.get_rent_apartament().click()
        print("Click rent_apartment")

    def click_rent_auto(self):
        self.get_rent_auto().click()
        print("Click rent_auto")

    # sell
    def click_add_sell(self):
        self.get_add_sell().click()
        print("Click add_sell")

    def click_sell_apartament(self):
        self.get_sell_apartament().click()
        print("Click sell_apartament")

    def click_sell_park_place(self):
        self.get_sell_park_place().click()
        print("Click sell_park_place")


    def click_choose_studia(self):
        self.get_choose_studia().click()
        print("Click choose_studia")

    def input_input_square(self, square):
        self.get_input_square().send_keys(square)
        print("input_square")

    def click_button_next(self):
        self.get_button_next().click()
        print("Click button_next")

    # other_services
    def click_add_food(self):
        self.get_add_food().click()
        print("Click add_food")

    def click_cake(self):
        self.get_cake().click()
        print("Click cake")

    # feedback
    def click_feedback_button(self):
        # time.sleep(2)
        self.get_feedback_button().click()
        print("Click feedback_button")

    def click_button_back_main(self):
        # time.sleep(2)
        self.get_button_back_main().click()
        print("Click button_back_main")


    def input_input_name_services(self, name):
        self.get_input_name_services().send_keys(name)
        print("input_name_services")

    def click_button_next_name(self):
        self.get_button_next_name().click()
        print("Click button_next_name")

    def input_input_description(self):
        self.get_input_description().send_keys("Описание автотест")
        print("input_description")

    def click_button_next_desc(self):
        self.get_button_next_desc().click()
        print("Click button_next_desc")

    def input_input_price(self):
        self.get_input_price().send_keys("555")
        print("input_price")

    def click_button_next_price(self):
        self.get_button_next_price().click()
        print("Click button_next_price")

    def click_switch_auto_renewal(self):
        self.get_switch_auto_renewal().click()
        print("Click switch_auto_renewal")

    def click_send_service(self):
        self.get_send_service().click()
        print("Click send_service")

    def click_button_service_well_done(self):
        self.get_button_service_well_done().click()
        print("Click button_service_well_done")


    # Metods
    """Аренда квартиры студии"""
    def add_rent_apartment(self):
        self.click_add_rent()
        time.sleep(1)
        self.click_rent_apartament()
        self.click_choose_studia()
        self.input_input_square("93")
        self.click_button_next()
        self.input_input_name_services("Аренда студии автотест")

    """Аренда автомобиля"""
    def add_rent_auto(self):
        self.click_add_rent()
        time.sleep(1)
        self.click_rent_auto()
        self.input_input_name_services("Аренда личного автомобиля автотест")

    """Продажа квартиры студии"""
    def add_sell_apartment(self):
        self.click_add_sell()
        time.sleep(1)
        self.click_sell_apartament()
        self.click_choose_studia()
        self.input_input_square("93")
        self.click_button_next()
        self.input_input_name_services("Продажа студии автотест")

    """Продажа парковочного места"""
    def add_sell_park_place(self):
        self.click_add_sell()
        time.sleep(1)
        self.click_sell_park_place()
        self.input_input_name_services("Продажа парковочного места автотест")

    """Еда на заказ"""
    def add_food_delivery(self):
        self.click_add_food()
        time.sleep(1)
        self.click_cake()
        self.input_input_name_services("Еда на заказ, торты автотест")

    """Заполнение общей формы услуги"""
    def fill_the_form_services(self):
        self.click_button_next_name()
        time.sleep(1)
        self.input_input_description()
        self.click_button_next_desc()
        self.input_input_price()
        self.click_button_next_price()
        self.click_switch_auto_renewal()
        self.click_send_service()
        self.click_button_service_well_done()
