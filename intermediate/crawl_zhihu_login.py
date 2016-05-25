# -*- coding: utf-8 -*-
# 简单的网络爬虫: 模拟浏览器登陆知乎

import gzip
import re, time, os
import http.cookiejar
import urllib.request
import urllib.parse
from PIL import Image

# 构造请求头信息 header
URL = 'http://www.zhihu.com/'
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.8,zh;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Accept-Encoding': 'gzip,deflate,br',
    'Host': 'www.zhihu.com',
}


def getOpener(header):
    # 设置一个cookie处理器，它负责从服务器下载cookie到本地，并且在发送请求时带上本地的cookie
    cj = http.cookiejar.CookieJar()
    processor = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(processor)
    header_lst = []
    for key, value in header.items():
        elem = (key, value)
        header_lst.append(elem)
    opener.addheaders = header_lst
    return opener


def ungzip(data):
    try:
        data = gzip.decompress(data)
    except:
        print('未经压缩, 无需解压')
    return data


# 获取_xsrf
def getXSRF(data):
    pattern = re.compile(r'name="_xsrf" value="([\w\d]*)"/>', flags=0)
    strlist = pattern.findall(data)
    # print(strlist)
    return strlist[0]


# 获取验证码
def get_captcha(opener):
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r' + t + "&type=login"
    r = opener.open(captcha_url)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.read())
    # 用pillow 的 Image 显示验证码
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("Captcha: ")
    return captcha


def initPostDict(account, postDict):
    global URL
    if re.match(r'^1\d{10}$', account):
        postDict['phone_num'] = account
        url = URL + 'login/phone_num'
    else:
        postDict['email'] = account
        url = URL + 'login/email'
    return url, postDict


def login():
    global URL, header
    opener = getOpener(header)
    resp = opener.open(URL)
    data = ungzip(resp.read())

    _xsrf = getXSRF(data.decode())

    # 组装post数据
    account = input('Account: ')
    password = input('Password: ')
    captcha = get_captcha(opener)
    # 构造Post数据
    postDict = {
        '_xsrf': _xsrf,  # 网站特有数据
        'password': password,
        'remember_me': 'true',
        'captcha': captcha
    }
    url, postDict = initPostDict(account, postDict)

    # 需要给Post数据编码
    postData = urllib.parse.urlencode(postDict).encode()
    resp = opener.open(url, postData)
    data = ungzip(resp.read())

    print(data.decode())


if __name__ == '__main__':
    login()
