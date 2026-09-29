import os
import re
from datetime import datetime

import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import test_data as data


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--window-size=1920,1080")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(2)
    yield driver
    driver.quit()


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.load()
    return page


@pytest.fixture
def inventory_page(driver, login_page):
    login_page.login(data.STANDARD_USER, data.PASSWORD)
    page = InventoryPage(driver)
    assert page.is_loaded()
    return page


@pytest.fixture
def checkout_page(driver, inventory_page):
    inventory_page.add_to_cart(data.PRODUCT_NAMES[0])
    inventory_page.open_cart()
    CartPage(driver).checkout()
    page = CheckoutInformationPage(driver)
    assert page.is_loaded()
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    driver = item.funcargs.get("driver")

    if report.when == "call" and report.failed and driver:
        os.makedirs("screenshots", exist_ok=True)
        name = re.sub(r"\W", "_", item.name)
        driver.save_screenshot(f"screenshots/{name}_{datetime.now():%H%M%S}.png")
