#1
txt=open("postcard.txt", "r").read()
print(txt)

#2
txt=open("postcard.txt", "r").read()
h, b, t=tuple(txt.split('\n\n'))
print(b)

#3
txt=open("postcard.txt", "r").read()
h, b, t=tuple(txt.split('\n\n'))

import re

d=re.sub('[:,\.]', '', b)
print(d)

#4
txt=open("postcard.txt", "r").read()
h, b, t=tuple(txt.split('\n\n'))

import re

d=re.sub('[:,\.]', '', b)
d=d.upper()
print(d)

#5
txt=open("postcard.txt", "r").read()
h, b, t=tuple(txt.split('\n\n'))

import re

d=re.sub('[:,\.]', '', b)
d=d.upper()

password=[]
l = []
line = ""

for char in d:
    if char == '\n':
        l.append(line)
        line = ""
    else:
        line += char

if line:
    l.append(line)

for i in l:
    password+=i.split()[:2]

message=' '.join(password)
print(message)
