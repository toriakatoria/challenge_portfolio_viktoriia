from pages.base_page import BasePage


class Dashboard(BasePage):
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]"
    date_field_xpath = "//input[@type='date']"
    my_team_field_xpath = "//*[@name='myTeam']"
    enemy_team_score_field_xpath = "//*[@name='enemyTeamScore']"
    reports_button_xpath = "//*[text() = 'Reports']"
    general_field_xpath = "//*[@name='general']"
    web_match_label_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/label"
    button_matches_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    time_played_field_xpath = "//*[@name='timePlayed']"

    pass
