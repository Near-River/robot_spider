# coding:utf-8
import urllib.request
from html.parser import HTMLParser


class CategoryName(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_category = ""
        self.name = []

    def handle_starttag(self, tag, attrs):
        print(attrs)
        # < a class ="category-name category-name-level1 J_category_hash" ...  > 女装男装 < / a >
        if tag == 'a' and attrs[0][1] == 'category-name category-name-level1 J_category_hash':
            self.is_category = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.is_category = False

    def handle_data(self, text):
        if self.is_category:
            self.name.append(text)


if __name__ == '__main__':
    content = urllib.request.urlopen('https://www.taobao.com/markets/tbhome/market-list').read()
    name_lst = CategoryName()
    name_lst.feed(content.decode('utf-8'))
    for item in name_lst.name:
        print(item)
