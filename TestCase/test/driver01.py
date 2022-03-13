from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import unittest
import time
import requests

s = Service('/Users/zhouwenxun/Downloads/chromedriver')
driver = webdriver.Chrome(service=s)
class TestCase(unittest.TestCase):

    def testcase_01_login(self):

        driver.get('http://www.baidu.com')

        #id定位
        driver.find_element(By.ID, "kw").send_keys("python")
        time.sleep(10)
        driver.find_element(By.ID, "su").click()

#    def testcase_02_query(self):
#        driver.find_element(By.ID, "su").click()


if __name__ == "__main__":
    unittest.main()
    requests.request()