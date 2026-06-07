# 🛒 SauceDemo Automation Testing Project

## 📌 Project Overview

This project is an automated end-to-end testing framework built using **Python** and **Selenium WebDriver** to test the main user journey on the SauceDemo e-commerce website.

The automation script covers:

* User Login
* Add Products to Cart
* Shopping Cart Validation
* Checkout Process
* Order Completion

Website Tested:

**SauceDemo** → https://www.saucedemo.com/

---

## 🛠️ Technologies Used

* Python
* Selenium WebDriver
* ChromeDriver
* Explicit Waits (WebDriverWait)
* PyTest Structure Concepts

---

## 📂 Test Scenarios Covered

### ✅ Login Test

* Open SauceDemo website
* Enter valid username
* Enter valid password
* Click Login button
* Verify successful login

### ✅ Add Products to Cart

* Add first 4 products to cart
* Validate items are added successfully

### ✅ Checkout Process

* Open shopping cart
* Proceed to checkout
* Fill customer information:

  * First Name
  * Last Name
  * Postal Code
* Continue checkout
* Finish order
* Return to products page

---

## 🚀 How to Run

### Clone Repository

```bash
git clone https://github.com/ABdallahMEaad/SauceDemo-Automation-Testing.git
```

### Install Dependencies

```bash
pip install selenium
```

### Run Script

```bash
python main.py
```

---

## 📋 Test Credentials

```text
Username: standard_user
Password: secret_sauce
```

---

## 📸 Test Flow

1. Launch Chrome Browser
2. Navigate to SauceDemo
3. Login Successfully
4. Add 4 Products to Cart
5. Open Shopping Cart
6. Checkout Order
7. Complete Purchase
8. Return to Products Page
9. Close Browser

---

## 🎯 Learning Objectives

This project demonstrates practical experience with:

* Selenium WebDriver
* Element Locators (ID, XPath, Class Name)
* Explicit Waits
* Browser Automation
* Functional Testing
* End-to-End Testing
* UI Test Automation

---

## 🔮 Future Improvements

* Implement PyTest Framework
* Generate HTML Reports
* Add Screenshot Capture on Failure
* Implement Page Object Model (POM)
* Data-Driven Testing
* Cross-Browser Testing
* CI/CD Integration using GitHub Actions

---

## 👨‍💻 Author

**Abdallah Ahmed Meaad**

QA Engineer | Manual Testing | API Testing | Selenium Automation | JMeter

GitHub:
https://github.com/ABdallahMEaad

LinkedIn:
Add your LinkedIn profile here
