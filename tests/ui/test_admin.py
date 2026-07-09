from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from test_data import login_data
import allure
import pytest

class TestAdmin:

    @pytest.mark.regression
    @allure.feature("Admin")
    @allure.title("Verify user can navigate to Admin page")
    def test_navigate_to_admin(self, page: Page):
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        admin_page = AdminPage(page)

        login_page.login(login_data.USERNAME, login_data.PASSWORD)

        dashboard_page.navigate_to('Admin')
        expect(admin_page.admin_heading).to_be_visible()