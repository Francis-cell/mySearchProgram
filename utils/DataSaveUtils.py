# coding=gbk

class DataSaveUtils(object):
    def __init__(self):
        super(DataSaveUtils, self).__init__()
        # ����һ��ȫ�ֵı���(һ���յ��ֵ䣬�������ú���������������)
        global datas
        datas = dict()
        self.datas = datas


    def getData(self):
        return self.datas


    '''
    ����˵��������ȡ����������ʱ�洢����
    '''
    def setData(self, innerKey, innerValue):
        datas[innerKey] = innerValue

    '''
    ����˵�����ߵ��ֵ�
    '''
    def reverseDict(self):
        keys = list(self.datas.keys())
        values = list(self.datas.values())
        keys.reverse()
        values.reverse()
        return(dict(zip(keys, values)))



if __name__ == '__main__':
    print("������ʱ�洢����")
    dsu = DataSaveUtils()
    dsu.setData("a", "1")
    dsu.setData("b", "2")
    print(dsu.getData())
    print(dsu.reverseDict())
