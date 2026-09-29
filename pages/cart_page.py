from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    path = "cart.html"

    items = (By.CSS_SELECTOR, ".cart_item")
    names = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    checkout_button = (By.ID, "checkout")
    continue_button = (By.ID, "continue-shopping")

    def remove_locator(self, product):
        return (
            By.XPATH,
            f"//div[@data-test='inventory-item-name' and normalize-space()='{product}']"
            "/ancestor::div[@class='cart_item']//button",
        )

    def is_loaded(self):
        return self.url_has(self.path) and self.get_title() == "Your Cart"

    def get_names(self):
        if len(self.driver.find_elements(*self.items)) == 0:
            return []
        return self.get_texts(self.names)

    def remove_item(self, product):
        self.click(self.remove_locator(product))

    def continue_shopping(self):
        self.click(self.continue_button)

    def checkout(self):
        self.click(self.checkout_button)
