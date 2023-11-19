from re import split
def timmax(c:list):
    max = c[0]
    for i in range(len(c)):
        if(int(c[i])> int(max)):
            max = c[i]
    return max
def Timsolonthu2(c: list):
    d = timmax(c)
    a = 0 
    secondmax = c[a]
    while secondmax == d:
        secondmax = c[a+1]
    for i in range(len(c)):
        if(c[i]>secondmax)and (c[i]<d):
            secondmax = c[i]
    return secondmax
def Timvitri(c:list):
    a = Timsolonthu2(c)
    for i in range(len(c)):
        if c[i] == a:
            vitri = i
    
    print(vitri)
def timmin(c:list):
    min = c[0]
    for i in range(len(c)):
        if(int(c[i])<int(min)):
            min= c[i]
    return min
def Timsobethu2(c: list):
    d = timmin(c)
    a = 0
    secondmin = c[a]
    while secondmin == d:
        secondmin = c[a+1]
    for i in range(len(c)):
        if(c[i]> d) and c[i]<secondmin:
            secondmin = c[i]
    return secondmin
def Timvitri2(c:list):
    a = Timsobethu2(c)
    for i in range(len(c)):
        if c[i] == a:
            print(i,end=' ')
def UCLN(a,b):
    if(a == 0):
        return int(a)+int(b)
    if(b == 0):
        return int(a)+int(b)
    while int(a)!= int(b):
        if int(a)> int(b) :
            a  =int(a) - int(b)
        else :
            b = int(b) - int(a)
    return int(a) 
def UCLNSTR(c:list):
    ucln = UCLN(c[0],c[1])
    for i in range(len(c)):
        j = i +1
        for j in range(j,len(c)):
            b = UCLN(c[i],c[j])
            if(int(b) > int(ucln)) and int(b)!=int(ucln):
                ucln = b 
    print(ucln)
def kiemtrasonguyento(a:int):
    uoc = 0
    for i in range(1,a+1):
        if(a%i == 0):
            uoc+=1
    if(uoc == 2):
        return a 
    else :
        return -1
def KTSO(c:list):
    b = [];
    for i in range(len(c)):
        j =i +1
        for j in range(j,len(c)):
            d =int(c[i])+int(c[j])
            a= kiemtrasonguyento(d)
            if(a == d):
                b.append(str(a))     
    k=timmin(b)
    print(list(b))
    print(k)
try:
    a = input()
    c = a.strip(' ').split(' ')

    #Timvitri(c)
    #Timvitri2(c)
    #print(end = '\n')
    #UCLNSTR(c)
    KTSO(c)
except:
    print('loi')