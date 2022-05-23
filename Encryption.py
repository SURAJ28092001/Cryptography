#D.R. D Y Patil Institute of Engineering, Management, and Research, Pune-411044
import random
a=str(input("Enter the statement to be encrypted : "))
l = len(a)
lis1=[]
lis2=[]
lis3=[]
sec=0
st = ""
v=0
c=[1,2,3,4,5,6,7,8,9,10]
d=random.choice(c)
for i in a:
    if ord(a[sec]) <= 79:
        ch = ord(a[sec]) + d + sec
        count=0
        ch1=d+sec
        if ch > 126:
            while ch > 126:
                ch = ch - d
                count+=1
            count = count*d
            lis1.append(ch)
            lis2.append(ch1)
            lis3.append(count)
            st = st + chr(ch)
        else:
            count = count*d
            lis1.append(ch)
            lis2.append(ch1)
            lis3.append(count)
            st = st + chr(ch)
    else:                                                             
        ch = ord(a[sec]) - d - sec
        count=0
        ch1= - d - sec
        if ch < 32:
            v=1
            while ch < 32:
                ch = ch + d
                count+=1
            count = count*d
            lis1.append(ch)
            lis2.append(ch1)
            lis3.append(count)
            st = st + chr(ch)
        else:
            count = count*d
            lis1.append(ch)
            lis2.append(ch1)
            lis3.append(count)
            st = st + chr(ch)
    sec = sec + 1
print('The Encryted Statement is : ',st)




































