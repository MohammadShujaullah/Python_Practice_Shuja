#Python program for factorial of a number
#Shvaib Khan(22BEE035)
n=int(input("Enter the number:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print("The factorial is: ", fact)