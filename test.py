import re

ip='192.168.104.19'
a=[]

test(2)

def test(a):
    print(a)

def maskip2(userip):
    for i in range(len(ip)):
        a.append(ip[i])

    b=''
    num=0
    for j in range(len(ip)):
        if a[j]=='.':
            num+=1
        if num!=2:
            b+=a[j]
        elif num==2:
            if a[j]=='.':
                b+=a[j]
                for n in range(3):
                    b+='*'

print(b)


#ip遮掩网段函数
def maskip(userip):
    a = []

    for i in range(len(userip)):
        a.append(userip[i])

    b = ''
    num = 0
    for j in range(len(userip)):
        if a[j] == '.':
            num += 1
        if num != 2:
            b += a[j]
        elif num == 2:
            if a[j] == '.':
                b += a[j]
            else:
                b += '*'

    return b