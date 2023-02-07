from pages.base_page import BasePage


class AddMatch(BasePage):
    add_match_url = "https://scouts-test.futbolkolektyw.pl/en/players/62f2bce6159aa3d4fa18f4b2/matches/add"
    expected_title = "Adding match player Tester Snizhana"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]"
    match_date_xpath = "//input[@type='date']"
    my_team_name_field_xpath = "//*[@name='myTeam']"
    enemy_team_name_field_xpath = "//*[@name='enemyTeam']"
    enemy_team_score_field_xpath = "//*[@name='enemyTeamScore']"
    reports_button_xpath = "//*[text() = 'Reports']"
    general_field_xpath = "//*[@name='general']"
    web_match_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/label"
    button_matches_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    time_played_field_xpath = "//*[@name='timePlayed']"
    my_team_score_field_xpath = "//*[@name='myTeamScore']"

    def type_in_my_team_name(self, name):
        self.field_send_keys(self.my_team_name_field_xpath, name)

    def type_in_my_team_score(self, score):
        self.field_send_keys(self.my_team_score_field_xpath, score)

    def type_in_enemy_team_name(self, name):
        self.field_send_keys(self.enemy_team_name_field_xpath, name)

    def type_in_enemy_team_score(self, score):
        self.field_send_keys(self.enemy_team_score_field_xpath, score)

    def type_in_match_date(self, date):
        self.field_send_keys(self.match_date_xpath, date)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.add_match_url) == self.expected_title

    pass
