from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    path = "checkout-complete.html"

    header = (By.CSS_SELECTOR, ".complete-header")
    back_button = (By.ID, "back-to-products")

    def is_loaded(self):
        return self.url_has(self.path) and self.is_visible(self.header)

    def get_header(self):
        return self.get_text(self.header)

    def back_home(self):
        self.click(self.back_button)
