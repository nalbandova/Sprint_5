import locators
from helpers import wait_clickable, wait_visible


class TestLogout:

    def test_logout_from_personal_account(self, personal_account_driver):
        wait_clickable(personal_account_driver, locators.LOGOUT_BUTTON).click()

        assert wait_visible(personal_account_driver, locators.LOGIN_HEADER).is_displayed()
