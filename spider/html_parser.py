# 一方面解析出有价值的数据，一方面解析出其他关联URL，传回至URL管理器进行循环处理
import re
from bs4 import BeautifulSoup


class UrlParser(object):
    def parse(self, page_url, html_doc):
        if page_url is None or html_doc is None:
            return
        soup = BeautifulSoup(
            html_doc,
            'html.parser',
            from_encoding='utf-8'
        )
        new_urls = self.get_new_urls(page_url, soup)
        content = self.get_content(page_url, soup)

        return new_urls, content

    # 获取页面的所有链接
    def get_new_urls(self, page_url, soup):
        # <a target="_blank" href="/view/125370.htm">面向对象</a>
        links = soup.find_all('a', href=re.compile(r'/view/\d+?.htm'))
        urls = []
        for link in links:
            url = link['href']
            # print(url)
            new_url = 'http://baike.baidu.com' + url
            # print(new_url)
            urls.append(new_url)
        if page_url in urls:
            urls.remove(page_url)
        return urls

    # 获取价值信息
    def get_content(self, page_url, soup):
        res_data = {}
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1> ... </dd>
        res_data['title'] = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        # print(res_data['title'])

        # <div class="lemma-summary" label-module="lemmaSummary"> <div class="para" label-module="para">Python ...
        res_data['summary'] = soup.find('div', class_='lemma-summary').find('div', class_='para').get_text()
        # print(res_data['summary'])

        res_data['page_url'] = page_url
        return res_data
