import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("ORANGEHRM_USERNAME")
PASSWORD = os.getenv("ORANGEHRM_PASSWORD")

if USERNAME is None or PASSWORD is None:
    raise RuntimeError(
        "ORANGEHRM_USERNAME and ORANGEHRM_PASSWORD are not configured. "
        "Configure them using a local .env file or GitHub Actions Secrets."
    )

INVALID_USERNAME = "abcde"
INVALID_PASSWORD = "abc@123"
BLANK_USERNAME = "  "
BLANK_PASSWORD = "  "