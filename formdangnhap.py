from re import split
from ngay3 import *
import PySimpleGUI as sg
from pandas import value_counts
sg.theme_text_color = 'Black'
sg.theme_button_color = ('White')
sg.theme_background_color('Yellow')
layout = [
    [sg.Text('ID',background_color='Yellow',text_color='Black',size=(8,1),justification='Left'),sg.Input(key = 'ID')],
    [sg.Text('Password',background_color='Yellow',text_color= 'Black',size=(8,1),justification='Left'),sg.Input(key= 'Password')],
    [sg.Text('',key='tinnhan',background_color='Yellow',text_color='Red',size=(25,1)),sg.Button('Đăng Nhập',key='C',size=(10,1)),sg.Button('Đăng ký',key='DK',size=(10,1))],
    
]

layout2 = [
    [sg.Text(background_color= "Yellow",size = (10,1)),sg.Text('MENU',background_color='Yellow',text_color='Black',size=(8,1),justification='Middle')],
    [sg.Text('1:Xem Thông Tin',background_color='Yellow',text_color='Black'),sg.Button('1',key= '_1',size=(5,1))],
    [sg.Text('2:Rút Tiền',background_color='Yellow',text_color='Black',justification='Left'),sg.Button('2',key='_2',size =(5,1))]
]
layout3 = [
    [sg.Text('ID',background_color='Yellow',text_color='Black',size=(8,1),justification='Left'),sg.Input(key = 'ID')],
    [sg.Text('Password',background_color='Yellow',text_color= 'Black',size=(8,1),justification='Left'),sg.Input(key= 'Password')],
    [sg.Text(background_color='Yellow',size=(25,1)),sg.Button('Đăng Nhập',key='C',size=(10,1)),sg.Button('Đăng ký',key='DK',size=(10,1))],
    [sg.Text(size= (10,1),background_color='Yellow'),sg.Text('Sai mật khẩu',background_color='Yellow',text_color='Red',justification='Middle')]
]

