# Playwright Python Automation Framework

A production-ready UI automation framework built with Playwright, Python, and Pytest.

The framework demonstrates modern automation engineering practices including scalable architecture, data-driven testing, parallel execution, CI/CD integration, and maintainable test design commonly adopted in enterprise projects.

---

## 🚀 Tech Stack

- Python 3.12
- Playwright
- Pytest
- Allure Reporting
- Pytest-xdist (Parallel Execution)
- Pytest-rerunfailures
- GitHub Actions

---

## ✨ Framework Features

- Page Object Model (POM)
- Centralized Browser Management
- Session & Function Scoped Pytest Fixtures
- Cross Browser Support
- Command Line Browser Selection
- JSON Data-Driven Testing
- Pytest Parameterization
- Smoke, Sanity & Regression Test Markers
- Automatic Screenshot Capture on Failure
- Playwright Trace Capture on Failure
- Allure Reporting & Attachments
- Configurable Logging
- Environment Variable Based Credential Management
- Automatic Cleanup of Test Artifacts
- GitHub Actions CI Pipeline

---

## 🏗️ Framework Architecture

```text
Tests
   │
   ▼
Page Objects
   │
   ▼
Browser / Context / Page Fixtures
   │
   ▼
Browser Manager
   │
   ▼
Playwright
```

The framework follows a layered architecture where test cases interact with Page Objects, which in turn use shared browser fixtures and the Browser Manager to communicate with Playwright.

---

## 📁 Project Structure

```text
playwright-python-framework/
│
├── artifacts/
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

## 📌 Design Decisions

This framework follows several design principles commonly adopted in enterprise automation projects.

- Page Object Model to separate UI interactions from test logic.
- Session-scoped browser to reduce execution time.
- Function-scoped browser context for complete test isolation.
- Environment variables for sensitive credentials.
- JSON-based data-driven testing for better separation of test data and test logic.
- Pytest fixtures for resource lifecycle management.
- Failure-only screenshots and Playwright traces for efficient debugging.
- GitHub Actions for automated CI execution.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone git clone https://github.com/your-username/playwright-python-framework.git
cd playwright-python-framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

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

## 🔐 Environment Configuration

Create a `.env` file in the project root.

```text
ORANGEHRM_USERNAME=your_username
ORANGEHRM_PASSWORD=your_password
```

Sensitive credentials should never be committed to source control.

---

## ▶️ Running Tests

### Run All Tests

```bash
pytest
```

### Run in Headed Mode

```bash
pytest --headed
```

### Run on Firefox

```bash
pytest --browser firefox
```

### Run a Single Test

```bash
pytest tests/test_login.py::TestLogin::test_valid_login
```

### Run Tests in Parallel

```bash
pytest -n auto
```

### Run Smoke Tests

```bash
pytest -m smoke
```

### Run Sanity Tests

```bash
pytest -m sanity
```

### Run Regression Tests

```bash
pytest -m regression
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

## 📂 Generated Artifacts

During execution the framework automatically generates:

```text
artifacts/
├── allure-results/
├── screenshots/
└── traces/
```

---

## 📈 Current Coverage

- Login Module
- Logout Module
- Dashboard Module
- Admin Module

The framework is designed to scale by simply adding new Page Objects and test modules.

---

## 🚧 Roadmap

- [x] UI Automation Framework
- [x] JSON Data-Driven Testing
- [x] Parameterization
- [x] Test Markers
- [x] GitHub Actions CI/CD
- [ ] API Automation Integration
- [ ] Unified UI + API Framework
- [ ] Docker Support

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Neeraj Joshi**

Senior Automation Test Engineer

Python | Playwright | API Automation | AI Testing Enthusiast