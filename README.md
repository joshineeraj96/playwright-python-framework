# Playwright Python Test Automation Framework

A scalable and maintainable test automation framework built with Playwright, Python, and Pytest, supporting both UI and API testing.

The framework demonstrates industry-standard automation practices, including the Page Object Model, reusable API client architecture, data-driven testing, parallel execution, Allure reporting, and GitHub Actions CI/CD.


---

## 🚀 Tech Stack

- Python 3.12
- Playwright
- Pytest
- Allure Reporting
- Pytest-xdist (Parallel Execution)
- Pytest-rerunfailures
- Faker
- JSON Schema Validation
- WireMock
- GitHub Actions

---

## ✨ Framework Features

- UI Automation using Page Object Model (POM)
- API Automation using Playwright APIRequestContext
- Reusable API Client Architecture
- Reusable Authentication Fixtures
- JSON Schema Validation
- WireMock Integration
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
      ┌───────────────┴───────────────┐
      ▼                               ▼
Page Objects                  API Clients
      │                               │
      └───────────────┬───────────────┘
                      ▼
              Pytest Fixtures
                      │
          Browser / API Context
                      │
                 Playwright
```

The framework follows a layered architecture where UI tests interact with Page Objects while API tests interact with reusable API Clients. Both layers leverage shared Pytest fixtures and Playwright for efficient, maintainable, and scalable test automation.

---

## 📁 Project Structure

```text
playwright-python-framework/
│
├── api/
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

- Page Object Model to improve maintainability and reduce code duplication.
- Session-scoped browser to reduce execution time.
- Function-scoped browser context for complete test isolation.
- Environment variables for sensitive credentials.
- JSON-based data-driven testing for better separation of test data and test logic.
- Pytest fixtures for resource lifecycle management.
- Failure-only screenshots and Playwright traces for efficient debugging.
- GitHub Actions for automated CI execution.
- Generic API client to promote code reuse and maintainability.
- Authentication handled through reusable fixtures to support multiple authentication mechanisms.


---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/playwright-python-framework.git
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

Additional environment variables can be added as required for different environments.

---

## ▶️ Running Tests

### Run All Tests

```bash
pytest
```

# Run only API tests
```bash
pytest tests/api
```

# Run only UI tests
```bash
pytest tests/ui
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

### UI Automation

- Login
- Logout
- Dashboard
- Admin

### API Automation

- Authentication
- Booking CRUD Operations
- JSON Schema Validation
- Mock API Testing (WireMock)
- Positive & Negative API Test Scenarios

The framework is designed to scale by simply adding new Page Objects and test modules.

---


## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Neeraj Joshi**

Senior SDET | Playwright | Python | API Automation | AI Testing