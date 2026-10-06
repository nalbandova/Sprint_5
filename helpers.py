import random
import string

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators
from data import EMAIL_DOMAIN

WAIT_TIMEOUT = 10


def generate_email():
    """Генерирует логин (email) вида abc123@yandex.ru: 3 буквы и 3 цифры."""
    letters = "".join(random.choices(string.ascii_lowercase, k=3))
    digits = "".join(random.choices(string.digits, k=3))
    return f"{letters}{digits}@{EMAIL_DOMAIN}"


def generate_password(length=6):
    """Генерирует пароль из букв и цифр. По умолчанию 6 символов (минимум для сервиса)."""
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choices(chars, k=length))


def wait_visible(driver, locator):
    """Ждёт, пока элемент появится на странице, и возвращает его."""
    return WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.visibility_of_element_located(locator)
    )


def wait_clickable(driver, locator):
    """Ждёт, пока элемент станет кликабельным, и возвращает его."""
    return WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.element_to_be_clickable(locator)
    )


def fill_registration_form(driver, name, email, password):
    """Заполняет форму регистрации и нажимает «Зарегистрироваться»."""
    wait_visible(driver, locators.REGISTER_NAME_INPUT).send_keys(name)
    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    wait_clickable(driver, locators.REGISTER_SUBMIT_BUTTON).click()


def fill_login_form(driver, email, password):
    """Заполняет форму входа и нажимает «Войти»."""
    wait_visible(driver, locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    wait_clickable(driver, locators.LOGIN_SUBMIT_BUTTON).click()
