# 梅森旋转算法   -xlxw
# 参考:mersenne twister from wikipedia

# import
from time import time
import numpy as np
import os
import random

# var
index = 624
MT = [0] * index
# MT[0] ->seed
# 数据目录
FilePath = os.path.abspath('..') + "\\final_data"

def inter(t):
    return (0xFFFFFFFF & t)  # 取最后32位->t


def twister():
    global index
    for i in range(624):
        y = inter((MT[i] & 0x80000000) + (MT[(i + 1) % 624] & 0x7fffffff))
        MT[i] = MT[(i + 397) % 624] ^ y >> 1
        if y % 2 != 0:
            MT[i] = MT[i] ^ 0x9908b0df
    index = 0


def exnum():
    global index
    if index >= 624:
        twister()
    y = MT[index]
    y = y ^ y >> 11
    y = y ^ y << 7 & 2636928640
    y = y ^ y << 15 & 4022730752
    y = y ^ y >> 18
    index = index + 1
    return inter(y)


def mainset(seed):
    MT[0] = seed  # seed
    for i in range(1, 624):
        MT[i] = inter(1812433253 * (MT[i - 1] ^ MT[i - 1] >> 30) + i)
    return exnum()


# BOX-MULLER 伪随机数生成方法
# 处理[0,1]范围的数据
def boxmuller():
    # boxmuller()[0]
    while (1):
        summa = 1
        size = 1
        x = np.random.uniform(size=size)
        y = np.random.uniform(size=size)
        z = np.sqrt(-2 * np.log(x)) * np.cos(2 * np.pi * y)
        q = z * summa
        if q > 0:
            return q

#根据属性个数生成随机数
def Random_list(num,n):
    random_list = []
    while len(random_list) < num:   #随机数个数
        y = random.uniform(1,n)  # 1-n之间抽样随机数
        if round(y) not in random_list:
            random_list.append(round(y))
    return random_list    #返回随机数组

def our_main(num,rate,n,outfilename):
    str_data = ''
    rate=float(rate/100)
    #定义输入输出文件
    file = open(FilePath + '\\data.txt', 'r')
    outfile = open(FilePath + '\\'+outfilename, 'w')
    lines = file.readlines()
    for line in lines:
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        list_data = Random_list(num,n-1)   #随机数组
        for i in list_data:    #对随机位置的数干扰处理
            idata = float(line[i])    #取出该位置的数
            #根据给定比列确定随机数生成区间，[min_data,max_data]
            min_idata = idata * (1-rate)
            max_idata = idata * (1+rate)

            so = mainset(int(time())) / (2 ** 32 - 1)
            #O线性同余法计算随机数
            #在min_data，max_data之间取一个随机数替代之前的数
            new_idata = min_idata + float((max_idata - min_idata) * so)
            line[i] = round(new_idata,3)   #保留三位小数



        #将数据存入文件
        for every in line:
            str_data = str_data + str(every) + ','
        str_data = str_data[:-1]
        str_data = str_data + '\n'
        outfile.write(str_data)

        str_data = ''

def mul_main(num,rate,outfilename):
    str_data = ''
    rate = float(rate / 100)

    # 定义输入输出文件
    file = open(FilePath + '\\data.txt', 'r')
    outfile = open(FilePath + '\\' + outfilename, 'w')
    lines = file.readlines()
    for line in lines:
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        list_data = Random_list(num,n)  # 随机数组
        for i in list_data:  # 对随机位置的数干扰处理
            idata = float(line[i])  # 取出该位置的数
            line[i] = idata*(1+rate)

        # 将数据存入文件
        for every in line:
            str_data = str_data + str(every) + ','
        str_data = str_data[:-1]
        str_data = str_data + '\n'
        outfile.write(str_data)

        str_data = ''

def add_main(num,n,range,outfilename):
    str_data = ''
    # 定义输入输出文件
    file = open(FilePath + '\\data.txt', 'r')
    outfile = open(FilePath + '\\' + outfilename, 'w')
    lines = file.readlines()
    for line in lines:
        line = line.split(',')
        line[-1] = line[-1].replace('\n', '')
        list_data = Random_list(num,n-1)  # 随机数组
        for i in list_data:  # 对随机位置的数干扰处理
            idata = float(line[i])  # 取出该位置的数
            # 根据给定比列确定随机数生成区间，[min_data,max_data]
            min_idata = idata - range
            max_idata = idata + range

            so = mainset(int(time())) / (2 ** 32 - 1)
            # O线性同余法计算随机数
            # 在min_data，max_data之间取一个随机数替代之前的数
            new_idata = min_idata + float((max_idata - min_idata) * so)
            line[i] = round(new_idata, 3)  # 保留三位小数


        # 将数据存入文件
        for every in line:
            str_data = str_data + str(every) + ','
        str_data = str_data[:-1]
        str_data = str_data + '\n'
        outfile.write(str_data)

        str_data = ''

def main(num,range,outfilename,TYPE):
    if TYPE=='mul':
        mul_main(num,range,outfilename)#此处range为百分比
    elif TYPE=='our':
        our_main(num,range,outfilename)#此处range为百分比
    else:
        add_main(num,n,range,outfilename)#此处range为范围
if __name__ == '__main__':
    # 第一个参数是随机属性的个数，第二个参数是比率
    # 比率k：在n(1-k)和n(1+k)之间取一个随机数
    n = 30
    for i in range(1,n):
        add_main(i,n,50,'add {},30.txt'.format(i))
        print('one done!')
