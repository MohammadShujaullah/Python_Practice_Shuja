# python program to check  armstrong no
# SHVAIB KHAN (22BEE035)
num=int(input("enter the value of number:"))

#initialise sum

sum=0

## find the sum of the cube of each digit

temp=num
while temp > 0:
    digit= temp % 10
    sum+= digit**3      
    temp=temp//10

    ## display the result
if num==sum:
    print(num," is a armstrong number")
else:
    print(num,"is not a armstrong number ")    
