# coding=gbk
import random

from bs4 import BeautifulSoup as sp
from random import choice
import requests
from urllib.parse import quote
from lxml import etree
import re


if __name__ == '__main__':
    print("ͼƬ���棡����")
    search_key = "��ţ"
    # 0��ǰ��׼��������
    proxies = {
        # 'http': 'http://@101.200.127.149:3129',
        'http': 'http://@223.96.90.216:8085',
        # 'http': 'http://@120.194.55.139:6969',
        # 'http': 'http://@47.106.105.236:80',
    }

    # 1��׼��url�׶�
    # ͼƬ��Դ����ַ
    url = "https://pixabay.com/zh/images/search/%s" % quote(search_key)

    # 2��׼������ͷ��Ϣ
    headers = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
    ]

    # 3����������
    response = requests.get(url,
                            headers={
                                'User-Agent': choice(headers),
                                'x-ms-blob-type': 'BlockBlob',
                                'x-ms-lease-status': 'unlocked',
                                'x-ms-request-id': '5b6e609c-601e-0078-3588-bb68d0000000',
                                'x-ms-version': '2009-09-19'
                            },
                            proxies=proxies)
    # �����ȡ������html�ı���ʹhtml�ı��ļ��е����ݷ���html��ǩ�﷨�淶
    # soup = sp(response.text, "lxml")
    html_ele = etree.HTML(response.text)
    strResult = etree.tostring(html_ele, encoding='gbk').decode('gbk')
    print(strResult)
    # ����������Ľ�����õ���ʱ�ļ���
    file = open("../txts/tempTxt.txt", "w")
    file.write(strResult)
    file.close()
    print("�ļ�д����ɣ�����")