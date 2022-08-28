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
    ����˵����ά���ٿ����湤����
    '''
    def wikiSpiderUtil(self):
        last_list = list()
        # һ������׼���׶�
        # 1��׼��url
        url = "http://zh.wikipedia.org/wiki/%s" % quote(self.search_key)
        # 2��׼������ͷ��Ϣ
        headers = [
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
        ]
        # 3�����ô�������ʽ
        req = request.Request(url=url, headers={'User-Agent': choice(headers)})
        # 4����ȡ���󷵻ص�Html�ı�����
        html = request.urlopen(req).read()

        # �����������ػ�����html�ı�����ȡ�Լ���Ҫ������
        # 1��ʹ��bs4����html
        soup = sp(html, 'html.parser')
        # 2����ȡָ���ڵ��ڵ��ı�
        # ֻ��Ҫֱ�ӵ��ӽڵ㼴��
        # �١�(��ȡ���е��ӽڵ�����)
        # results = soup.select(".mw-parser-output > p")
        # �ڡ�(ֻ��ȡ��һ���ӽڵ�����)����ȡclass=mw-parser-output�ڵ���; ��һ����class���Ե�div��ǩ��; ��һ��p��ǩ���ı����ݡ�
        results = soup.select(".mw-parser-output div[class] + p")
        for item in results:
            last_list.append(item.get_text())

        # 3����ϴ��ȡ���������б�
        # ��ϴ��\xa0
        filter_result = [item.replace(u'\xa0', u'') for item in last_list]
        # ��������е�[XXX]����
        pat = re.compile(r'\[.*?\]')
        filter_result = [re.sub(pat, '', item) for item in filter_result]

        # 4��ƴ�Ӳ�����list�б���ֵ
        last_val = "".join([item for item in filter_result])
        return last_val

