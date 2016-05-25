# -*- coding: utf-8 -*-
# 简单的网络爬虫: 抓取糗事百科段子

import re
import time
import urllib.request
from threading import Thread


class Spider_Model:
    def __init__(self, pages):
        self.pages = pages
        self.content = []

    def loadpage(self, page):
        url = 'http://www.qiushibaike.com/textnew/page/' + str(page) + '/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'}
        try:
            req = urllib.request.Request(url=url, headers=headers)
            resp = urllib.request.urlopen(req)
            html = resp.read()
            pattern = re.compile(r'<div.*?class="content">(.*?)</div>', flags=re.DOTALL)
            tex_lst = re.findall(pattern, html.decode('utf-8'))
            self.content.append('Page: %s\r\n' % page)
            for item in tex_lst:
                # print(item.strip())
                self.content.append(item.strip().replace('<br/>', '\n') + '\r\n')
        except urllib.request.URLError:
            print('Unable to connect %s' % url)

    def savepages(self):
        with open('qiushi.txt', 'w', encoding='utf-8') as f:
            f.writelines(self.content)

    def run(self):
        if self.pages <= 0:
            print('Invalid total number of pages')
            return
        print(u'Loading......')

        # t1 = time.time()
        # for page in range(1, self.pages + 1):
        #     self.loadpage(page)
        # t2 = time.time()
        # print('Cost Time: %s' % (t2 - t1))

        def loadpages(startpage, endpage):
            for page in range(startpage, endpage + 1):
                self.loadpage(page)

        t1 = time.time()
        half = self.pages // 2
        thread1 = Thread(loadpages(1, half))
        thread2 = Thread(loadpages(half + 1, self.pages))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        t2 = time.time()
        print('Cost Time: %s' % (t2 - t1))
        """
        spider 35 pages(cost time):
            Multiply Thread: 14.529830932617188(s)
            Single Thread: 7.45742654800415(s)
        """
        print('Save the data......')
        self.savepages()
        print('End.')


if __name__ == '__main__':
    pages = input('Total pages: ')
    spider = Spider_Model(int(pages))
    spider.run()
