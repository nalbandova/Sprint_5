import locators
from helpers import wait_clickable, wait_visible


class TestPersonalAccount:

    def test_go_to_personal_account(self, logged_in_driver):
        wait_clickable(logged_in_driver, locators.PERSONAL_ACCOUNT_BUTTON).click()

        assert wait_visible(logged_in_driver, locators.PROFILE_LINK).is_displayed()


    def test_go_to_constructor_by_constructor_button(self, personal_account_driver):
        wait_clickable(personal_account_driver, locators.CONSTRUCTOR_BUTTON).click()

        assert wait_visible(personal_account_driver, locators.CONSTRUCTOR_HEADER).is_displayed()


    def test_go_to_constructor_by_logo(self, personal_account_driver):
        wait_clickable(personal_account_driver, locators.LOGO).click()

        assert wait_visible(personal_account_driver, locators.CONSTRUCTOR_HEADER).is_displayed()
