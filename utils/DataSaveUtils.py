# coding=gbk

class DataSaveUtils(object):
    def __init__(self, num):
        super(DataSaveUtils, self).__init__()
        # ����һ��ȫ�ֵı���(һ���յ��ֵ䣬�������ú���������������)
        global datas
        datas = dict()
        self.datas = datas
        self.num = num


    def getData(self):
        return self.datas


    '''
    ����˵��������ȡ����������ʱ�洢����
    '''
    def setData(self, innerKey, innerValue):
        datas[innerKey] = innerValue
        return self.datas

    '''
    ����˵�����ߵ��ֵ�
    '''
    def reverseDict(self, dicts):
        keys = list(dicts.keys())
        values = list(dicts.values())
        keys.reverse()
        values.reverse()
        return(dict(zip(keys, values)))


    '''
    ����˵��������һ���������ֵ��ֶΣ�����ɾ�����һ��Ԫ��
    '''
    def withNumDict(self):
        # ��ȡ�ֵ����Եļ�ֵ
        keys = list(self.datas)
        if (len(self.datas) == self.num + 1):
            # �Ƴ����һ��Ԫ��
            # self.datas.popitem()
            # �Ƴ���һ��Ԫ��
            self.datas.pop(keys[0])
        return self.datas
