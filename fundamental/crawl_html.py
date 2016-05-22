# coding:utf-8
import urllib.request
import urllib.parse

if __name__ == '__main__':
    user = dict(id='001', name='Jack', age=21)
    print(urllib.parse.urlencode(user).encode())
    # >> b'age=21&name=Jack&id=001'
