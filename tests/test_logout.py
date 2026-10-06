import locators
from helpers import wait_clickable, wait_visible


def test_logout_from_personal_account(logged_in_driver):
    driver = logged_in_driver
    wait_clickable(driver, locators.PERSONAL_ACCOUNT_BUTTON).click()
    wait_clickable(driver, locators.LOGOUT_BUTTON).click()

    assert wait_visible(driver, locators.LOGIN_HEADER).is_displayed()
