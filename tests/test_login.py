import allure
import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page, expect
from test_data import login_data

class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.feature("Login")
    @allure.title("Verify login pass with valid credentials")
    def test_valid_login(self, page: Page):
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        login_page.login(login_data.USERNAME, login_data.PASSWORD)
        expect(dashboard_page.dashboard_heading).to_be_visible()

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.feature("Login")
    @allure.title("Verify login fails with invalid credentials")
    @pytest.mark.parametrize("user", [pytest.param(user, id=user["id"]) for user in login_data.INVALID_LOGIN_DATA])
    def test_invalid_login(self, page: Page, user):
        login_page = LoginPage(page)
        login_page.login(user["username"], user["password"])
        expect(login_page.login_error).to_be_visible()
        expect(login_page.login_error).to_have_text('Invalid credentials')
