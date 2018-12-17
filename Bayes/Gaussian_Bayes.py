from sklearn.naive_bayes import GaussianNB  #高斯朴素贝叶斯
import numpy as np
import sklearn.model_selection as train
from sklearn.metrics import accuracy_score
import os

#数据目录
FilePath = os.path.abspath('..')+"\\final_data"


def loadData(filename,type):
    data = np.loadtxt(filename, dtype=type, delimiter=',',skiprows=2)
    x,y=np.split(data,indices_or_sections=(1,),axis=1)
    #后十个为属性值，第一个为标签
    x ,y= y[:,1:],x
    #前十个为属性值
    x_train,x_test,y_train,y_test=train.train_test_split(x,y,random_state=1,train_size=0.6)
    #随机划分训练集与测试集
    return x_train,x_test,y_train,y_test

def Train(x_train,y_train):
    clf = GaussianNB()
    clf.fit(x_train, y_train.ravel())
    return clf


def Test(x_train,x_test,y_train,y_test,clf):
    if clf is None:
        raise IOError("Must input a clf!")
    y_hat = clf.predict(x_train)
    score = accuracy_score(y_hat, y_train)
    print('训练集准确率：{}'.format(score))
    y_hat=clf.predict(x_test)
    score=accuracy_score(y_hat,y_test)
    print('测试集准确率：{}'.format(score))


if __name__ == '__main__':
    print('乘法')
    x_train1, x_test1, y_train1, y_test1 = loadData(FilePath + '\\new_data.txt', float)
    clf1 = Train(x_train1, y_train1)
    print('随机干扰前：')
    Test(x_train1, x_test1, y_train1, y_test1, clf1)

    for i in range(1,31):
        print('------------------------------------------------------')
        print('random={},rate=50 数据：'.format(i))
        x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\mul {}, 50.txt'.format(i), float)
        clf2 = Train(x_train2, y_train2)
        Test(x_train2, x_test2, y_train2, y_test2, clf2)

    print()
    print()
    print()

    print('加法')
    x_train1, x_test1, y_train1, y_test1 = loadData(FilePath + '\\new_data.txt', float)
    clf1 = Train(x_train1, y_train1)
    print('随机干扰前：')
    Test(x_train1, x_test1, y_train1, y_test1, clf1)

    for i in range(1,31):
        print('------------------------------------------------------')
        print('random={},rate=30 数据：'.format(i))
        x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\add {}, 30.txt'.format(i), float)
        clf2 = Train(x_train2, y_train2)
        Test(x_train2, x_test2, y_train2, y_test2, clf2)

    print()
    print()
    print()


    print('我们的算法')
    x_train1, x_test1, y_train1, y_test1 = loadData(FilePath + '\\new_data.txt', float)
    clf1 = Train(x_train1, y_train1)
    print('随机干扰前：')
    Test(x_train1, x_test1, y_train1, y_test1, clf1)

    for i in range(1,31):
        print('------------------------------------------------------')
        print('random={},rate=50 数据：'.format(i))
        x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\{}, 50.txt'.format(i), float)
        clf2 = Train(x_train2, y_train2)
        Test(x_train2, x_test2, y_train2, y_test2, clf2)