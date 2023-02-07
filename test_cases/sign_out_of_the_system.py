import os
import unittest

# from selenium.webdriver.chrome.service import Service
# from webdriver.manager.chrome import ChromeDriverManager

from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestSignOut(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.login_form_title()
        user_login.remind_password()
        user_login.type_in_email('user02@getnada.com')
        user_login.fill_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        dashboard.click_sign_out_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()
