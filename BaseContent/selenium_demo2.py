import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestForm(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def test_web_form(self) -> None:
        # 打开表单页面
        self.driver.get('https://www.selenium.dev/selenium/web/web-form.html')
        self.assertEqual(self.driver.title, 'Web form')
        time.sleep(2)

        # Text 输入
        text_input_elem = self.driver.find_element(By.ID, 'my-text-id')
        text_input_elem.send_keys('Selenium')
        time.sleep(1)

        # Password 输入
        password_elem = self.driver.find_element(By.NAME, 'my-password')
        password_elem.send_keys('Selenium')
        time.sleep(1)

        # Dropdown 选择
        dropdown_elem = Select(self.driver.find_element(By.NAME, 'my-select'))
        dropdown_elem.select_by_value('2')
        time.sleep(1)

        # 日期输入
        date_input_elem = self.driver.find_element(By.XPATH, '//input[@name="my-date"]')
        date_input_elem.send_keys('05/10/2023')

        # 点击 Submit 按钮
        submit_button_elem = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button_elem.click()
        time.sleep(1)

        # 等待进入已提交页面
        WebDriverWait(self.driver, 10).until(EC.title_is('Web form - target page'))

        # 断言
        message = self.driver.find_element(By.ID, 'message').text
        self.assertEqual(message, 'Received!')