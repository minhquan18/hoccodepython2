

class NODE:
    key = int 
    mu =int 
    pNext = None
    def __init__(self,key,mu):
        self.key = key
        self.mu = mu
        self.pNext =None

class Linklist:
    phead = None
    ptail= None
    size = 0
    def __init__(self):
        self.phead = None
        self.ptail =None
        self.size = int
    def AddHead(self,key,mu):
        pnode= NODE(key,mu)
        if(self.phead == None):
             self.phead =pnode
        else:
            pnode.pNext = self.phead
            self.phead = pnode
        (self.size) = (self.size+1)
    def Printlist(self):
        pnode =self.phead
        while(pnode != None):
                print(pnode.key,"^",pnode.mu,' ',end= ' ' )
                pnode=pnode.pNext
    def Addtail(self,key,mu):
        pNode = NODE(key,mu)
        if (self.phead == None):
              self.phead = pNode
              self.tail = pNode
        else :
             self.ptail.pNext = pNode
             self.ptail = pNode
             self.size = self.size+1
        
    def Delete(self):
        a = (int(input('nhap phan tu muon xoa :'))) 
        pnode = self.phead
        print(pnode.key)
        while (pnode.key!= a):
             pTemp = pnode
             pnode = pnode.pNext
        pTemp.pNext = pnode.pNext
        del(pnode.key)
        pnode.pNext = None
        size-=1
    def AddBack(self):
         a = int(input('nhap vi tri muon them vao phia sau: '))
         b= int(input('nhap so muon them vao phia sau: '))
         c = int(input('nhap so mu : '))
         pTemp = NODE(b,c)
         pNode = self.phead
         while(pNode.key != a):
              pNode = pNode.pNext
         pTemp.pNext = pNode.pNext
         pNode.pNext = pTemp
         (self.size) = (self.size+1)
    def Sort(self):
        pNode = self.phead
        while pNode!=None:
            pTemp = pNode.pNext
            while pTemp!=None:
                if (pTemp.mu>pNode.mu):
                     x= pNode.mu
                     pNode.mu = pTemp.mu
                     pTemp.mu =x
                     y = pNode.key
                     pNode.key = pTemp.key
                     pTemp.key = y
                     pTemp=pTemp.pNext
                else:
                    pTemp=pTemp.pNext
            pNode=pNode.pNext
                

         
