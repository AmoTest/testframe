
from Public.Pages.BasePage import BasePage
"""
    结合Page Object模式，优化搜索基础场景
"""

class SearchPage(BasePage):

    SearchId = ("xpath", "//input[@name='q']")

    def Search_Value(self, searchValue):

        pass
