from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 
    REG_EMAIL = (By.XPATH, "//*[@id='id_registration-email']")
    REG_PASSWORD = (By.XPATH, "//*[@id='id_registration-password1']")
    REG_PASSWORD2 = (By.XPATH, "//*[@id='id_registration-password2']")
    REG_BUTTON = (By.XPATH, "//*[@id='register_form']/button")

class BasketPageLocators(object):
    ADD_BASKET = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    ADD_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRICE_BASKET = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    PRICE_BOOK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div")
    BASKET_BUTTON = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")
    QUANTITY_LOCATOR = (By.XPATH, "//*[@id='id_form-1-quantity']")
    
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")