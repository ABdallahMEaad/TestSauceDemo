from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    path = "inventory.html"

    product_list = (By.CLASS_NAME, "inventory_list")
    names = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    prices = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    buttons = (By.XPATH, "//div[@class='inventory_item']//button")
    sort_dropdown = (By.CSS_SELECTOR, "select[data-test='product-sort-container']")
    cart_badge = (By.CSS_SELECTOR, "span.shopping_cart_badge")
    cart_link = (By.CSS_SELECTOR, "a.shopping_cart_link")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def name_locator(self, product):
        return (By.XPATH, f"//div[@data-test='inventory-item-name' and normalize-space()='{product}']")

    def button_locator(self, product):
        return (
            By.XPATH,
            f"//div[@data-test='inventory-item-name' and normalize-space()='{product}']"
            "/ancestor::div[@class='inventory_item']//button",
        )

    def is_loaded(self):
        return self.is_visible(self.product_list) and self.get_title() == "Products"

    def get_names(self):
        return self.get_texts(self.names)

    def get_prices(self):
        return [float(p.replace("$", "")) for p in self.get_texts(self.prices)]

    def button_count(self):
        return len(self.find_all(self.buttons))

    def button_text(self, product):
        return self.get_text(self.button_locator(product))

    def cart_count(self):
        badge = self.driver.find_elements(*self.cart_badge)
        if badge:
            return int(badge[0].text)
        return 0

    def sort_by(self, value):
        Select(self.find(self.sort_dropdown)).select_by_value(value)

    def add_to_cart(self, product):
        self.click(self.button_locator(product))

    def remove_from_cart(self, product):
        self.click(self.button_locator(product))

    def add_first_items(self, number):
        products = self.get_names()[:number]
        for p in products:
            self.add_to_cart(p)
        return products

    def open_product(self, product):
        self.click(self.name_locator(product))

    def open_cart(self):
        self.click(self.cart_link)

    def logout(self):
        self.click(self.menu_button)
        self.click(self.logout_link)
