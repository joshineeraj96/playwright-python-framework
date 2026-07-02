from pathlib import Path
from utils.file_naming import unique_name

def take_screenshot(page, test_name):
    screenshot_dir = Path("artifacts/screenshots")
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    filename = unique_name(test_name, "png")
    screenshot_path = screenshot_dir / filename

    page.screenshot(path=screenshot_path, full_page=True)

    return screenshot_path