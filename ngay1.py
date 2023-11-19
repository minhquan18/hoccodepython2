from pipes import Template

class NODE:
    sdt = str
    goidi = int 
    goiden =int 
    pnext = None
    def __init__(self,sdt,goidi,goiden) :
        self.sdt= sdt
        self.goidi = goidi
        self.goiden = goiden
        self.pnext = None

class Linklist:
    pHead =None
    pTail = None
    def __init__(self):
        self.pHead = None
        self.pTail= None
    def Addhead(self,a,b,c):
        pNode = NODE(a,b,c)
        if(self.pHead == None):
                self.pHead = pNode
        else :
             pNode.pnext = self.pHead
             self.pHead =pNode
    def printlist(self):
         pNode = self.pHead
         while pNode != None:
            print(pNode.sdt,' ',pNode.goiden,' ',pNode.goidi,'-->',end= ' ')
            pNode = pNode.pnext
    def Timsococgoiden(self):
        pNode = self.pHead
        while(pNode != None):
             pTemp = pNode.pnext
             while(pTemp!=None):
                 if(int(pTemp.goiden) > int(pNode.goiden)):
                      self.swap(self,pTemp,pNode)
                 pTemp = pTemp.pnext
             pNode = pNode.pnext
    def swap(self,a:NODE,b:NODE):
        x =a.goiden
        a.goiden = b.goiden
        b.goiden = x
        y =a.goidi
        a.goidi = b.goidi
        b.goidi = y
        z =a.sdtz
        a.sdt = b.sdt
        b.sdt = z
            
            
            
try:
     a = Linklist
     b = int
     while b!=0:
          b=str(input())
          if b == str(0):
              break
          if b!=str(0):
            c=int(input())
            d=int(input())
            a.Addhead(a,b,c,d)
     a.Timsococgoiden(a)
     a.printlist(a)
except:
     print('loi')