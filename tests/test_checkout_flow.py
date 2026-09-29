import pytest

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from utils import test_data as data


@pytest.mark.smoke
def test_full_purchase(driver, inventory_page):
    added = inventory_page.add_first_items(4)
    assert inventory_page.cart_count() == 4
    inventory_page.open_cart()

    cart = CartPage(driver)
    assert cart.is_loaded()
    assert cart.get_names() == added
    cart.checkout()

    info = CheckoutInformationPage(driver)
    assert info.is_loaded()
    info.fill_form(**data.CHECKOUT_INFO)
    info.continue_checkout()

    overview = CheckoutOverviewPage(driver)
    assert overview.is_loaded()
    assert overview.get_names() == added
    overview.finish()

    complete = CheckoutCompletePage(driver)
    assert complete.is_loaded()
    assert complete.get_header() == data.ORDER_DONE
    complete.back_home()

    assert inventory_page.is_loaded()
    assert inventory_page.cart_count() == 0
