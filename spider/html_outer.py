# 收集抓取的数据
import codecs


class Outputer(object):
    def __init__(self):
        self.contents = []

    def collect(self, content):
        if content is None:
            return
        self.contents.append(content)

    def output(self):
        try:
            fout = codecs.open('D:/demo/baike.html', 'w', 'utf-8')

            fout.write('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"></head><body>')
            fout.write("<table border=1>")
            fout.write("<tr>")
            fout.write("<td>URL</td>")
            fout.write("<td>标题</td>")
            fout.write("<td>简介</td>")
            fout.write("</tr>")

            for content in self.contents:
                fout.write("<tr>")
                fout.write('<td>%s</td>' % content['page_url'])
                fout.write('<td>%s</td>' % (content['title']))
                fout.write('<td>%s</td>' % (content['summary']))
                fout.write("</tr>")

            fout.write('</table></body></html>')
            fout.close()
        except IOError as error:
            print(error)
            if fout is not None:
                fout.close()
