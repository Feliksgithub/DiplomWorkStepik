from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM =(By.CSS_SELECTOR, "#register_form") 

class BasketPageLocators(object):
    ADD_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    ADD_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRICE_BASKET = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE_BOOK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")