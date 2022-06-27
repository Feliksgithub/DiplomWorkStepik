class BasePage():
def __inint__(self, browser, url):
    self.browseer = browser
    self.url = url
    
    
def open(self):
    self.browser.get(self.url)