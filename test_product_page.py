from .pages.product_page import AddBasket
from selenium.webdriver.common.by import By

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = AddBasket(browser, link)
    page.open()
    page.add_book_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_message()
    page.should_be_same_price_basket()