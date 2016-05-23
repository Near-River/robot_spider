# -*- coding: utf-8 -*-
# 简单的网络爬虫1: 抓取豆瓣网图片

import urllib.request
import re
import os


def makeFileName(targetDir, path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    filename = os.path.join(targetDir, path[pos + 1:])
    return filename


if __name__ == '__main__':
    url = 'http://www.douban.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'}
    req = urllib.request.Request(url=url, headers=headers)
    resp = urllib.request.urlopen(req)
    html = resp.read()
    print(html)

    targetDir = 'D:/demo/temp_imgs/'
    # pattern = re.compile(r'<img [\s\S]+?src="(http:[^\s]+?(jpg|png|gif))"')
    pattern = re.compile(r'(https:[^\s]*?(jpg|png|gif))')
    url_lst = re.findall(pattern, str(html))
    print('Total count: %s' % len(url_lst))
    failed_count = 0
    for inx, url in enumerate(url_lst):
        print('Count: %s    Url: %s' % (inx + 1, url))
        try:
            img_path = makeFileName(targetDir, url[0])
            urllib.request.urlretrieve(url[0], img_path)  # 远程下载
        except urllib.request.URLError as e:
            print('Crawl failed at: %s' % url[0])
            failed_count += 1
    print('Failed crawl count: %s' % failed_count)
