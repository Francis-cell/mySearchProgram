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
    方法说明：输入关键字，通过关键字在百度百科中进行爬虫
    参数说明：proxies: 代理地址
            searchKey: 搜索关键词
    '''
    def baiduSpider(self):
        url = "http://baike.baidu.com/item/%s" % self.search_key
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        # 发起请求
        response = requests.get(url, headers=headers, proxies=self.proxies)
        html_ele = etree.HTML(response.text)
        # 使用xpath匹配数据，获取被匹配到的字符串列表
        result_list = html_ele.xpath('//div[contains(@class, "lemma-summary") or contains(@class,"lemmaWgt-lemmaSummary")]//text()')
        # 过滤数据，去掉空白
        filter_result = [item.strip("\n") for item in result_list]
        # 清洗掉\xa0
        filter_result = [item.replace(u'\xa0', u'') for item in filter_result]
        # 拼接字符串，然后返回结果
        return "".join(filter_result)


    '''
    方法说明：百度百科爬虫02，使用BeautifulSoup实现数据清洗操作
    '''
    def baiduSpider02(self):
        # 存储清洗后结果的list列表
        last_list = list()
        url = "http://baike.baidu.com/item/%s" % self.search_key
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        }
        # 发起请求
        response = requests.get(url, headers=headers, proxies=self.proxies)
        # 处理读取出来的html文本，使html文本文件中的内容符合html标签语法规范
        soup = sp(response.text, "lxml")
        # 获取class = main-content中的文本内容
        results = soup.select(".main-content")
        # 获取内部的文本内容
        for item in results:
            last_list.append(item.get_text())
        # print(last_list)
        # 过滤数据，去掉空白
        filter_result = [item.replace(u"\n", u'') for item in last_list]
        # 清洗掉\xa0
        filter_result = [item.replace(u'\xa0', u'') for item in filter_result]
        # 清除掉所有的[XXX]数据
        pat = re.compile(r'\[.*?\]')
        filter_result = [re.sub(pat, '', item) for item in filter_result]
        # print(filter_result)
        last_val = "".join([item for item in filter_result])
        # print(last_val)
        file = open("../txts/tempTxt01.txt", "w", encoding="utf-8")
        # 忽略gbk无法解码的内容
        file.write(last_val.encode("utf-8", 'ignore').decode("utf-8", "ignore"))
        file.close()
        print("文件写入完成！！！")



if __name__ == '__main__':
    print("百度爬虫携带词云生成！！")
    proxies = {
        'http': 'http://@58.20.184.187:9091',
        'http': 'http://@101.200.127.149:3129',
        # 'http': 'http://@27.42.168.46:9091',
        # 'http': 'http://@47.106.105.236:80'
    }
    key_words = input("请输入需要查询的关键词:")
    baidus = BaiduBaikeSpiderUtils(proxies, key_words)
    resultTemp = baidus.baiduSpider02()
    print("resultTemp的值为：", resultTemp)
    # 生成词云文件
    wordsUtils = WordCloudUtils(key_words)
    wordsUtils.createCloudWord()
    print("运行结束")