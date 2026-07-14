import pytest
import allure

from core.browser_manager import BrowserManager
from config import config
from utils.logger import configure_logger, get_logger
from utils.screenshot import take_screenshot
from pathlib import Path
from utils.file_manager import clean_directory
from utils.file_naming import unique_name

configure_logger()
logger = get_logger(__name__)


pytest_plugins = [
    "tests.fixtures.auth_fixture",
    "tests.fixtures.booking_fixture",
    "tests.fixtures.mock_api_fixture",
]


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium")
    parser.addoption("--headed", action="store_true")


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    is_headed = request.config.getoption("--headed")

    playwright, browser = BrowserManager.launch_browser(browser_name, headless=not is_headed)
   
    yield browser, playwright

    logger.info("Closing Browser")
    browser.close()

    logger.info("Stopping Playwright")
    playwright.stop()


@pytest.fixture(scope="session")
def api_context(browser):

    _, playwright = browser

    logger.info("Creating API Request Context")

    request_context = playwright.request.new_context(base_url=config.API_BASE_URL)

    yield request_context

    logger.info("Disposing API Request Context")
    request_context.dispose()


@pytest.fixture(scope="function")
def context(request, browser):
    browser_instance, _ = browser
    context = browser_instance.new_context(no_viewport=True)

    # start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    # save tracing and stop it if test fail else stop it without saving.
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        trace_dir = Path("artifacts/traces")
        trace_dir.mkdir(parents=True, exist_ok=True)

        trace_path = trace_dir / unique_name(request.node.name, "zip")

        context.tracing.stop(path=trace_path)

        allure.attach.file(
                str(trace_path),
                name="Playwright Trace",
                attachment_type=allure.attachment_type.ZIP
        )

        logger.info(f"Trace saved: {trace_path}")

    else:
        context.tracing.stop()

    context.close()


@pytest.fixture(scope="function")
def page(request, context):
    page = context.new_page()

    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(60000)

    logger.info(f"Navigating to {config.BASE_URL}")
    page.goto(config.BASE_URL, wait_until="domcontentloaded")
    logger.info("Navigation completed")

    setattr(request.node, "page", page)

    yield page

    page.close()


def pytest_runtest_logstart(nodeid, location):
    logger.info("=" * 80)
    logger.info(f"STARTING TEST: {nodeid}")
    logger.info("=" * 80)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Save the report on the current test
    setattr(item, f"rep_{rep.when}", rep)

     # Execute only after the test body has run
    if rep.when == "call" and rep.failed:

        page = getattr(item, "page", None)

        if page:
            screenshot_path = take_screenshot(page, item.name)

            allure.attach.file(
                str(screenshot_path),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            logger.error(f"Screenshot captured: {item.name}.png")


def pytest_sessionstart(session):
    clean_directory("artifacts/screenshots")
    clean_directory("artifacts/traces")
    clean_directory("artifacts/allure-results")