from pages.base_page import BasePage


class AddaPlayer(BasePage):
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    age_field_xpath = "//input[@name='age']"
    submit_button_xpath = "//*[text()='Submit']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    expected_title = "Add player"

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.surname_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.surname_field_xpath, main_position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title
    pass
