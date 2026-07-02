from pages.base_page import BasePage
from playwright.sync_api import Page
from utils.logger import get_logger

logger = get_logger(__name__)

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_heading = self.page.get_by_role("heading", name="Dashboard")
        self.user_menu = self.page.get_by_alt_text("profile picture")
        self.logout_menu_item = self.page.get_by_role("menuitem", name="Logout")


    def click_user_menu(self):
        logger.info("Clicking User Menu")
        self.user_menu.click()
    
    def click_logout(self):
        logger.info("Clicking Logout button")
        self.logout_menu_item.click()

    def logout(self):
        self.click_user_menu()
        self.click_logout()

    def navigate_to(self, menu_name: str):
        logger.info(f"Navigating to {menu_name} Page")
        self.page.get_by_role('link', name=menu_name).click()