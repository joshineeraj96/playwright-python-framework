# Playwright Python Automation Framework

A scalable UI automation framework built using **Playwright**, **Python**, and **Pytest**, following industry-standard design principles. The framework is designed with maintainability, reusability, and scalability in mind, making it suitable for enterprise web application testing.

---

## 🚀 Tech Stack

* Python 3.12
* Playwright
* Pytest
* Allure Reporting
* Pytest-xdist (Parallel Execution)
* Pytest-rerunfailures
* Requests

---

## ✨ Features

* Page Object Model (POM)
* Centralized Browser Management
* Pytest Fixtures
* CLI Browser Selection
* Parallel Test Execution
* Automatic Screenshot Capture on Failure
* Playwright Trace Collection on Failure
* Allure Reporting
* Configurable Logging
* Automatic Cleanup of Test Artifacts
* Cross Browser Support (Chromium, Firefox, WebKit)

---

## 📁 Project Structure

```text
playwright-python-framework/
│
├── config/
├── core/
├── pages/
├── resources/
├── test_data/
├── tests/
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd playwright-python-framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

> Linux (recommended for CI)

```bash
playwright install-deps
```

---

## ▶️ Running Tests

Run all tests:

```bash
pytest
```

Run in headed mode:

```bash
pytest --headed
```

Run on Firefox:

```bash
pytest --browser firefox
```

Run a single test:

```bash
pytest tests/test_login.py::TestLogin::test_valid_login
```

Run tests in parallel:

```bash
pytest -n auto
```

---

## 📊 Reporting

Generate Allure results:

```bash
pytest --alluredir=artifacts/allure-results
```

View the Allure report:

```bash
allure serve artifacts/allure-results
```

---

## 📂 Test Artifacts

The framework automatically generates the following artifacts during execution:

```text
artifacts/
├── allure-results/
├── screenshots/
└── traces/
```

---

## 📌 Current Framework Capabilities

* Login Automation
* Dashboard Navigation
* Logout Validation
* Admin Navigation
* Screenshot Capture on Failure
* Playwright Trace Capture on Failure
* Allure Reporting
* Parallel Execution
* Browser Selection via CLI

---

## 🚧 Roadmap

- [ ] GitHub Actions CI/CD
- [ ] Smoke & Regression Test Suites
- [ ] API Automation Integration
- [ ] Environment Configuration
- [ ] Docker Support
- [ ] AI Testing Integration
- [ ] AI Agent-Based Test Automation

---

## 👨‍💻 Author

**Neeraj Joshi**
