# coding=gbk
import requests
# 这个库的作用是自动补全读出来缺失的html标签
from lxml import etree
import time
import json

# 获取代理ip的地址
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
    # 代理ip列表
    proxy_list = []
    for i in range(0, len(ip_eles)):
        # 检查代理ip是否可用
        proxy_list.append(get_useful_proxy(ip_eles[i], port_eles[i]))
    return proxy_list


'''
方法说明：筛选有效的ip地址
参数说明：host：ip地址
        port：ip地址对应的端口号
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
            print('代理可用：' + proxy_str)
            print('耗时:' + str(end_time - start_time))
            proxies['type'] = type
            proxies['host'] = host
            proxies['port'] = port
            proxiesJson = json.dumps(proxies)
            with open('./files/verifiedProxy.json', 'a+') as f:
                f.write(proxiesJson + '\n')
            print("已写入：%s" % proxy_str)
            return proxy_str
        else:
            print('代理超时')
    except:
        print('代理不可用--------------->' + proxy_str)


if __name__ == '__main__':
    print("爬取免费代理网站中的代理ip")
    # 选取前十页数据使用
    for i in range(1, 11):
        proxy_list = get_all_proxy(i)
        time.sleep(20)
        print(proxy_list)
