from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators
from data import LOGIN_URL, REGISTER_URL, USER_NAME
from helpers import (
    fill_registration_form,
    generate_email,
    generate_password,
    wait_visible,
)


def test_successful_registration(driver):
    driver.get(REGISTER_URL)
    fill_registration_form(driver, USER_NAME, generate_email(), generate_password())

    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
    assert wait_visible(driver, locators.LOGIN_HEADER).is_displayed()


def test_registration_with_short_password_shows_error(driver):
    driver.get(REGISTER_URL)
    fill_registration_form(driver, USER_NAME, generate_email(), generate_password(5))

    assert wait_visible(driver, locators.PASSWORD_ERROR).is_displayed()
