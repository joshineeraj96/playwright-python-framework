import json
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("ORANGEHRM_USERNAME")
PASSWORD = os.getenv("ORANGEHRM_PASSWORD")

if USERNAME is None or PASSWORD is None:
    raise RuntimeError(
        "ORANGEHRM_USERNAME and ORANGEHRM_PASSWORD are not configured. "
        "Configure them using a local .env file or GitHub Actions Secrets."
    )

json_file = Path(__file__).parent / "login_data.json"

with open(json_file, encoding="utf-8") as file:
    INVALID_LOGIN_DATA = json.load(file)["invalid_login_data"]