# coding=gbk
import requests
from lxml import etree
from bs4 import BeautifulSoup as sp
import re
from WordCloudUtils import WordCloudUtils


class BaiduBaikeSpiderUtils(object):

    def __init__(self, proxies, search_key):
        super(BaiduBaikeSpiderUtils, self).__init__()
        self.proxies = proxies
        self.search_key = search_key

    def get_search_key(self):
        return self.search_key

    def get_proxies(self):
        return self.proxies

    '''
    ����˵��������ؼ��֣�ͨ���ؼ����ڰٶȰٿ��н�������
    ����˵����proxies: �����ַ
            searchKey: �����ؼ���
    '''
    def baiduSpider(self):
        url = "http://baike.baidu.com/item/%s" % self.search_key
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        # ��������
        response = requests.get(url, headers=headers, proxies=self.proxies)
        html_ele = etree.HTML(response.text)
        # ʹ��xpathƥ�����ݣ���ȡ��ƥ�䵽���ַ����б�
        result_list = html_ele.xpath('//div[contains(@class, "lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()')
        # �������ݣ�ȥ���հ�
        filter_result = [item.strip("\n") for item in result_list]
        # ��ϴ��\xa0
        filter_result = [item.replace(u'\xa0', u'') for item in filter_result]
        # ƴ���ַ�����Ȼ�󷵻ؽ��
        return "".join(filter_result)


    '''
    ����˵�����ٶȰٿ�����02��ʹ��BeautifulSoupʵ��������ϴ����
    '''
    def baiduSpider02(self):
        # �洢��ϴ������list�б�
        last_list = list()
        url = "http://baike.baidu.com/item/%s" % self.search_key
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        # ��������
        response = requests.get(url, headers=headers, proxies=self.proxies)
        # �����ȡ������html�ı���ʹhtml�ı��ļ��е����ݷ���html��ǩ�﷨�淶
        soup = sp(response.text, "lxml")
        # ��ȡclass = main-content�е��ı�����
        results = soup.select(".main-content")
        # ��ȡ�ڲ����ı�����
        for item in results:
            last_list.append(item.get_text())
        # print(last_list)
        # �������ݣ�ȥ���հ�
        filter_result = [item.replace(u"\n", u'') for item in last_list]
        # ��ϴ��\xa0
        filter_result = [item.replace(u'\xa0', u'') for item in filter_result]
        # ��������е�[XXX]����
        pat = re.compile(r'\[.*?\]')
        filter_result = [re.sub(pat, '', item) for item in filter_result]
        # print(filter_result)
        last_val = "".join([item for item in filter_result])
        # print(last_val)
        file = open("../txts/tempTxt01.txt", "w", encoding="utf-8")
        # ����gbk�޷����������
        file.write(last_val.encode("utf-8", 'ignore').decode("utf-8", "ignore"))
        file.close()
        print("�ļ�д����ɣ�����")



if __name__ == '__main__':
    print("�ٶ�����Я���������ɣ���")
    proxies = {
        'http': 'http://@58.20.184.187:9091',
        'http': 'http://@101.200.127.149:3129',
        # 'http': 'http://@27.42.168.46:9091',
        # 'http': 'http://@47.106.105.236:80'
    }
    key_words = input("��������Ҫ��ѯ�Ĺؼ���:")
    baidus = BaiduBaikeSpiderUtils(proxies, key_words)
    resultTemp = baidus.baiduSpider02()
    print("resultTemp��ֵΪ��", resultTemp)
    # ���ɴ����ļ�
    wordsUtils = WordCloudUtils(key_words)
    wordsUtils.createCloudWord()
    print("���н���")