# SauceDemo UI Tests

Selenium + Pytest tests for [saucedemo.com](https://www.saucedemo.com/), written with the Page Object Model.

## What is tested

- Login: valid login, wrong data, empty fields, locked user, logout
- Products: list, sorting, product details, cart
- Checkout: form validation, order totals, full purchase

## Structure

```
pages/    page classes (locators and actions)
tests/    the tests
utils/    test data
conftest.py    driver setup and fixtures
```

## Setup

```
pip install -r requirements.txt
```

You need Chrome installed. Selenium downloads the driver by itself.

## Run

```
pytest
pytest --headless
pytest --browser firefox
pytest -n 4
pytest -m smoke
```

The HTML report is saved in `reports/report.html` and screenshots of failed tests are saved in `screenshots/`.

## Author

Abdallah Ahmed Meaad - [GitHub](https://github.com/ABdallahMEaad) - [LinkedIn](https://www.linkedin.com/in/abdallah-meaad/)
