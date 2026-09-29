from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    username = (By.ID, "user-name")
    password = (By.CSS_SELECTOR, "input#password")
    login_button = (By.XPATH, "//input[@id='login-button']")
    error = (By.CSS_SELECTOR, "h3[data-test='error']")
    error_close = (By.CSS_SELECTOR, "button.error-button")

    def load(self):
        self.open()
        return self

    def is_loaded(self):
        return self.is_visible(self.login_button)

    def login(self, user, password):
        self.write(self.username, user)
        self.write(self.password, password)
        self.click(self.login_button)

    def get_error(self):
        return self.get_text(self.error)

    def error_shown(self):
        return self.is_visible(self.error, 3)

    def error_hidden(self):
        return self.is_gone(self.error, 3)

    def close_error(self):
        self.click(self.error_close)
