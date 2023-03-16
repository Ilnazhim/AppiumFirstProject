import datetime

from appium.webdriver.common.touch_action import TouchAction

number_auto = datetime.datetime.utcnow().strftime("%Y%H%M")
print(number_auto)

"""
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location([object Object], undefined)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(undefined, undefined)
actions.w3c_actions.pointer_action.release()
actions.perform()
    
"""

touch = TouchAction(driver)
touch.press(x=500, y=1700).move_to(x=500, y=500).release().perform()