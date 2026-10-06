import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators
from data import LOGIN_URL, MAIN_URL, REGISTER_URL, USER_NAME
from helpers import (
    fill_login_form,
    fill_registration_form,
    generate_email,
    generate_password,
    wait_visible,
)


@pytest.fixture
def driver():
    """Открывает Chrome на главной странице и закрывает его после теста."""
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.get(MAIN_URL)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def user():
    """Регистрирует нового пользователя (один раз за запуск) и возвращает его email и пароль."""
    email = generate_email()
    password = generate_password()
    browser = webdriver.Chrome()
    try:
        browser.set_window_size(1920, 1080)
        browser.get(REGISTER_URL)
        fill_registration_form(browser, USER_NAME, email, password)
        WebDriverWait(browser, 10).until(EC.url_to_be(LOGIN_URL))
    finally:
        browser.quit()
    return {"email": email, "password": password}


@pytest.fixture
def logged_in_driver(driver, user):
    """Браузер с уже выполненным входом в аккаунт."""
    driver.get(LOGIN_URL)
    fill_login_form(driver, user["email"], user["password"])
    wait_visible(driver, locators.ORDER_BUTTON)
    return driver
