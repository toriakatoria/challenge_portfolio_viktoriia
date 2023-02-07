import os
import unittest

from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.addaMatch import AddMatch
from pages.matches import Matches
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from PIL import Image


class TestAddMatch(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_match(self):
        user_login = LoginPage(self.driver)
        user_login.login_form_title()
        user_login.type_in_email('user02@getnada.com')
        user_login.fill_in_password('Test-1234')
        self.driver.save_screenshot(
            '/home/yevgrafova/Documents/GitHub/challenge_portfolio_viktoriia/screenshots/login-filled-in.png')
        Image.open(
            '/home/yevgrafova/Documents/GitHub/challenge_portfolio_viktoriia/screenshots/login-filled-in.png').show()
        user_login.click_sign_in_button()
        dashboard = Dashboard(self.driver)
        dashboard.title_of_page()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/62f2bce6159aa3d4fa18f4b2/matches/add')
        add_match = AddMatch(self.driver)
        add_match.title_of_page()
        add_match.type_in_my_team_name('First')
        add_match.type_in_my_team_score('5')
        add_match.type_in_enemy_team_name('Second')
        add_match.type_in_enemy_team_score('3')
        add_match.type_in_match_date('02-02-2023')
        add_match.click_submit_button()
        matches = Matches(self.driver)
        self.driver.save_screenshot(
            '/home/yevgrafova/Documents/GitHub/challenge_portfolio_viktoriia/screenshots/match-added.png')
        matches.assert_match_added()

    @classmethod
    def tearDown(self):
        self.driver.quit()
