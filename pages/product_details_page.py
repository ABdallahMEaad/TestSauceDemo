from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    path = "inventory-item.html"

    name = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    price = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")
    back_button = (By.ID, "back-to-products")

    def is_loaded(self):
        return self.url_has(self.path) and self.is_visible(self.name)

    def get_name(self):
        return self.get_text(self.name)

    def get_price(self):
        return float(self.get_text(self.price).replace("$", ""))

    def go_back(self):
        self.click(self.back_button)
