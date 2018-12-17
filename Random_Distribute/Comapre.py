#比较干扰后数据和原数据的相似度
import os


# 数据目录
FilePath = os.path.abspath('..') + "\\data"

def Compare(cmpfilename,outfilename):
    #打开文件操作
    datafile=open(FilePath+'//new_data.txt','r')
    cmpfile=open(FilePath+'//'+cmpfilename,'r')
    outfile=open(FilePath+'//'+outfilename,'w')
    #把文件内容读出并转换成float格式的元组
    datalines=datafile.readlines()
    cmplines=cmpfile.readlines()
    data=[]
    for eachline in datalines:
        eachline=eachline.split(',')
        for i in range(0,len(eachline)):
            eachline[i] = float(eachline[i])
        data.append(eachline)
    cmp=[]
    for eachline in cmplines:
        eachline=eachline.split(',')
        for i in range(0,len(eachline)):
            eachline[i] = float(eachline[i])
        cmp.append(eachline)
    out=[]
    #开始对比数据
    for i in range(len(data)):
        line=[]
        for j in range(1,len(data[i])):#除去标签属性
            if data[i][j]==0:
                line.append(abs(cmp[i][j]-data[i][j]))
            elif cmp[i][j]==0:
                line.append(abs(cmp[i][j]-data[i][j]))
            else:
                difference=abs(1-float(cmp[i][j]/data[i][j]))
                line.append(abs(1-float(cmp[i][j]/data[i][j])))
        out.append(line)

    #存入输出文件
    str=''
    for line in out:
        for each in line:
            str=str+'{},'.format(each)
        str=str[:-1]+'\n'
    outfile.write(str)



if __name__ == '__main__':
    Compare(cmpfilename='5, 30.txt', outfilename='5, 30.cmp')
    Compare(cmpfilename='10, 10.txt', outfilename='10, 10.cmp')
    Compare(cmpfilename='10, 20.txt', outfilename='10, 20.cmp')
    Compare(cmpfilename='10, 30.txt', outfilename='10, 30.cmp')
    Compare(cmpfilename='10, 40.txt', outfilename='10, 40.cmp')
    Compare(cmpfilename='10, 50.txt', outfilename='10, 50.cmp')
    Compare(cmpfilename='10, 60.txt', outfilename='10, 60.cmp')
    Compare(cmpfilename='10, 70.txt', outfilename='10, 70.cmp')
    Compare(cmpfilename='10, 80.txt', outfilename='10, 80.cmp')
    Compare(cmpfilename='10, 90.txt',outfilename='10, 90.cmp')
    Compare(cmpfilename='10, 30.txt', outfilename='10, 30.cmp')
    Compare(cmpfilename='15, 30.txt', outfilename='15, 30.cmp')
    Compare(cmpfilename='20, 30.txt', outfilename='20, 30.cmp')
    Compare(cmpfilename='25, 30.txt', outfilename='25, 30.cmp')
    Compare(cmpfilename='30, 30.txt', outfilename='30, 30.cmp')
