# coding=gbk
'''
��Ŀ��������������ѧϰĳ�����֪ʶ�����ѳ����Ľ�����Ը���һЩ���ӣ�������˵��
        �����İ��������ճ���ͨ���׶�
        �������ʣ��漰ʵ�顢ʵ�鲽��ȣ��ܹ��ṩһЩ��Ƶ���ӣ�������չ֪ʶ
'''
from utils.BaiduBaikeSpiderUtils import BaiduBaikeSpiderUtils as baidus
from flaskFiles import spiderFlask as sf

if __name__ == '__main__':
    print("�ؼ��ʺ���������Ŀ������")
    proxies = {
        # 'http': 'http://@58.20.184.187:9091',
        'http': 'http://@101.200.127.149:3129',
        # 'http': 'http://@27.42.168.46:9091',
        # 'http': 'http://@47.106.105.236:80'
    }
    sf.mains(proxies)

