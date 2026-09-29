import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from utils import test_data as data


@pytest.mark.smoke
def test_valid_login(driver, login_page):
    login_page.login(data.STANDARD_USER, data.PASSWORD)

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()
    assert "inventory.html" in driver.current_url


def test_wrong_password(login_page):
    login_page.login(data.STANDARD_USER, "wrong_password")
    assert login_page.get_error() == data.WRONG_CREDENTIALS


def test_unknown_username(login_page):
    login_page.login("unknown_user", data.PASSWORD)
    assert login_page.get_error() == data.WRONG_CREDENTIALS


def test_empty_username(login_page):
    login_page.login("", data.PASSWORD)
    assert login_page.get_error() == data.USERNAME_REQUIRED


def test_empty_password(login_page):
    login_page.login(data.STANDARD_USER, "")
    assert login_page.get_error() == data.PASSWORD_REQUIRED


def test_empty_username_and_password(login_page):
    login_page.login("", "")
    assert login_page.get_error() == data.USERNAME_REQUIRED


def test_locked_out_user(driver, login_page):
    login_page.login(data.LOCKED_USER, data.PASSWORD)
    assert login_page.get_error() == data.LOCKED_OUT
    assert "inventory.html" not in driver.current_url


def test_close_error_message(login_page):
    login_page.login("", "")
    assert login_page.error_shown()
    login_page.close_error()
    assert login_page.error_hidden()


@pytest.mark.smoke
def test_logout(driver, inventory_page):
    inventory_page.logout()

    login = LoginPage(driver)
    assert login.is_loaded()
    assert driver.current_url == LoginPage.base_url


def test_open_inventory_without_login(driver):
    InventoryPage(driver).open()

    login = LoginPage(driver)
    assert login.get_error() == data.NOT_LOGGED_IN
