from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    base_url = "https://www.saucedemo.com/"
    path = ""
    title = (By.CSS_SELECTOR, "[data-test='title']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.base_url + self.path)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def write(self, locator, text):
        box = self.find(locator)
        box.clear()
        box.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text.strip()

    def get_texts(self, locator):
        return [e.text.strip() for e in self.find_all(locator)]

    def is_visible(self, locator, seconds=10):
        try:
            WebDriverWait(self.driver, seconds).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_gone(self, locator, seconds=10):
        try:
            WebDriverWait(self.driver, seconds).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def url_has(self, text):
        try:
            self.wait.until(EC.url_contains(text))
            return True
        except TimeoutException:
            return False

    def get_title(self):
        return self.get_text(self.title)
