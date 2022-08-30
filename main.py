# coding=gbk
'''
项目描述：比如我想学习某方面的知识，它搜出来的结果可以附带一些例子，并举例说明
        给出的案例贴近日常、通俗易懂
        如果这个词，涉及实验、实验步骤等，能够提供一些视频链接，方便拓展知识
'''
from utils.BaiduBaikeSpiderUtils import BaiduBaikeSpiderUtils as baidus
from flaskFiles import spiderFlask as sf

if __name__ == '__main__':
    print("关键词含义搜索项目！！！")
    proxies = {
        #'http': 'http://@101.200.127.149:3129',
        'http': 'http://@223.96.90.216:8085',
        # 'http': 'http://@120.194.55.139:6969',
        # 'http': 'http://@47.106.105.236:80',
    }
    sf.mains(proxies)

