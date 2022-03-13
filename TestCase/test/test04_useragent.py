
from urllib.request import Request
from urllib.request import urlopen
from urllib.request import build_opener, HTTPHandler


url = 'http://www.baidu.com'

req = Request(url)

# print(urlopen(req).read().decode())
resp = build_opener(HTTPHandler(debuglevel=1)).open(req)
# print(resp.read().decode())