# SauceDemo – Playwright Automation

## Project Overview
This project contains Python-based UI automation tests for the SauceDemo application using Playwright and pytest.

## Tools and Technologies
- Python
- Playwright
- Pytest
- Pytest HTML

## Automated Test Scenarios

| Test Scenario | Description |
|---|---|
| Valid Login | Verify successful login with valid credentials |
| Invalid Login | Verify error message for incorrect credentials |
| Blank Login | Verify validation when both fields are empty |
| Blank Username | Verify validation when username is empty |
| Blank Password | Verify validation when password is empty |

## Framework Structure

```text
Automation/
├── .gitignore
├── conftest.py
├── requirements.txt
├── README.md
├── reports/
│   └── login-report.html
└── tests/
    └── test_login.py
```

## Execution

Install dependencies:

```bash
pip install -r requirements.txt
playwright install chromium
```

Run all login tests:

```bash
pytest tests/test_login.py -v
```

Generate an HTML report:

```bash
pytest tests/test_login.py -v --html=reports/login-report.html --self-contained-html
```

## Test Results
All five login scenarios passed during the latest local execution.

## Project Purpose
This is an independent QA learning and portfolio project demonstrating practical UI automation skills. It is not professional employment experience.