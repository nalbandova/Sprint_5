import pytest
from selenium import webdriver

import locators
from data import LOGIN_URL, MAIN_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD
from helpers import fill_login_form, wait_clickable, wait_visible


@pytest.fixture
def driver():
    """Открывает Chrome на главной странице и закрывает его после теста."""
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.get(MAIN_URL)
    yield browser
    browser.quit()


@pytest.fixture
def user():
    """Email и пароль тестового пользователя."""
    return {"email": TEST_USER_EMAIL, "password": TEST_USER_PASSWORD}


@pytest.fixture
def logged_in_driver(driver, user):
    """Браузер с уже выполненным входом в аккаунт."""
    driver.get(LOGIN_URL)
    fill_login_form(driver, user["email"], user["password"])
    wait_visible(driver, locators.ORDER_BUTTON)
    return driver


@pytest.fixture
def personal_account_driver(logged_in_driver):
    """Браузер, в котором выполнен вход и открыт личный кабинет."""
    wait_clickable(logged_in_driver, locators.PERSONAL_ACCOUNT_BUTTON).click()
    wait_visible(logged_in_driver, locators.PROFILE_LINK)
    return logged_in_driver
