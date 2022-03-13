
from urllib.request import ProxyHandler
from urllib.request import build_opener
from urllib.request import Request

url = 'http://www.baidu.com'

proxy = ProxyHandler({"http": "59.58.43.154:8888"})
"""
ProxyHandler({"http": "ip:port"})
ProxyHandler({"http": "username:password@ip:port"})
"""

opener = build_opener(proxy)
resp = opener.open(Request(url))

print(resp.read().decode('utf-8'))