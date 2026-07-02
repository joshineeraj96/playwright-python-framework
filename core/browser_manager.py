from playwright.sync_api import sync_playwright
from utils.logger import get_logger

logger = get_logger(__name__)


class BrowserManager:

    @staticmethod
    def launch_browser(browser_name:str, headless:bool = False):
        playwright  = sync_playwright().start()

        if browser_name.lower() == "chromium":
            logger.info("Launching Chromium browser")
            browser = playwright.chromium.launch(headless=headless, args=["--start-maximized"])
            logger.info("Chromium browser launched")
        elif browser_name.lower() == "firefox":
            logger.info("Launching Firefox browser")
            browser = playwright.firefox.launch(headless=headless, args=["--start-maximized"])
            logger.info("Firefox browser launched")
        elif browser_name.lower() == "webkit":
            logger.info("Launching Webkit browser")
            browser = playwright.webkit.launch(headless=headless, args=["--start-maximized"])
            logger.info("Webkit browser launched")
        else:
            raise ValueError(f"Unsupported Browser:: {browser_name}")
        
        return playwright, browser