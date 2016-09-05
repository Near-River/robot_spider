# -*- coding: utf-8 -*-

import re
import gzip
import http.cookiejar
import urllib.request
import numpy as np
from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
URL = 'https://movie.douban.com/top250'
# 构造请求头信息 header
header = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.8,zh;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip,deflate,br',
    'Connection': 'Keep-Alive'
}


class Movie(object):
    def __init__(self, name, kinds, rating, quote):
        self.name = name
        self.kinds = kinds
        self.rating = float(rating)
        self.quote = quote

    def __str__(self):
        return '%s, %s, %s, %s' % (self.name, str(self.kinds), str(self.rating), self.quote)


class Fetcher(object):
    global header, URL

    def __init__(self):
        self.totalPages = 10
        self.movies = []
        self.opener = self.get_opener(header)
        self.fetcher_data()

    def get_opener(self, header):
        cj = http.cookiejar.CookieJar()
        processor = urllib.request.HTTPCookieProcessor(cj)
        opener = urllib.request.build_opener(processor)
        header_lst = []
        for key, value in header.items():
            elem = (key, value)
            header_lst.append(elem)
        opener.addheaders = header_lst
        return opener

    def ungzip(self, data):
        try:
            data = gzip.decompress(data)
        except:
            print('Uncompressed, no decompression.')
        return data

    def get_html(self, url, retries=3):  # 失败后的重连机制
        try:
            data = self.opener.open(fullurl=url, timeout=10).read()  # 设置超时时间为10秒
            return self.ungzip(data)
        except urllib.request.URLError as e:
            if retries > 0: return self.get_html(retries - 1)
            print(e.reason)

    def fetcher_data(self):
        for i in range(self.totalPages):
            url = URL + '?start=' + str(i * 25) + '&filter='
            html = self.get_html(url).decode()
            self.parse_html(html)

    def parse_html(self, html):
        movie_pattern = re.compile(
            r'<div class="info">.*?<div class="hd">.*?<span class="title">(.*?)</span>.*?</div>.*?<div class="bd">.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span class="inq">(.*?)</span>.*?</div>.*?</div>',
            flags=re.DOTALL)
        movies = list(map(list, movie_pattern.findall(html)))
        for movie in movies:
            s = movie[1].replace('\n', '').replace('&nbsp;', '')
            s = s.strip()
            movie[1] = s[s.rfind('/') + 1:].split(' ')
            self.movies.append(Movie(*movie))

    def get_data(self):
        return self.movies


def analysis_data(movies):
    hash = {}
    for movie in movies:
        for kind in movie.kinds:
            hash[kind] = hash.get(kind, 0) + 1
    kinds = list(hash.keys())
    nums = list(hash.values())
    plt.figure(figsize=(18, 15))
    plt.title('豆瓣top250电影')
    plt.xlabel('种类：')
    plt.ylabel('数量：')
    bar_width = 1.0
    index = np.arange(len(kinds))
    plt.xticks(index + bar_width / 2, kinds)
    plt.bar(index, nums, bar_width, color="green")
    plt.grid(True)
    # plt.show()
    plt.savefig('douban_movie.jpg')


if __name__ == '__main__':
    fetcher = Fetcher()
    movies = fetcher.get_data()
    analysis_data(movies)
