from turtle import update, window_height
from ngay3 import *
from  formdangnhap import *
i = 0
def CHECKLOGIN(a:Linklist,values,quan:sg.Window):
         giatri = a.CheckIDs(a,values['ID'],values['Password'])
         if(giatri == 1):
            quan.close()
            quan2 = sg.Window('NGÂN HÀNG MINH QUÂN',layout2)
            value=quan2.read()
            if value == '_1':
                 print('duoc rồi')
                 quan3 = sg.Window('Ngân Hàng lê kimminhquana')
                 quan3.read()
            elif value == '_2':
                 print('duoc rồi')
                 
         elif giatri  == 2:
            global i 
            i+=1
            if i < 3:
                  quan['tinnhan'].update('Sai mật khẩu')
                  LOGIN(a,quan)
            elif i == 3 :
                 a.LOCKPASS(a,values['ID'])
                 quan['tinnhan'].update('Tài Khoản Đã Bị Khóa')

                 LOGIN(a,quan)
         elif giatri == 3:
            i +=1
            quan['tinnhan'].update('Tài khoản không tồn tại')
            LOGIN(a,quan)
def LOGIN(a:Linklist,quan):
       event,values= quan.read()
       if event == sg.WIN_CLOSED:
           return 0
       elif event == 'C':
            CHECKLOGIN(a,values,quan)
def Readfile(a:Linklist):
      docfile = open('minhquan.txt',mode='r')
      quan=docfile.read()
      docfile.close()
      quan =quan.split('\n')
      for i in range (0,len(quan)):
            if quan[i] == '':
                  del(quan[i])
            else:
                  b = quan[i].split(',')
                  a.AddHead(a,b[0],b[1],b[2])
def main():
      global i 
      a = Linklist
      Readfile(a)
      quan = sg.Window('NGÂN HÀNG MINH QUÂN',layout= layout)
      LOGIN(a,quan)
if __name__ == '__main__':
     main()
    