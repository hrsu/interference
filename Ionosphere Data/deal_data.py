iris={'b\n': 0, 'g\n': 1,'g':1,'b':0}
def deal(infilename,outfilename):
    infile = open(infilename)
    lines = infile.readlines()
    out = []
    for line in lines:
        line = line.split(',')
        val = line[-1]
        line = line[:-1]
        val = iris[val]
        line.insert(0,val)
        out.append(line)
    str = ''
    for line in out:
        line_str =''
        for each in line:
            line_str = line_str + '{},'.format(each)
        str = str + line_str[:-1]+'\n'
    print(str)
    outfile=open(outfilename,'w')
    outfile.write(str)
deal('Ionosphere Data Set.txt','Ionosphere_data.txt')