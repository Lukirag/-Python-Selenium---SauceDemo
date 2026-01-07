import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pip install -r requirements.txt

class SauceDemoLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def test_valid_login(self):
        """Тест: успешный вход с валидными данными"""
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.ID, "login-button")


        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        wait = WebDriverWait(self.driver, 10)
        inventory_title = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "title"))
        )

        self.assertEqual(inventory_title.text, "PRODUCTS")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

python test_login.py