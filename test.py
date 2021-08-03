import re

ip='192.168.101.134'
a=[]
print(ip[0])
for i in range(len(ip)):
    a.append(ip[i])
print(a)
c=a[:]
a.reverse()

b=''
num=0
for j in range(len(ip)):
    if c[j]=='.':
        num+=1
    if num!=2 and c[j]!='.':
        b+=c[j]

print(b)