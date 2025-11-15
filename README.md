# SauceDemo Pytest Automation Framework

This repository contains an end-to-end automated testing framework for the **SauceDemo** web application using **Python**, **Pytest**, **Selenium WebDriver**, and **pytest-html** reporting.

The project implements **3 test scenarios** based on the provided user story and acceptance criteria.

---

# Features

### Scenario 1 — Successful Login  
Validates that a valid user (`standard_user`) can log in and is redirected to the inventory page with the app logo visible.

### Scenario 2 — Failed Login  
Validates that a banned/locked-out user (`locked_out_user`) receives the correct error message.

### Scenario 3 — Extract Inventory Data  
Logs in, extracts all item details from the Inventory page, saves them to JSON, logs out, and verifies redirection to the Login page.

### Additional Features  
- Selenium WebDriver setup using **webdriver-manager**
- Automatic **screenshots on test failure**
- **HTML reports** generated for every run
- Tests organized with **custom markers**: `success`, `failed`, `extract`
- Runs on any machine with **Python 3.8+**
- Fully automated installation using `requirements.txt`

---
### steps to run project
  1. Install Python 3.8+ and ensure `python` is on PATH.
  2. Open CMD and navigate to the project folder:
     cd /d C:\path to saucedemo_pytest_automation
  3. Run:
     run_tests.bat
     
# Project Structure

saucedemo_pytest_automation/
│
├── conftest.py # WebDriver setup, fixtures, report hooks
├── utils.py # Helper methods (login, element-checking)
├── requirements.txt # All dependencies (pinned versions)
├── pytest.ini # Custom markers & pytest config
├── run_tests.bat # Windows test runner script
├── run_tests.sh # Linux/Mac test runner
├── README.md # Project documentation
│
└── tests/
├── test_success_login.py
├── test_failed_login.py
└── test_extract_and_logout.py
