# coding=gbk

class DataSaveUtils(object):
    def __init__(self, num):
        super(DataSaveUtils, self).__init__()
        # 创建一个全局的变量(一个空的字典，用来放置后续传进来的数据)
        global datas
        datas = dict()
        self.datas = datas
        self.num = num


    def getData(self):
        return self.datas


    '''
    方法说明：将获取到的数据临时存储起来
    '''
    def setData(self, innerKey, innerValue):
        datas[innerKey] = innerValue
        return self.datas

    '''
    方法说明：颠倒字典
    '''
    def reverseDict(self, dicts):
        keys = list(dicts.keys())
        values = list(dicts.values())
        keys.reverse()
        values.reverse()
        return(dict(zip(keys, values)))


    '''
    方法说明：保存一定数量的字典字段，总是删除最后一个元素
    '''
    def withNumDict(self):
        # 获取字典所以的键值
        keys = list(self.datas)
        if (len(self.datas) == self.num + 1):
            # 移除最后一个元素
            # self.datas.popitem()
            # 移除第一个元素
            self.datas.pop(keys[0])
        return self.datas
