# coding=gbk

class DataSaveUtils(object):
    def __init__(self):
        super(DataSaveUtils, self).__init__()
        # 创建一个全局的变量(一个空的字典，用来放置后续传进来的数据)
        global datas
        datas = dict()
        self.datas = datas


    def getData(self):
        return self.datas


    '''
    方法说明：将获取到的数据临时存储起来
    '''
    def setData(self, innerKey, innerValue):
        datas[innerKey] = innerValue

    '''
    方法说明：颠倒字典
    '''
    def reverseDict(self):
        keys = list(self.datas.keys())
        values = list(self.datas.values())
        keys.reverse()
        values.reverse()
        return(dict(zip(keys, values)))



if __name__ == '__main__':
    print("数据临时存储方法")
    dsu = DataSaveUtils()
    dsu.setData("a", "1")
    dsu.setData("b", "2")
    print(dsu.getData())
    print(dsu.reverseDict())
