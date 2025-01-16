# 9.check whether anumber is prime or not 
#  SHVAIB KHAN(22BEE035)

num=int(input("enter the value of number"))
flag=0

for i in range (2,(num//2+1)):  
                                
    if(num % i)==0:
        flag=1
        break
    else:
        flag=0

if(flag==0):
     print(num,"the number is aprime no.")

else:
          print(num,"is not aprime number ")        