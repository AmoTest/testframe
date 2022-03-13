
from selenium import webdriver


class BasePage:

    """
        BasePage封装所有页面的公共方法
    """
    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception:
            raise NameError("Not Firefox")

    def open(self, url):
        pass

    def findElement(self, element):
        pass

    def findElements(self, elements):
        pass

    def click(self, element):
        pass

    def enter(self, element):
        pass

    def getAttribute(self, element, attribute):
        pass

    def display(self, element):
        pass