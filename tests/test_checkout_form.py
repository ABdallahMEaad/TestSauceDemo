import pytest

from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from utils import test_data as data


@pytest.mark.parametrize("first, last, postal, error", [
    ("", "Meaad", "12345", data.FIRST_NAME_REQUIRED),
    ("Abdallah", "", "12345", data.LAST_NAME_REQUIRED),
    ("Abdallah", "Meaad", "", data.POSTAL_CODE_REQUIRED),
    ("", "", "", data.FIRST_NAME_REQUIRED),
])
def test_required_fields(checkout_page, first, last, postal, error):
    checkout_page.fill_form(first, last, postal)
    checkout_page.continue_checkout()
    assert checkout_page.get_error() == error


@pytest.mark.smoke
def test_valid_form(driver, checkout_page):
    checkout_page.fill_form(**data.CHECKOUT_INFO)
    checkout_page.continue_checkout()
    assert CheckoutOverviewPage(driver).is_loaded()


def test_cancel(driver, checkout_page):
    checkout_page.cancel()
    assert CartPage(driver).is_loaded()


def test_order_totals(driver, inventory_page):
    added = inventory_page.add_first_items(2)
    inventory_page.open_cart()
    CartPage(driver).checkout()

    info = CheckoutInformationPage(driver)
    info.fill_form(**data.CHECKOUT_INFO)
    info.continue_checkout()

    overview = CheckoutOverviewPage(driver)
    assert overview.is_loaded()

    expected = round(sum(data.PRODUCTS[name] for name in added), 2)
    assert overview.get_subtotal() == pytest.approx(expected)
    assert overview.get_total() == pytest.approx(overview.get_subtotal() + overview.get_tax(), abs=0.01)
