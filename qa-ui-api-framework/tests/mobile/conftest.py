import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def mobile_driver():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android Emulator",
        "udid": "emulator-5554",
        "appPackage": "com.saucelabs.mydemoapp.rn",
        "appActivity": ".MainActivity",
        "noReset": False,
    })

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options,
    )

    try:
        try:
            ok_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                     'new UiSelector().text("OK")')
                )
            )
        except TimeoutException:
            pass  # The startup popup did not appear.
        else:
            ok_button.click()

        yield driver
    finally:
        driver.quit()