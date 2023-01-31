import time

from pages.base_page import BasePage



class Dashboard(BasePage):
    main_page_xpath = "//*[text() = 'Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    players_count_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div/div[1]"
    matches_count_xpath = "//*[text() = 'Main page']"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    last_created_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/h6[1]"
    match_created_xpath = "//*[text() = 'Last created match']"
    dev_team_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    expected_title = 'Scouts panel'

    def click_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
