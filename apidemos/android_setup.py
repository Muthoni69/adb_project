from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput #For creating a 'finger' input device
from selenium.webdriver.common.actions.action_builder import ActionBuilder #For creating an action sequence
from selenium.webdriver.common.actions import interaction

import time

class AndroidSetup:
    def __init__(self):
        options = UiAutomator2Options()

        # Set desired capabilities
        options.platform_name = "Android"
        options.platform_version = "15"
        options.device_name = "emulator-5554"
        options.app = "C:\\Users\\v-puritynjau\\MobileApps\\ApiDemos-debug.apk"
        options.automation_name = "UiAutomator2"

        #Connect to Appium Server
        self.driver = webdriver.Remote("http://localhost:4723", options = options)

        self.screen_size = self.driver.get_window_size()
        self.width = self.screen_size['width']
        self.height = self.screen_size['height']

    def tearDown(self):
        self.driver.quit()

    def navigate_to_photos(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Views").click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Gallery").click()
        time.sleep(1)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Photos").click()
        time.sleep(2)

    def swipe(self, start_x, start_y, end_x, end_y):
        actions = ActionChains(self.driver)
        pointer = PointerInput(interaction.POINTER_TOUCH, "finger")
        action_builder = ActionBuilder(self.driver, mouse = pointer)

        # Move to start position
        action_builder.pointer_action.move_to_location(x=int(start_x), y=int(start_y))
        # Press down
        action_builder.pointer_action.pointer_down()
        # short pause to ensure down action is registered.
        action_builder.pointer_action.pause(10)
        # Move to end position
        action_builder.pointer_action.move_to_location(x=int(end_x), y=int(end_y))
        # Release
        action_builder.pointer_action.pointer_up()

        actions.perform()


    def scroll_down(self, percentage=.8):
        # Performs a scroll down action.
        start_x = self.width / 2
        start_y = self.height * 0.2
        end_y = self.height * percentage
        self.swipe(start_x, start_y, start_x, end_y)





