from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators
from helpers import wait_clickable, wait_visible


def test_go_to_personal_account(logged_in_driver):
    driver = logged_in_driver
    wait_clickable(driver, locators.PERSONAL_ACCOUNT_BUTTON).click()

    assert wait_visible(driver, locators.PROFILE_LINK).is_displayed()


def test_go_to_constructor_by_constructor_button(logged_in_driver):
    driver = logged_in_driver
    wait_clickable(driver, locators.PERSONAL_ACCOUNT_BUTTON).click()
    wait_visible(driver, locators.PROFILE_LINK)
    wait_clickable(driver, locators.CONSTRUCTOR_BUTTON).click()

    assert wait_visible(driver, locators.CONSTRUCTOR_HEADER).is_displayed()


def test_go_to_constructor_by_logo(logged_in_driver):
    driver = logged_in_driver
    wait_clickable(driver, locators.PERSONAL_ACCOUNT_BUTTON).click()
    wait_visible(driver, locators.PROFILE_LINK)
    wait_clickable(driver, locators.LOGO).click()

    assert wait_visible(driver, locators.CONSTRUCTOR_HEADER).is_displayed()


def test_logout_from_personal_account(logged_in_driver):
    driver = logged_in_driver
    wait_clickable(driver, locators.PERSONAL_ACCOUNT_BUTTON).click()
    wait_clickable(driver, locators.LOGOUT_BUTTON).click()

    assert wait_visible(driver, locators.LOGIN_HEADER).is_displayed()
