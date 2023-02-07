import os
import unittest

# from selenium.webdriver.chrome.service import Service
# from webdriver.manager.chrome import ChromeDriverManager

from selenium import webdriver
from pages.login_page import LoginPage
from pages.addPlayer import AddaPlayer
from pages.dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddaPlayer(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user02@getnada.com')
        user_login.fill_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard = Dashboard(self.driver)
        dashboard.click_add_player_button()
        add_player = AddaPlayer(self.driver)
        add_player.type_in_name('John')
        add_player.type_in_surname('Doe')
        add_player.type_in_age('01-02-2012')
        add_player.type_in_main_position('Goalkeeper')
        add_player.click_submit_button()

    @classmethod
    def tearDown(self):
        self.driver.quit()