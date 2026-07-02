from pages.base_page import BasePage
from playwright.sync_api import Page

class AdminPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.admin_heading = self.page.get_by_role('heading', name='Admin')
        