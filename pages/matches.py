from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Matches(BasePage):
    matches_url = "https://scouts-test.futbolkolektyw.pl/en/players/62f2bce6159aa3d4fa18f4b2/matches"
    expected_title = "Matches player Tester Snizhana"
    match_name_xpath = "//*/tbody/tr[3]/td[1]"
    match_name_expected = "First"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.match_name_xpath)
        assert self.get_page_title(self.matches_url) == self.expected_title

    def assert_match_added(self):
        element = self.driver.find_element(by=By.XPATH, value=self.match_name_xpath)
        element_text = element.text
        assert self.match_name_expected == element_text
