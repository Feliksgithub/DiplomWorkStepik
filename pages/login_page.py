from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверяем на корректный url адрес
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        # проверяем наличие формы логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # проверяем наличие формы регистрации
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        
    def register_new_user(self, email, password):
        # регистрация нового пользователя
    	email_reg = self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)        
    	pass_reg = self.browser.find_element(*LoginPageLocators.REG_PASSWORD).send_keys(password)      
    	pass_reg2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD2).send_keys(password)    
    	button_reg = self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()              