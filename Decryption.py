from Encryption import l,st,lis1,lis2,v,lis3
rub=input("Let's check that our algorithm is correct or not. Press enter to decrypt the message.")
sec=0
st1=""
for i in st:
    if v == 1:
        if lis2[sec]<0:
            c1 = lis1[sec] - lis2[sec] - lis3[sec]
        else:
            c1 = lis1[sec] - lis2[sec] + lis3[sec]
    else:
        c1 = lis1[sec] - lis2[sec] + lis3[sec]
    st1 = st1 + chr(c1)
    sec = sec + 1
print("The Decrypted Statement is : ",st1)
rub1=input("The Decrypted Statement shows that our algorithm is correct.")
