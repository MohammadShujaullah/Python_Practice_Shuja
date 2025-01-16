## 10.   for nth febonacci number 
 
a=0
b=1
num=int(input("enter the vlue of number :"))
print(a,b,end=" ")
for i in range (1,num-1):
    c=a+b
    a=b
    b=c
    print(c ,end=" ")                       ## by use of funtion 
    def fibonacci(num):
        a=0
        b=1
        if num<0:
            print("incorrect input")
        elif num==0:
            return a
        elif num == 1:
            return b
        else:
            for i in range (2,num):
                c=a+b
                a=b
                b=c
            return b                # drive program 
        print(fibonacci(8))
     
        

