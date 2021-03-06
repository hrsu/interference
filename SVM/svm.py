from sklearn import svm as svm
import numpy as np
import sklearn.model_selection as train
#处理旧数据
from sklearn.metrics import accuracy_score
import os

# 数据目录
FilePath = os.path.abspath('..') + "\\Haberman Data"
def loadData(filename,type):
    data = np.loadtxt(filename, dtype=type, delimiter=',')
    x,y=np.split(data,indices_or_sections=(1,),axis=1)
    #后十个为属性值，第一个为标签
    x ,y= y[:,1:],x
    #前十个为属性值
    x_train,x_test,y_train,y_test=train.train_test_split(x,y,random_state=1,train_size=0.6)
    #随机划分训练集与测试集
    return x_train,x_test,y_train,y_test

def Train(x_train,y_train):
    '''
    kernel='linear'时，为线性核，C越大分类效果越好，但有可能会过拟合（defaul C=1）。
　　 kernel='rbf'时（default），为高斯核
    gamma值越小，分类界面越连续；gamma值越大，分类界面越“散”，分类效果越好，但有可能会过拟合。
　　decision_function_shape='ovr'时，为one v rest，即一个类别与其他类别进行划分，
　　decision_function_shape='ovo'时，为one v one，即将类别两两之间进行划分，用二分类的方法模拟多分类的结果。
    :param x_train: 数据集
    :param y_train: 分类标签
    :return:
    '''
    clf= svm.SVC(C=1,kernel='rbf',gamma=0.000001,decision_function_shape='ovo')
    clf.fit(x_train,y_train.ravel())
    return clf

def Test(x_train,x_test,y_train,y_test,clf=None):
    if clf is None:
        raise IOError("Must input a clf!")
    y_hat = clf.predict(x_train)
    score = accuracy_score(y_hat, y_train)
    print('训练集准确率：{}'.format(score))
    y_hat=clf.predict(x_test)
    score=accuracy_score(y_hat,y_test)
    print('测试集准确率：{}'.format(score))



if __name__ == '__main__':
    n=4
    x_train1, x_test1, y_train1, y_test1 = loadData(FilePath + '\\Haberman_data.txt', float)
    clf1 = Train(x_train1, y_train1)
    print('随机干扰前：')
    Test(x_train1, x_test1, y_train1, y_test1, clf1)

    for i in range(1,n):
        print('------------------------------------------------------')
        print('random={},rate=50 数据：'.format(i))
        x_train2, x_test2, y_train2, y_test2 = loadData(FilePath + '\\{} , 50.txt'.format(i), float)
        clf2 = Train(x_train2, y_train2)
        Test(x_train2, x_test2, y_train2, y_test2, clf2)
