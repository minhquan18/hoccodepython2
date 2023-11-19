from os import system
from turtle import clear
from unittest import case
from numpy import longlong

number = int
class NODE:
    id= int
    password = str
    tien = longlong
    pNext = None
    def __init__(self,id ,password,tien):
        self.id = id 
        self.password = password
        self.tien = tien
        self.pNext = None
class Linklist:
    pHead = None
    pTail = None
    def __init__(self):
        self.pHead = None
        self.pTail = None
    def AddHead(self,id,password,tien):
        pNode = NODE(id,password,tien)
        if(self.pHead == None):
            self.pHead = pNode
        else:
            pNode.pNext = self.pHead
            self.pHead = pNode
    def Print(self):
        pNode =self.pHead
        while pNode != None:
            print(pNode.id,' ',pNode.ten,' ',pNode.tien,'-->',end=' ')
            pNode = pNode.pNext
    def BrowserID(self,id):
        pNode =self.pHead
        while pNode!=None:
            if int(pNode.id) == id:
                return 1 ; break
            else :
                pNode = pNode.pNext
        return 2
    def CheckID(self,id,password:str):
        i = self.BrowserID(self,id)
        if i == 1:
            pNode = self.pHead
            while pNode != None:
                if int(pNode.id) == id:
                    if pNode.password == password:
                        self.Displaysuccessuser(self,pNode)
                    else :
                        print('Sai mat khau')
                        self.Menu(self)
                pNode = pNode.pNext
        elif i == 2:
            print('Tai Khoan khong ton tai')
    def Displaysuccessuser(self,a:NODE):
         for i in range(4):
            if i ==0:
                print('*'*20)
            elif i == 3:
                print('*'*20)
            elif i == 2:
                print('*',' '*1,'NGAN HANG MQ ','','*')
         print('1: Xem thong tin ')
         print('2: Chuyen Tien ')
         print('3: Rut tien ')
         print('4: Thoat')
         number = int(input('Moi ban chon'))
         if number == 1:
             print(a.id,'\n',a.password,'\n',a.tien,'\n')
         elif number == 2:
             pass
         elif number == 3:
             pass
         elif number == 4:
            if system('CLS'):
                    system('clear')
            return self.Menu(self)
    def CheckIDs(self,id,password):
        pNode = self.pHead
        while pNode != None:
            if(int(pNode.id) == int(id)):
                if(str(pNode.password) == str(password)):
                    return 1; break
                else:
                    return 2 ; break
            pNode= pNode.pNext
        return 3
        
    def LOCKPASS(self,id):
        pNode = self.pHead
        while pNode.id != id:
            pNode = pNode.pNext
        pNode.password = 'khoalekimminhquan'
        self.WRITELOCKFILE(self)
    def WRITELOCKFILE(self):
        b = ''
        docfile2 = open('minhquan.txt','w+t')
        pNode = self.pHead
        while pNode != None:
            b = str(pNode.id) + ',' + str(pNode.password)+ ',' + str(pNode.tien)+'\n'
            pNode = pNode.pNext
            docfile2.writelines(b)
        

           

        