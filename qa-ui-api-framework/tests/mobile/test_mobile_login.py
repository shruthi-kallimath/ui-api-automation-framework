from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login(mobile_driver):
    driver = mobile_driver
    wait = WebDriverWait(driver, 20)

    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "open menu")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR,
         'new UiSelector().text("Log In")')
    )).click()

    username = wait.until(EC.visibility_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    ))
    username.clear()
    username.send_keys("bob@example.com")

    password = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Password input field"
    )
    password.clear()
    password.send_keys("10203040")

    if driver.is_keyboard_shown():
        driver.hide_keyboard()

    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Login button")
    )).click()

    products_heading = wait.until(EC.visibility_of_element_located(
        (AppiumBy.ANDROID_UIAUTOMATOR,
         'new UiSelector().text("Products")')
    ))
    assert products_heading.is_displayed()


def test_invalid_login(mobile_driver):
    driver = mobile_driver
    wait = WebDriverWait(driver, 20)

    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "open menu")
    )).click()

    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ANDROID_UIAUTOMATOR,
         'new UiSelector().text("Log In")')
    )).click()

    username = wait.until(EC.visibility_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, "Username input field")
    ))
    username.clear()
    username.send_keys("bob@example.com")

    password = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "Password input field"
    )
    password.clear()
    password.send_keys("wrongpassword")

    if driver.is_keyboard_shown():
        driver.hide_keyboard()

    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Login button")
    )).click()

    error = wait.until(EC.visibility_of_element_located(
        (AppiumBy.XPATH,
         '//*[@content-desc="generic-error-message"]'
         '/android.widget.TextView')
    ))
    assert error.text == (
        "Provided credentials do not match any user in this service."
    )

    assert driver.find_element(
        AppiumBy.ACCESSIBILITY_ID, "login screen"
    ).is_displayed()