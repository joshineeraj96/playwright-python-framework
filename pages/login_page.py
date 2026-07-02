from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.login_error = self.page.get_by_role('alert')

    def enter_username(self, username):
        logger.info("Entering username")
        self.username_input.fill(username)

    def enter_password(self, password):
        logger.info("Entering password")
        self.password_input.fill(password)

    def click_login(self):
        logger.info("Clicking Login button")
        self.login_button.click()

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()



        