# coding=gbk
from bs4 import BeautifulSoup as sp
from urllib import request
from random import choice
from urllib.parse import quote
import re

class WikiSpiderUtils(object):
    def __init__(self, search_key):
        super(WikiSpiderUtils, self).__init__()
        self.search_key = search_key


    def get_search_key(self):
        return self.search_key


    '''
    方法说明：维基百科爬虫工具类
    '''
    def wikiSpiderUtil(self):
        last_list = list()
        # 一、请求准备阶段
        # 1、准备url
        url = "http://zh.wikipedia.org/wiki/%s" % quote(self.search_key)
        # 2、准备请求头信息
        headers = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
        ]
        # 3、设置代理请求方式
        req = request.Request(url=url, headers={'User-Agent': choice(headers)})
        # 4、获取请求返回的Html文本内容
        html = request.urlopen(req).read()

        # 二、解析返回回来的html文本，获取自己需要的内容
        # 1、使用bs4解析html
        soup = sp(html, 'html.parser')
        # 2、获取指定节点内的文本
        # 只需要直接的子节点即可
        # ①、(获取所有的子节点内容)
        # results = soup.select(".mw-parser-output > p")
        # ②、(只获取第一个子节点内容)【获取class=mw-parser-output节点下; 第一个有class属性的div标签后; 第一个p标签的文本内容】
        results = soup.select(".mw-parser-output div[class] + p")
        for item in results:
            last_list.append(item.get_text())

        # 3、清洗获取到的数据列表
        # 清洗掉\xa0
        filter_result = [item.replace(u'\xa0', u'') for item in last_list]
        # 清除掉所有的[XXX]数据
        pat = re.compile(r'\[.*?\]')
        filter_result = [re.sub(pat, '', item) for item in filter_result]

        # 4、拼接并返回list列表中值
        last_val = "".join([item for item in filter_result])
        return last_val

