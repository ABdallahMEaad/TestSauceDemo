from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestSauceDemo:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        print("Chrome opened")
        time.sleep(1)

    def open_site(self):
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(1)

    def login_test(self):
        driver = self.driver

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        time.sleep(1)

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)

        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        assert "inventory" in driver.current_url
        print("Login Success")
        time.sleep(1)

    def shopping_items_test(self):
        driver = self.driver

        buttons = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//button[contains(@id,'add-to-cart')]")
            )
        )

        for i in range(min(4, len(buttons))):
            time.sleep(1)
            buttons[i].click()
            print(f"Item {i + 1} added to cart")

        time.sleep(1)



    def chech_out(self):
        driver = self.driver

        time.sleep(1)

        driver.find_element(By.ID, "shopping_cart_container").click()
        print("Open cart")
        time.sleep(1)

        print("Checkout page opened")

        driver.find_element(By.ID, "checkout").click()
        print("Checkout clicked")
        time.sleep(1)

        driver.find_element(By.ID, "first-name").send_keys("Abdallah")
        time.sleep(1)

        driver.find_element(By.ID, "last-name").send_keys("Meaad")
        time.sleep(1)

        driver.find_element(By.ID, "postal-code").send_keys("0554")
        time.sleep(1)

        driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        driver.find_element(By.ID, "finish").click()
        time.sleep(1)

        print('Checkout Done ^_^')

        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(1)


    def teardown(self):
        time.sleep(3)
        self.driver.quit()


test = TestSauceDemo()
test.setup()
test.open_site()
test.login_test()
test.shopping_items_test()
test.chech_out()
test.teardown()