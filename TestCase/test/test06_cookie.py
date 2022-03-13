from urllib.request import urlopen
from urllib.request import build_opener
from urllib.request import Request
from urllib.parse import urlencode
from http.cookiejar import MozillaCookieJar
from urllib.request import HTTPCookieProcessor
from lxml import etree


def getCookie():
    loginUrl = 'https://udblgn.huya.com/web/v2/passwordLogin'

    formData = {
        "username": "2715756433",
        "password": "xun08020906qing"
    }

    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }

    req = Request(loginUrl, data=urlencode(formData).encode(), headers=header)
    cookieJar = MozillaCookieJar()
    handle = HTTPCookieProcessor(cookieJar)

    resp = build_opener(handle).open(req)

    cookieJar.save('cookie.txt', ignore_discard=True, ignore_expires=True)

def useCookie():
    infoUrl = "https://i.huya.com/"
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }

    req = Request(infoUrl, headers=header)
    cookieJar = MozillaCookieJar()
    cookieJar.load('cookie.txt', ignore_expires=True, ignore_discard=True)
    handler = HTTPCookieProcessor(cookieJar)

    resp = build_opener(handler).open(req)
    print(resp.read().decode())


if __name__ == '__main__':

    getCookie()
    useCookie()