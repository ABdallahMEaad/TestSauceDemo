import pytest

from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from utils.test_data import PRODUCTS, PRODUCT_NAMES


@pytest.mark.smoke
def test_all_products_are_shown(inventory_page):
    assert sorted(inventory_page.get_names()) == sorted(PRODUCT_NAMES)


def test_every_product_has_a_button(inventory_page):
    assert inventory_page.button_count() == len(PRODUCT_NAMES)


def test_sort_by_name_a_to_z(inventory_page):
    inventory_page.sort_by("az")
    names = inventory_page.get_names()
    assert names == sorted(names)


def test_sort_by_name_z_to_a(inventory_page):
    inventory_page.sort_by("za")
    names = inventory_page.get_names()
    assert names == sorted(names, reverse=True)


def test_sort_by_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.get_prices()
    assert prices == sorted(prices)


def test_sort_by_price_high_to_low(inventory_page):
    inventory_page.sort_by("hilo")
    prices = inventory_page.get_prices()
    assert prices == sorted(prices, reverse=True)


def test_product_details(driver, inventory_page):
    product = PRODUCT_NAMES[0]
    inventory_page.open_product(product)

    details = ProductDetailsPage(driver)
    assert details.is_loaded()
    assert details.get_name() == product
    assert details.get_price() == PRODUCTS[product]


def test_back_from_product_details(driver, inventory_page):
    inventory_page.open_product(PRODUCT_NAMES[1])
    ProductDetailsPage(driver).go_back()
    assert inventory_page.is_loaded()


@pytest.mark.smoke
def test_add_one_item(inventory_page):
    product = PRODUCT_NAMES[0]
    inventory_page.add_to_cart(product)

    assert inventory_page.cart_count() == 1
    assert inventory_page.button_text(product) == "Remove"


def test_add_four_items(inventory_page):
    inventory_page.add_first_items(4)
    assert inventory_page.cart_count() == 4


def test_remove_item_on_inventory_page(inventory_page):
    product = PRODUCT_NAMES[0]
    inventory_page.add_to_cart(product)
    inventory_page.remove_from_cart(product)

    assert inventory_page.cart_count() == 0
    assert inventory_page.button_text(product) == "Add to cart"


def test_items_are_in_cart(driver, inventory_page):
    added = inventory_page.add_first_items(3)
    inventory_page.open_cart()

    cart = CartPage(driver)
    assert cart.is_loaded()
    assert cart.get_names() == added


def test_remove_item_in_cart(driver, inventory_page):
    first, second = inventory_page.add_first_items(2)
    inventory_page.open_cart()

    cart = CartPage(driver)
    cart.remove_item(first)
    assert cart.get_names() == [second]


def test_continue_shopping(driver, inventory_page):
    inventory_page.open_cart()
    CartPage(driver).continue_shopping()
    assert inventory_page.is_loaded()
