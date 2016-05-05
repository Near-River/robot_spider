from main.spider import url_manager, html_parser, html_outer, html_downloader


class SpiderMain(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.html_downloader = html_downloader.UrlDownloader()
        self.html_parser = html_parser.UrlParser()
        self.html_outer = html_outer.Outputer()

    def craw(self, root_url):
        count = 1
        self.url_manager.add_url(root_url)
        while self.url_manager.has_more_url():
            try:
                new_url = self.url_manager.get_url()
                print('craw %d：%s' % (count, new_url))
                html_doc = self.html_downloader.download(new_url)
                new_urls, content = self.html_parser.parse(new_url, html_doc)
                self.url_manager.add_urls(new_urls)
                self.html_outer.collect(content)

                if count == 1000:  # 抓取1000个百度百科页面
                    break
                count += 1
            except Exception as error:
                print(error)
                print('craw error...')
        self.html_outer.output()

if __name__ == '__main__':
    # python 百度百科词条网页url
    root_url = 'http://baike.baidu.com/link?url=mjTIpOyjMNQn1HSz7YG8AfeNlwP6ReAdONxmVOYzXKG1sjVoukGp-yJmSW2W-ACRzyebQXsaw7qeKH5uATIg2K'
    spider_obj = SpiderMain()
    spider_obj.craw(root_url)
