docfile = open('minhquan.txt')
quan=docfile.readline()
minhquan = quan.split(',')
n= len(minhquan[2])
b = 'daohoa'
if(b in quan):
    print('true')

print(n)
docfile.close()