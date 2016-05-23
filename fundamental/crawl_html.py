# coding:utf-8

import urllib.parse
import urllib.request

# 网络爬虫
# =========================================================================
# 添加特殊情景的处理器：
#   1.需要用户登录：HTTPCookieProcessor
#   2.需要代理服务器：ProxyHandler
#   3.使用https加密访问的：HTTPSHandler
#   4.url之间自动的跳转关系：HTTPRedirectHandler

if __name__ == '__main__':
    user = dict(id='001', name='Jack', age=21)
    print(urllib.parse.urlencode(user).encode())
    # >> b'age=21&name=Jack&id=001'
    try:
        req = urllib.request.urlopen(url='http://www.google.com', timeout=10)
        print(req.read())
        print(req.geturl())
        print(req.info())
    except urllib.request.URLError as e:
        if hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        elif hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
