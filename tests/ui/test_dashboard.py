from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from test_data import login_data
import allure
import pytest

class TestDashboard:

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.feature("Dashboard")
    @allure.title("Verify user can logout successfully")
    def test_logout(self, page: Page):
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)

        login_page.login(login_data.USERNAME, login_data.PASSWORD)
        dashboard_page.logout()

        expect(login_page.login_button).to_be_visible()

