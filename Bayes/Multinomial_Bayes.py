from sklearn.naive_bayes import MultinomialNB  #多项式分布朴素贝叶斯
import numpy as np
import sklearn.model_selection as train
from sklearn.metrics import accuracy_score
import os

#数据目录
FilePath = os.path.abspath('..')+"\\data"


def loadData(filename,type):
    data = np.loadtxt(filename, dtype=type, delimiter=',',skiprows=2)
    x,y=np.split(data,indices_or_sections=(1,),axis=1)
    #后十个为属性值，第一个为标签
    x ,y= y[:,1:],x
    #前十个为属性值
    x_train,x_test,y_train,y_test=train.train_test_split(x,y,random_state=1,train_size=0.6)
    #随机划分训练集与测试集
    return x_train,x_test,y_train,y_test

def Train_Bayes(x_train,y_train):
    clf = MultinomialNB()
    clf.fit(x_train, y_train.ravel())
    return clf


def Test_Bayes(x_train,x_test,y_train,y_test,clf):
    if clf is None:
        raise IOError("Must input a clf!")
    y_hat = clf.predict(x_train)
    score = accuracy_score(y_hat, y_train)
    print('训练集准确率：{}'.format(score))
    y_hat=clf.predict(x_test)
    score=accuracy_score(y_hat,y_test)
    print('测试集准确率：{}'.format(score))




if __name__ == '__main__':
    x_train1, x_test1, y_train1, y_test1 = loadData(FilePath + '\\new_data.txt', float)
    clf1 = Train_Bayes(x_train1, y_train1)
    print('随机干扰前：')
    Test_Bayes(x_train1, x_test1, y_train1, y_test1, clf1)

    print('-------------------------------------------------------------------')
    print('random=5,max=10数据：')
    x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\random=5,max=10.txt', int)
    clf2 = Train_Bayes(x_train2, y_train2)
    Test_Bayes(x_train2, x_test2, y_train2, y_test2, clf2)

    print('-------------------------------------------------------------------')
    print('random=10,max=10数据：')
    x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\random=10,max=10.txt', int)
    clf2 = Train_Bayes(x_train2, y_train2)
    Test_Bayes(x_train2, x_test2, y_train2, y_test2, clf2)

    print('-------------------------------------------------------------------')
    print('random=15,max=10数据：')
    x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\random=15,max=10.txt', int)
    clf2 = Train_Bayes(x_train2, y_train2)
    Test_Bayes(x_train2, x_test2, y_train2, y_test2, clf2)

    print('-------------------------------------------------------------------')
    print('random=20,max=10数据：')
    x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\random=20,max=10.txt', int)
    clf2 = Train_Bayes(x_train2, y_train2)
    Test_Bayes(x_train2, x_test2, y_train2, y_test2, clf2)

    print('-------------------------------------------------------------------')
    print('random=25,max=10数据：')
    x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\random=25,max=10.txt', int)
    clf2 = Train_Bayes(x_train2, y_train2)
    Test_Bayes(x_train2, x_test2, y_train2, y_test2, clf2)

    print('-------------------------------------------------------------------')
    print('random=30,max=10数据：')
    x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\random=30,max=10.txt', int)
    clf2 = Train_Bayes(x_train2, y_train2)
    Test_Bayes(x_train2, x_test2, y_train2, y_test2, clf2)
