from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators
from helpers import wait_clickable


class TestConstructor:

    def test_go_to_sauces_section(self, driver):
        wait_clickable(driver, locators.SAUCES_TAB).click()
        
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(locators.ACTIVE_TAB, "Соусы"))


    def test_go_to_fillings_section(self, driver):
        wait_clickable(driver, locators.FILLINGS_TAB).click()
        
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(locators.ACTIVE_TAB, "Начинки"))


    def test_go_to_buns_section(self, driver):
        # «Булки» выбраны по умолчанию, поэтому сначала уходим на другую вкладку
        wait_clickable(driver, locators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(locators.ACTIVE_TAB, "Соусы"))
        wait_clickable(driver, locators.BUNS_TAB).click()
        
        assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(locators.ACTIVE_TAB, "Булки"))
            
