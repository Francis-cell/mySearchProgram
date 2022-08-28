# coding=gbk
import requests
# �������������Զ���ȫ������ȱʧ��html��ǩ
from lxml import etree
import time
import json

# ��ȡ����ip�ĵ�ַ
def get_all_proxy(page):
    url = 'https://free.kuaidaili.com/free/inha/%s' % page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    html_ele = etree.HTML(response.text)
    result = etree.tostring(html_ele)
    # print(result.decode('utf-8'))
    ip_eles = html_ele.xpath('//td[@data-title="IP"]/text()')
    port_eles = html_ele.xpath('//td[@data-title="PORT"]/text()')
    print(ip_eles)
    print(port_eles)
    # ����ip�б�
    proxy_list = []
    for i in range(0, len(ip_eles)):
        # ������ip�Ƿ����
        proxy_list.append(get_useful_proxy(ip_eles[i], port_eles[i]))
    return proxy_list


'''
����˵����ɸѡ��Ч��ip��ַ
����˵����host��ip��ַ
        port��ip��ַ��Ӧ�Ķ˿ں�
'''
def get_useful_proxy(host, port):
    type = 'http'
    proxies = {}
    proxy_str = "%s://@%s:%s" % (type, host, port)
    url = 'http://www.baidu.com/'
    proxy_dict = {
        'http': proxy_str,
        'https': proxy_str
    }
    try:
        start_time = time.time()
        response = requests.get(url, proxies=proxy_dict, timeout=5)
        if response.status_code == 200:
            end_time = time.time()
            print('������ã�' + proxy_str)
            print('��ʱ:' + str(end_time - start_time))
            proxies['type'] = type
            proxies['host'] = host
            proxies['port'] = port
            proxiesJson = json.dumps(proxies)
            with open('./files/verifiedProxy.json', 'a+') as f:
                f.write(proxiesJson + '\n')
            print("��д�룺%s" % proxy_str)
            return proxy_str
        else:
            print('����ʱ')
    except:
        print('��������--------------->' + proxy_str)


if __name__ == '__main__':
    print("��ȡ��Ѵ�����վ�еĴ���ip")
    # ѡȡǰʮҳ����ʹ��
    for i in range(1, 11):
        proxy_list = get_all_proxy(i)
        time.sleep(20)
        print(proxy_list)
