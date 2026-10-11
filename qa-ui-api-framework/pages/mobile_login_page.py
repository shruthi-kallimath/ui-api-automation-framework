from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MobileLoginPage:
    OPEN_MENU = (AppiumBy.ACCESSIBILITY_ID, "open menu")
    LOGIN_MENU_ITEM = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Log In")'
    )
    USERNAME = (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    PASSWORD = (AppiumBy.ACCESSIBILITY_ID, "Password input field")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login button")
    PRODUCTS_HEADING = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("Products")'
    )
    ERROR_MESSAGE = (
        AppiumBy.XPATH,
        '//*[@content-desc="generic-error-message"]/android.widget.TextView'
    )
    LOGIN_SCREEN = (AppiumBy.ACCESSIBILITY_ID, "login screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open(self):
        self.wait.until(
            EC.element_to_be_clickable(self.OPEN_MENU)
        ).click()
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_MENU_ITEM)
        ).click()

    def login(self, username, password):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        password_field.clear()
        password_field.send_keys(password)

        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()

        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def is_products_page_displayed(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_HEADING)
        )
        return heading.is_displayed()

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return error.text

    def is_login_screen_displayed(self):
        screen = self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_SCREEN)
        )
        return screen.is_displayed()