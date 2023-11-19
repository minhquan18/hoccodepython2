from ast import Break
from msilib.schema import TextStyle
from pydoc import text
from re import T
import PySimpleGUI as sg
import ngay2 
import sys
sg.theme("DarkBlue13")
layout = [
    [sg.Text("Hi Em Yêu <3",background_color="White",text_color="Tan",justification='Left')],
    [sg.Text(" Em có Yêu Anh Không",size=(20,1)),sg.Button('Có',key ='C',size = (5,1)),sg.Button('Không',key = 'K',size = (5,1))]
    ]
layout2 = [
    [sg.Text('Thật Không',background_color="White",text_color= "Tan",justification='Left')],
    [sg.Text('Chỗ đầu tiên mình hẹn hò ở đâu?'),sg.Input(size= (50,10))],
    [sg.Button('Xác Nhận',key ='C',size=(10,1))]
]
layout3 = [
    [sg.Text('ĐỒ TỒI',background_color="Black",text_color= "White",auto_size_text='ĐỒ TỒI',justification='Left',size=(20,5))],
    [sg.Button('Xác Nhận',size= (10,1))]
]
window =sg.Window("Anh gui tang em ne",layout)
manhinh2= sg.Window("Chúc mừng em ",layout2)
manhinh3 = sg.Window('ĐỒ TỒI',layout3)
try:
    event,value = window.read()
    if event == sg.WIN_CLOSED:
        Break
    elif event == 'C':
         a,b= manhinh2.read()
         if(a =='C'):
             window.read()
    
    elif event == 'K':
         a,b= manhinh3.read()
         if(a =='C') and b == ' thật':
             window.read()
    

except:
    print('loi')