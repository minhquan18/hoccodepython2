from re import split
from numpy import append
from ngay3 import *
def main():
    a =Linklist
    docfile = open('minhquan.txt',mode= 'r')
    quan=docfile.read()
    quan =quan.split('\n')
    for i in range (len(quan)):
        b = quan[i].split(',')
        a.AddHead(a,b[0],b[1],b[2])
    docfile.close()
    a.Menu(a)
if __name__ == '__main__':
    main()