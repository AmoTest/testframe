
import sys
from urllib import request
import urllib3
import requests

print("hello world")

print(sys.platform)

r = requests.get("http://www.baidu.com")
# print(r.content)
# # r.encoding = 'utf-8'
# print(r.text）
print(r.raw.read())

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("Hello World你好")

with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())