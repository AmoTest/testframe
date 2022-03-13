# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.find_element_by_link_text(u"京东服饰").click()
        driver.get("https://channel.jd.com/fashion.html")
        driver.get("https://channel.jd.com/fashion.html")
        driver.find_element_by_link_text(u"原创设计").click()
        driver.get(
            "https://wqs11.jd.com/data/coss/recoverydata/45/fe2c4ab59833605dc85b41b408b70e3d.shtml?tpl=index?err=52")
        # ERROR: Caught exception [unknown command []]
        # ERROR: Caught exception [unknown command []]
        # ERROR: Caught exception [unknown command []]
        # ERROR: Caught exception [unknown command []]
        # ERROR: Caught exception [unknown command []]

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
