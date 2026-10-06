from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators
from helpers import wait_clickable


def check_active_tab(driver, tab_name):
    """Ждёт, пока выбранной вкладкой станет tab_name, и проверяет это."""
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(locators.ACTIVE_TAB, tab_name)
    )
    assert driver.find_element(*locators.ACTIVE_TAB).text == tab_name


def test_go_to_sauces_section(driver):
    wait_clickable(driver, locators.SAUCES_TAB).click()

    check_active_tab(driver, "Соусы")


def test_go_to_fillings_section(driver):
    wait_clickable(driver, locators.FILLINGS_TAB).click()

    check_active_tab(driver, "Начинки")


def test_go_to_buns_section(driver):
    # «Булки» выбраны по умолчанию, поэтому сначала уходим на другую вкладку
    wait_clickable(driver, locators.SAUCES_TAB).click()
    check_active_tab(driver, "Соусы")
    wait_clickable(driver, locators.BUNS_TAB).click()

    check_active_tab(driver, "Булки")
