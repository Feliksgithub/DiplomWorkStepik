from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.QUANTITY_LOCATOR), \
        "The book was added in the basket, but should not to be"       
    def should_be_empty_basket_message(self):      
        assert self.is_element_present(By.XPATH, "//*[@id='content_inner']/p"), "Basket IS NOT Empty"