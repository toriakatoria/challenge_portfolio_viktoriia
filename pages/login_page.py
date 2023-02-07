from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@type='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/login'
    expected_title = 'Scouts panel - sign in'
    login_form_title_xpath = "// h5"
    login_form_title_expected = "Scouts Panel"
    remind_password_xpath= "//a"
    remind_password_title_expected = 'Remind password'
    login_error_expected = "Identifier or password invalid."
    login_error_xpath = "//*/form/div/div[1]/div[3]/span"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def fill_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

    def login_form_title(self):
        element = self.driver.find_element(by=By.XPATH, value=self.login_form_title_xpath)
        element_text = element.text
        assert self.login_form_title_expected == element_text

    def remind_password(self):
        element = self.driver.find_element(by=By.XPATH, value=self.remind_password_xpath)
        element_text = element.text
        assert self.remind_password_title_expected == element_text

    def log_in_error(self):
        element = self.driver.find_element(by=By.XPATH, value=self.login_error_xpath)
        element_text = element.text
        assert self.login_error_expected == element_text




