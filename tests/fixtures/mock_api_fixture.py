import pytest

from utils.logger import get_logger

logger = get_logger(__name__)


@pytest.fixture(scope="session")
def mock_api_context(browser):

    _, playwright = browser

    logger.info("Creating Mock API Request Context")

    request_context = playwright.request.new_context(
        base_url="http://localhost:8080"
    )

    yield request_context

    logger.info("Disposing Mock API Request Context")
    request_context.dispose()