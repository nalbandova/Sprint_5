import locators
from data import FORGOT_PASSWORD_URL, LOGIN_URL, REGISTER_URL
from helpers import fill_login_form, wait_clickable, wait_visible


def test_login_by_main_page_button(driver, user):
    wait_clickable(driver, locators.LOGIN_BUTTON_MAIN).click()
    fill_login_form(driver, user["email"], user["password"])

    assert wait_visible(driver, locators.ORDER_BUTTON).is_displayed()


def test_login_by_personal_account_button(driver, user):
    wait_clickable(driver, locators.PERSONAL_ACCOUNT_BUTTON).click()
    fill_login_form(driver, user["email"], user["password"])

    assert wait_visible(driver, locators.ORDER_BUTTON).is_displayed()


def test_login_by_button_in_registration_form(driver, user):
    driver.get(REGISTER_URL)
    wait_clickable(driver, locators.LOGIN_LINK).click()
    fill_login_form(driver, user["email"], user["password"])

    assert wait_visible(driver, locators.ORDER_BUTTON).is_displayed()


def test_login_by_button_in_forgot_password_form(driver, user):
    driver.get(FORGOT_PASSWORD_URL)
    wait_clickable(driver, locators.LOGIN_LINK).click()
    fill_login_form(driver, user["email"], user["password"])

    assert wait_visible(driver, locators.ORDER_BUTTON).is_displayed()
