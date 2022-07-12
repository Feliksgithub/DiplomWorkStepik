from .base_page import BasePage
from .locators import BasketPageLocators

class AddBasket(BasePage):
     def add_book_in_basket(self):
         add_basket = self.browser.find_element(*BasketPageLocators.ADD_BASKET)
         add_basket.click()        
     def should_be_add_message(self):    
         add_message = self.browser.find_element(*BasketPageLocators.ADD_MESSAGE).text
         book_name = self.browser.find_element(*BasketPageLocators.BOOK_NAME).text        
         assert add_message in book_name, "No book name in the message"
     def should_be_same_price_basket(self):
         price_basket = self.browser.find_element(*BasketPageLocators.PRICE_BASKET).text
         price_book = self.browser.find_element(*BasketPageLocators.PRICE_BOOK).text
         assert price_basket in price_book, "Product price is not correct"