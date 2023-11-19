from os import close
from pydoc import doc
from re import split
from turtle import clear
from ngay2 import * 
def main():
    docfile = open('minhquan.txt') 
    a = Linklist
    b =int 
    c = int
    d = 0
    f = docfile.readline()
    docfile = clear()

    f2 = f.split(',')
    p =len(f2)
    for i in range (0,p):
          p2 = f2[i].split('^')
          a.AddHead(a,p2[0],p2[1])
    a.Sort(a)
    
    docfile = open('minhquan.txt','w')
    docfile.write(str(a))
    a.Printlist(a)
    print()

if __name__ == '__main__':
        main()