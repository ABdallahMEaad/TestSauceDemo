from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):
    path = "checkout-step-two.html"

    names = (By.CSS_SELECTOR, "[data-test='inventory-item-name']")
    subtotal = (By.XPATH, "//div[contains(@class,'summary_subtotal_label')]")
    tax = (By.XPATH, "//div[contains(@class,'summary_tax_label')]")
    total = (By.XPATH, "//div[contains(@class,'summary_total_label')]")
    finish_button = (By.ID, "finish")

    def is_loaded(self):
        return self.url_has(self.path) and self.get_title() == "Checkout: Overview"

    def get_names(self):
        return self.get_texts(self.names)

    def get_amount(self, locator):
        return float(self.get_text(locator).split("$")[1])

    def get_subtotal(self):
        return self.get_amount(self.subtotal)

    def get_tax(self):
        return self.get_amount(self.tax)

    def get_total(self):
        return self.get_amount(self.total)

    def finish(self):
        self.click(self.finish_button)
