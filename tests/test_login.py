from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from playwright.sync_api import Page, expect
from test_data import login_data
import allure

class TestLogin:

    @allure.feature("Login")
    @allure.title("Verify login pass with valid credentials")
    def test_valid_login(self, page: Page):
        login_page = LoginPage(page)
        dashboard_page = DashboardPage(page)
        login_page.login(login_data.USERNAME, login_data.PASSWORD)
        expect(dashboard_page.dashboard_heading).to_be_visible()

    @allure.feature("Login")
    @allure.title("Verify login fails with invalid username")
    def test_invalid_username(self, page: Page):
        login_page = LoginPage(page)
        login_page.login(login_data.INVALID_USERNAME, login_data.PASSWORD)
        expect(login_page.login_error).to_have_text('invalid credentials')

    @allure.feature("Login")
    @allure.title("Verify login fails with invalid password")
    def test_invalid_password(self, page: Page):
        login_page = LoginPage(page)
        login_page.login(login_data.USERNAME, login_data.INVALID_PASSWORD)
        expect(login_page.login_error).to_have_text('Invalid credentials')
    