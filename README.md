# Playwright Python Test Automation Framework

A production-inspired, scalable, and maintainable test automation framework built using **Playwright**, **Python**, and **Pytest** for both **UI** and **API** testing.

This project demonstrates enterprise-level automation practices including **Page Object Model (POM)**, reusable API client architecture, data-driven testing, centralized browser management, configurable fixtures, robust reporting, parallel execution, and GitHub Actions CI/CD.

The framework has been designed with a strong focus on **maintainability**, **reusability**, **scalability**, and **clean architecture**, making it suitable for modern web application testing and showcasing enterprise automation engineering practices and scalable framework design.

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
        UI                 API
         │                  │
         ▼                  ▼
   Page Objects       API Clients
         │                  │
         └──────┬───────────┘
                ▼
        Pytest Fixtures
                │
      Browser / API Context
                │
          Playwright Engine
                │
    Allure | Logs | Screenshots
                │
        GitHub Actions CI
```

The framework follows a layered architecture that separates concerns between test logic, business actions, infrastructure, and reporting.

- UI tests interact only with Page Objects.
- API tests communicate through reusable API Clients.
- Fixtures manage browser, API context, authentication, and resource lifecycle.
- Configuration and environment management remain centralized.
- Reporting, screenshots, traces, and logs are automatically generated during execution.

This separation improves readability, simplifies maintenance, and allows the framework to scale as additional modules and test suites are introduced.


---

## ⭐ Framework Highlights

✔ Enterprise-style folder structure

✔ UI & API Automation in a single framework

✔ Reusable Page Object Model

✔ Generic API Client Architecture

✔ Browser Context Isolation

✔ Parallel Test Execution

✔ Cross Browser Testing

✔ Automatic Screenshot & Trace Capture

✔ JSON Schema Validation

✔ WireMock Integration

✔ GitHub Actions CI/CD

✔ Allure Reporting

✔ Environment Variable Management

✔ Data-Driven Testing

✔ Scalable and Maintainable Design


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

- Session-scoped browser to minimize browser startup overhead and improve execution speed.
- Function-scoped browser contexts to ensure complete isolation between test cases and eliminate shared state.
- Generic API client to reduce duplicated request logic and simplify the addition of new endpoints.
- Environment variables for secure credential management and easier deployment across environments.
- JSON-based test data to separate test logic from test data and improve maintainability.
- Pytest fixtures to manage test dependencies and resource lifecycle.
- Automatic screenshots and Playwright traces only on failures to simplify debugging while minimizing storage.
- GitHub Actions to enable automated execution and continuous validation on every code change.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/joshineeraj96/playwright-python-framework.git
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

Senior SDET | Automation Test Engineer

Specializing in Playwright, Python, API Automation, and AI Testing.

GitHub:
https://github.com/joshineeraj96

LinkedIn:
https://www.linkedin.com/in/neeraj-joshi-60855b99