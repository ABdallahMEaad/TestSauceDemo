from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutInformationPage(BasePage):
    path = "checkout-step-one.html"

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.CSS_SELECTOR, "input#postal-code")
    continue_button = (By.ID, "continue")
    cancel_button = (By.ID, "cancel")
    error = (By.CSS_SELECTOR, "h3[data-test='error']")

    def is_loaded(self):
        return self.url_has(self.path) and self.get_title() == "Checkout: Your Information"

    def fill_form(self, first_name, last_name, postal_code):
        self.write(self.first_name, first_name)
        self.write(self.last_name, last_name)
        self.write(self.postal_code, postal_code)

    def continue_checkout(self):
        self.click(self.continue_button)

    def cancel(self):
        self.click(self.cancel_button)

    def get_error(self):
        return self.get_text(self.error)
